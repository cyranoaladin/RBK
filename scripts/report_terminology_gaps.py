#!/usr/bin/env python3
"""
Terminology gaps reporter v4.7
- unknown RBKTerm keys
- declared-but-unused RBKTerm keys
- uncovered acronyms (non couverts par lexique/affichages)
- uncovered technical tokens

Default: report only (exit 0). --strict can fail on uncovered counts.
"""

import argparse
import datetime
import os
import re
import subprocess
from collections import Counter, defaultdict
from pathlib import Path

REPORT_VERSION = "4.7"


# ------------------------------------------------------------
# Normalisation unique
# ------------------------------------------------------------
def normalize_token(raw: str) -> str:
    t = raw.replace("–", "-").replace("—", "-").replace("−", "-").replace("‐", "-")
    t = t.strip().strip("{}[]()").replace("~", " ").replace("\\%", "%")
    t = t.strip(".,;:)}]").strip("({[")
    t = re.sub(r"\s+", " ", t)
    return t.lower()


def normalize_variants(raw: str) -> set[str]:
    base = normalize_token(raw)
    variants = {base}
    if base.endswith("s") and len(base) > 3:
        variants.add(base[:-1])
    return variants


# ------------------------------------------------------------
# CLI
# ------------------------------------------------------------
def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="RBK Terminology gaps reporter")
    parser.add_argument("--root", default=".", help="root path to scan (default: .)")
    parser.add_argument(
        "--output",
        default="docs/TERMINOLOGY_REPORT.md",
        help="report output path (default: docs/TERMINOLOGY_REPORT.md)",
    )
    parser.add_argument(
        "--top",
        type=int,
        default=80,
        help="limit number of suspect tokens shown (default: 80)",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="exit 1 on critical gaps (unknown keys or large uncovered sets)",
    )
    parser.add_argument(
        "--include-covered",
        action="store_true",
        help="show terms déjà présents dans le lexique ou via affichage optionnel",
    )
    parser.add_argument(
        "--debug-token",
        help="affiche normalisation + statut covered pour un token donné",
    )
    return parser.parse_args()


# ------------------------------------------------------------
# Utils
# ------------------------------------------------------------
def walk_tex_files(root: Path, exclude_dirs: set[str]) -> list[Path]:
    tex_files: list[Path] = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in exclude_dirs and not d.startswith(".git")]
        for fname in filenames:
            if fname.endswith(".tex"):
                tex_files.append(Path(dirpath) / fname)
    return tex_files


def load_declared_entries(entries_path: Path):
    pattern = re.compile(
        r"\\DeclareRBKTerm\{([^}]+)\}\{([^}]+)\}\{([^}]+)\}\{([^}]*)\}"
    )
    keys: set[str] = set()
    display_map: dict[str, str] = {}
    try:
        content = entries_path.read_text(encoding="utf-8", errors="ignore")
    except FileNotFoundError:
        return keys, display_map
    for key, display, _, _ in pattern.findall(content):
        key = key.strip()
        keys.add(key)
        for norm in normalize_variants(display):
            display_map[norm] = key
    return keys, display_map


def collect_usages(tex_files: list[Path], exclude_dirs: set[str]) -> tuple[set[str], list[tuple[str, int, str]], set[str]]:
    usage_pattern = re.compile(r"\\RBKTerm(?:\[([^\]]*)\])?\{([A-Za-z0-9_]+)\}")
    keys_used: set[str] = set()
    occurrences: list[tuple[str, int, str]] = []
    displays_used: set[str] = set()
    for path in tex_files:
        if any(part in exclude_dirs for part in path.parts):
            continue
        with path.open(encoding="utf-8", errors="ignore") as f:
            for lineno, line in enumerate(f, start=1):
                for display_opt, key in usage_pattern.findall(line):
                    keys_used.add(key)
                    occurrences.append((str(path), lineno, line.strip()))
                    if display_opt:
                        displays_used.add(display_opt.strip())
    return keys_used, occurrences, displays_used


