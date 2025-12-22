# RBK 2.0 Whitepaper - Technical Documentation

## Overview
This repository contains the LaTeX source code for the "RBK 2.0 - L'Architecture de la Souveraineté Numérique" whitepaper. The project is structured for modularity and ease of maintenance.

## Compilation
This project **MUST** be compiled with **XeLaTeX** (or LuaLaTeX) to support the custom fonts and Unicode characters. Classic `pdflatex` will not work.

### Recommended Command
```bash
latexmk -pdfxe -interaction=nonstopmode -output-directory=output main.tex
# OR
xelatex -interaction=nonstopmode main.tex
```

### Dependencies
- **TeX Live** (Full distribution recommended)
- **Fonts**:
    - `Fira Code` (Monospace)
    - `DejaVu Sans Mono` (Fallback)
    - `Latin Modern Math`
- **LaTeX Packages**:
    - `fontspec` (System fonts)
    - `fontawesome5` (Icons)
    - `tcolorbox` (Boxes)
    - `tikz` (Diagrams)
    - `xcolor` (Colors)
    - `geometry`, `fancyhdr`, `tocloft` (Layout)

## Directory Structure
- `main.tex`: Master file.
- `chapters/`: Content chapters and annexes.
    - `11b_fiches_metiers.tex`: Renamed from `10_fiches_metiers.tex` to maintain correct ordering.
- `images/`: Graphics and figures.
- `separates/`: Standalone documents (Tracks, Capstones) that share the same style but can be compiled individually.
- `styles/`: Custom package definitions (`rbk.sty`).
- `templates/`: Reusable layouts (tables, title pages).

## Recent Fixes
- **Colors**: Standardized on `SolanaPurple` (removed `SOLANAPURPLE` alias).
- **Macros**: Renamed `\faPreselectedIcon` to `\rbkIcon` to prevent package conflicts.
- **Naming**: `10_fiches_metiers.tex` -> `11b_fiches_metiers.tex`.

## Troubleshooting
- **"Font not found"**: Install Fira Code or switch `\IfFontExistsTF` logic in `main.tex`.
- **"Undefined control sequence \rbkIcon"**: Ensure `main.tex` (or the separate file preamble) defines the macro.
