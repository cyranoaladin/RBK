#!/usr/bin/env python3
# Vérification des dépendances LaTeX

import subprocess
import sys

REQUIRED_PACKAGES = [
    "fontspec",
    "polyglossia",
    "microtype",
    "unicode-math",
    "xcolor",
    "geometry",
    "graphicx",
    "amsmath",
    "amssymb",
    "amsthm",
    "enumitem",
    "array",
    "booktabs",
    "tabularx",
    "tikz",
    "titlesec",
    "tcolorbox",
    "fontawesome5",
    "draftwatermark",
    "fancyhdr",
    "etoolbox",
    "hyperref",
    "pgfplots",
    "listings",
    "float",
    "rotating",
    "multicol",
    "multirow",
    "makecell",
    "longtable",
    "wrapfig",
    "pdflscape"
]

def check_package(package):
    """Vérifie si un package LaTeX est installé."""
    try:
        result = subprocess.run(
            ["kpsewhich", f"{package}.sty"],
            capture_output=True,
            text=True
        )
        return result.returncode == 0
    except FileNotFoundError:
        return False

def main():
    print("🔍 Vérification des packages LaTeX requis...")
    print("=" * 50)
    
    missing = []
    for package in REQUIRED_PACKAGES:
        if check_package(package):
            print(f"✅ {package}")
        else:
            print(f"❌ {package} - MANQUANT")
            missing.append(package)
    
    print("=" * 50)
    
    if missing:
        print(f"\\n⚠️  {len(missing)} packages manquants:")
        for package in missing:
            print(f"   - {package}")
        
        print("\\n📦 Installation recommandée:")
        print("   sudo apt-get install texlive-latex-extra texlive-science")
        print("   sudo apt-get install texlive-fonts-extra texlive-pictures")
        print("   sudo apt-get install texlive-lang-french")
        
        return 1
    else:
        print("✨ Tous les packages sont installés!")
        return 0

if __name__ == "__main__":
    sys.exit(main())