def detect_unknown_keys(keys_used: set[str], keys_declared: set[str], occurrences: list[tuple[str, int, str]]):
    unknown = []
    for path, lineno, line in occurrences:
        for key in re.findall(r"\\RBKTerm(?:\[[^\]]*\])?\{([A-Za-z0-9_]+)\}", line):
            if key not in keys_declared:
                unknown.append((key, path, lineno, line.strip()))
    return unknown


# ------------------------------------------------------------
# Detection helpers
# ------------------------------------------------------------
def detect_acronyms(
    tex_files: list[Path],
    exclude_paths: set[Path],
    top_n: int,
    whitelist: set[str],
    covered_strings: set[str],
    include_covered: bool,
):
    acr_pattern = re.compile(r"\b([A-Z]{2,6}|[A-Z]{2,5}[0-9]{1,2})\b")
    ci_cd_pattern = re.compile(r"\bCI/CD\b")
    counts_uncovered = Counter()
    counts_covered = Counter()
    locations_uncovered: dict[str, list[tuple[str, int, str]]] = defaultdict(list)
    locations_covered: dict[str, list[tuple[str, int, str]]] = defaultdict(list)
    skip_line_markers = (
        "\\rowcolor{",
        "\\definecolor{",
        "\\pagecolor{",
        "\\textcolor{",
        "\\color{",
        "\\cellcolor{",
        "\\hypersetup{",
        "\\tikz",
        "\\pgf",
        "\\lstset{",
        "\\begin{lstlisting",
        "\\end{lstlisting",
        "\\chapter{",
        "\\section{",
        "\\subsection{",
        "\\subsubsection{",
        "\\paragraph{",
        "\\caption{",
    )
    for path in tex_files:
        if path in exclude_paths:
            continue
        if any(part in {"build", "out", "node_modules", "dist", "_minted-"} for part in path.parts):
            continue
        with path.open(encoding="utf-8", errors="ignore") as f:
            for lineno, line in enumerate(f, start=1):
                if line.lstrip().startswith("%"):
                    continue
                if any(marker in line for marker in skip_line_markers):
                    continue
                if "\\DeclareRBKTerm" in line or "\\newcommand" in line or "\\RBKTerm" in line:
                    continue
                scrubbed = re.sub(r"\\[A-Za-z@]+(\s|{)", " ", line)
                tokens = set(acr_pattern.findall(line))
                if ci_cd_pattern.search(line):
                    tokens.add("CI/CD")
                for token in tokens:
                    normed = normalize_token(token)
                    if normed in whitelist:
                        continue
                    if normed in {"go", "no", "ok"}:
                        continue
                    if re.match(r"^[a-z]{1,2}-\d{2,4}$", normed):
                        continue
                    if normed in covered_strings:
                        counts_covered[token] += 1
                        if include_covered and len(locations_covered[token]) < 3:
                            locations_covered[token].append((str(path), lineno, scrubbed.strip()))
                    else:
                        counts_uncovered[token] += 1
                        if len(locations_uncovered[token]) < 3:
                            locations_uncovered[token].append((str(path), lineno, scrubbed.strip()))
    top_uncovered = counts_uncovered.most_common(top_n)
    top_covered = counts_covered.most_common(top_n) if include_covered else []
    return counts_uncovered, locations_uncovered, top_uncovered, counts_covered, locations_covered, top_covered


def detect_tokens(
    tex_files: list[Path],
    exclude_paths: set[Path],
    top_n: int,
    covered_strings: set[str],
    include_covered: bool,
):
    camel = re.compile(r"\b([A-Z][a-z]+[A-Z][A-Za-z0-9]*)\b")
    slash = re.compile(r"\b([A-Za-z]{1,6}/[A-Za-z]{1,6})\b")
    hyphen = re.compile(r"\b([A-Za-z]+-[A-Za-z0-9-]+)\b")
    ignore_token_patterns = [
        re.compile(r"^Solana[A-Za-z]+$", re.IGNORECASE),
        re.compile(r".*!\d+$"),
        re.compile(r"^[0-9A-Fa-f]{6}$"),
        re.compile(r"^[A-Za-z]+Font$", re.IGNORECASE),
        re.compile(r"^HeadingFont(?:Light|Dark)?$", re.IGNORECASE),
        re.compile(r"^Inter$", re.IGNORECASE),
        re.compile(r"^SpaceGrotesk$", re.IGNORECASE),
        re.compile(r"^HoP$", re.IGNORECASE),
    ]
    skip_line_markers = (
        "\\rowcolor{",
        "\\definecolor{",
        "\\pagecolor{",
        "\\textcolor{",
        "\\color{",
        "\\cellcolor{",
        "\\hypersetup{",
        "\\tikz",
        "\\pgf",
        "\\lstset{",
        "\\begin{lstlisting",
        "\\end{lstlisting",
    )
    counts = Counter()
    counts_covered = Counter()
    locations: dict[str, list[tuple[str, int, str]]] = defaultdict(list)
    locations_covered: dict[str, list[tuple[str, int, str]]] = defaultdict(list)
    ssot_skip_tokens = {
        "programweeks",
        "programdurationtext",
        "isathresholdtnd",
        "isarate",
        "isacaptnd",
        "isamaxpaidmonths",
    }
    style_skip_tokens = {
        "headingfontlight",
        "headingfontdark",
        "basedark",
        "baselight",
        "toc",
        "matchlowercase",
        "brut/mois",
    }
    for path in tex_files:
        if path in exclude_paths:
            continue
        if any(part in {"build", "out", "node_modules", "dist", "_minted-"} for part in path.parts):
            continue
        with path.open(encoding="utf-8", errors="ignore") as f:
            for lineno, line in enumerate(f, start=1):
                if "http://" in line or "https://" in line:
                    continue
                if line.lstrip().startswith("%"):
                    continue
                if any(marker in line for marker in skip_line_markers):
                    continue
                if "\\DeclareRBKTerm" in line:
                    continue
                if any(mark in line for mark in ("\\chapter{", "\\section{", "\\subsection{", "\\subsubsection{", "\\paragraph{", "\\caption{")):
                    continue
                scrubbed = re.sub(r"\\[A-Za-z@]+(\s|{)", " ", line)
                line_tokens = set()
                line_tokens |= set(camel.findall(scrubbed))
                line_tokens |= set(slash.findall(scrubbed))
                line_tokens |= set(hyphen.findall(scrubbed))
                if "\\RBKTerm" in line:
                    continue
                for token in line_tokens:
                    if any(pat.match(token) for pat in ignore_token_patterns):
                        continue
                    normed = normalize_token(token)
                    if normed in ssot_skip_tokens or normed in style_skip_tokens:
                        continue
                    if normed.startswith("doc-") and normed.endswith("checks"):
                        continue
                    if re.match(r"^[a-z]{1,2}-\d{2,4}$", normed):
                        continue
                    if normed in {"go", "no", "ok"}:
                        continue
                    if normed in {"basedark", "baselight"} or re.match(r"^base[a-z]+$", normed):
                        continue
                    if "/" in normed:
                        parts = [p for p in normed.split("/") if p]
                        if parts and all(p in covered_strings for p in parts):
                            counts_covered[token] += 1
                            if include_covered and len(locations_covered[token]) < 3:
                                locations_covered[token].append((str(path), lineno, scrubbed.strip()))
                            continue
                    if normed in covered_strings:
                        counts_covered[token] += 1
                        if include_covered and len(locations_covered[token]) < 3:
                            locations_covered[token].append((str(path), lineno, scrubbed.strip()))
                        continue
                    counts[token] += 1
                    if len(locations[token]) < 3:
                        locations[token].append((str(path), lineno, scrubbed.strip()))
    top = counts.most_common(top_n)
    top_covered = counts_covered.most_common(top_n) if include_covered else []
    return counts, locations, top, counts_covered, locations_covered, top_covered


# ------------------------------------------------------------
# Report writer
# ------------------------------------------------------------
def write_report(
    output_path: Path,
    root: Path,
    keys_declared: set[str],
    keys_used: set[str],
    unknown_keys,
    declared_unused,
    acr_top,
    acr_locations,
    tok_top,
    tok_locations,
    acr_total: int,
    tok_total: int,
    acr_cov_top,
    acr_cov_locations,
    tok_cov_top,
    tok_cov_locations,
    include_covered: bool,
):
    output_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        commit = (
            subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], cwd=root)
            .decode("utf-8")
            .strip()
        )
    except Exception:
        commit = "N/A"
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = []
    lines.append("# Terminology Gaps Report")
    lines.append(f"_Generated: {now}_")
    lines.append(f"_Root: {root}_")
    lines.append(f"_Commit: {commit}_")
    lines.append(f"_Report version: {REPORT_VERSION}_")
    lines.append("")
    lines.append("## Résumé")
    lines.append(f"- Keys déclarées : {len(keys_declared)}")
    lines.append(f"- Keys utilisées : {len(keys_used)}")
    lines.append(f"- Unknown keys : {len(unknown_keys)}")
    lines.append(f"- Declared but unused : {len(declared_unused)}")
    lines.append(f"- Acronymes suspects non couverts (uniques) : {acr_total}")
    lines.append(f"- Tokens techniques suspects non couverts (uniques) : {tok_total}")
    lines.append("")

    lines.append("## A — UNKNOWN KEYS (critique)")
    if not unknown_keys:
        lines.append("_Aucune entrée._")
    else:
        for key, path, lineno, snippet in unknown_keys:
            lines.append(f"- `{key}` — {path}:{lineno} — `{snippet}`")
    lines.append("")

    lines.append("## B — DECLARED BUT UNUSED (warning)")
    if not declared_unused:
        lines.append("_Aucune entrée._")
    else:
        for key in sorted(declared_unused):
            lines.append(f"- `{key}`")
    lines.append("")

    lines.append("## C — Acronymes suspects NON COUVERTS (top)")
    if not acr_top:
        lines.append("_Aucun acronyme suspect._")
    else:
        for token, count in acr_top:
            locs = "; ".join(f"{p}:{ln}" for p, ln, _ in acr_locations.get(token, []))
            lines.append(f"- `{token}` — {count} occurrence(s) — {locs}")
    lines.append("")

    lines.append("## D — Tokens techniques suspects NON COUVERTS (top)")
    if not tok_top:
        lines.append("_Aucun token suspect._")
    else:
        for token, count in tok_top:
            locs = "; ".join(f"{p}:{ln}" for p, ln, _ in tok_locations.get(token, []))
            lines.append(f"- `{token}` — {count} occurrence(s) — {locs}")
    lines.append("")

    if include_covered:
        lines.append("## E — Acronymes déjà définis dans le lexique (pour info)")
        if not acr_cov_top:
            lines.append("_Aucun acronyme couvert._")
        else:
            for token, count in acr_cov_top:
                locs = "; ".join(f"{p}:{ln}" for p, ln, _ in acr_cov_locations.get(token, []))
                lines.append(f"- `{token}` — {count} occurrence(s) — {locs}")
        lines.append("")

        lines.append("## F — Tokens techniques déjà définis (pour info)")
        if not tok_cov_top:
            lines.append("_Aucun token couvert._")
        else:
            for token, count in tok_cov_top:
                locs = "; ".join(f"{p}:{ln}" for p, ln, _ in tok_cov_locations.get(token, []))
                lines.append(f"- `{token}` — {count} occurrence(s) — {locs}")
        lines.append("")

    lines.append("## Notes")
    lines.append("- Ignorés pour les suspects : terminology_entries.tex, terminology_core.tex, et dossiers build/out/node_modules/dist/_minted-*.")
    lines.append("- Réduire les faux positifs : ajouter \\\\RBKTerm{...} autour du terme ou l’ajouter au lexique.")
    output_path.write_text("\n".join(lines), encoding="utf-8")


# ------------------------------------------------------------
# Main
# ------------------------------------------------------------
def main():
    args = parse_args()
    root = Path(args.root).resolve()
    output_path = Path(args.output)

    exclude_dirs = {"build", "out", "node_modules", "dist", "_minted-"}
    tex_files = walk_tex_files(root, exclude_dirs)

    entries_path = root / "tex" / "terminology_entries.tex"
    keys_declared, display_map = load_declared_entries(entries_path)

    keys_used, usage_occurrences, displays_used = collect_usages(tex_files, exclude_dirs)
    unknown_keys = detect_unknown_keys(keys_used, keys_declared, usage_occurrences)
    declared_unused = keys_declared - keys_used

    def add_display_to_covered(d: str, target: set[str]):
        target.update(normalize_variants(d))
        if "/" in d:
            for part in d.split("/"):
                norm_part = normalize_token(part)
                if len(norm_part) > 1 and norm_part not in {"go", "no", "ok"}:
                    target.add(norm_part)

    covered_strings: set[str] = set(display_map.keys())
    for disp in displays_used:
        add_display_to_covered(disp, covered_strings)
    extra_variants = set()
    for s in list(covered_strings):
        if len(s) > 3 and not s.endswith("s"):
            extra_variants.add(s + "s")
    covered_strings.update(extra_variants)

    exclude_paths = {
        root / "tex" / "terminology_entries.tex",
        root / "tex" / "terminology_core.tex",
        root / "tex" / "params.tex",
    }
    whitelist_acr = {
        "ue",
        "tv",
        "pdf",
        "http",
        "https",
        "json",
        "csv",
        "xml",
        "sql",
        "cpu",
        "gpu",
        "ram",
        "www",
        "ide",
        "vm",
        "tls",
        "ssl",
    }

    acr_counts, acr_locations, acr_top, acr_cov_counts, acr_cov_locations, acr_cov_top = detect_acronyms(
        tex_files, exclude_paths, args.top, whitelist_acr, covered_strings, args.include_covered
    )
    tok_counts, tok_locations, tok_top, tok_cov_counts, tok_cov_locations, tok_cov_top = detect_tokens(
        tex_files, exclude_paths, args.top, covered_strings, args.include_covered
    )

    if args.debug_token:
        norm = normalize_token(args.debug_token)
        print(f"DEBUG TOKEN: raw='{args.debug_token}' norm='{norm}' covered={norm in covered_strings}")
        matched = []
        for disp_norm, key in display_map.items():
            if norm == disp_norm:
                matched.append(("declared_display", key, disp_norm))
            else:
                # plural variant match
                if norm.endswith("s") and norm[:-1] == disp_norm:
                    matched.append(("declared_display_plural", key, disp_norm))
        if matched:
            print("Matches:", "; ".join(f"{m[0]}->{m[1]} ({m[2]})" for m in matched))
        else:
            # check optional display usages
            for disp_norm in covered_strings:
                if norm == disp_norm:
                    print(f"Covered via optional display: {disp_norm}")
                    break
            else:
                print("No mapping found")
        return

    write_report(
        output_path,
        root,
        keys_declared,
        keys_used,
        unknown_keys,
        declared_unused,
        acr_top,
        acr_locations,
        tok_top,
        tok_locations,
        len(acr_counts),
        len(tok_counts),
        acr_cov_top,
        acr_cov_locations,
        tok_cov_top,
        tok_cov_locations,
        args.include_covered,
    )

    if args.strict:
        acr_threshold = 10
        tok_threshold = 20
        if unknown_keys or len(acr_counts) > acr_threshold or len(tok_counts) > tok_threshold:
            raise SystemExit(1)


if __name__ == "__main__":
    main()
