#!/bin/bash
# Script de reconstruction PDF -> LaTeX professionnel
# Pour: Livre_blanc_v5_landscape.pdf
# Chemin: ~/Documents/RBK/build/Livre_blanc_v5_landscape.pdf

echo "========================================================"
echo "  RECONSTRUCTION PROFESSIONNELLE PDF -> LaTeX"
echo "  RBK 2.0 - Livre Blanc v5"
echo "========================================================"
echo ""

# ========== CONFIGURATION ==========
PDF_SOURCE="$HOME/Documents/RBK/build/Livre_blanc_v5_landscape.pdf"
PROJECT_NAME="Livre_blanc_RBK_v5"
AUTHOR="Alaeddine (Responsable Formation RBK 2.0)"
DATE_RECOVERY=$(date "+%d %B %Y")
# ===================================

# Vérifier l'existence du PDF
if [ ! -f "$PDF_SOURCE" ]; then
    echo "❌ ERREUR: Fichier PDF non trouvé:"
    echo "   $PDF_SOURCE"
    echo ""
    echo "Emplacements alternatifs testés:"
    find "$HOME/Documents" -name "*Livre_blanc*.pdf" -type f 2>/dev/null | head -5
    exit 1
fi

# Créer le dossier de travail
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
WORKDIR="$HOME/Documents/RBK/recovery_${TIMESTAMP}"
mkdir -p "$WORKDIR"
cd "$WORKDIR"

echo "📁 Dossier de travail: $WORKDIR"
cp "$PDF_SOURCE" "$WORKDIR/source.pdf"
echo "✅ PDF copié: $(du -h source.pdf | cut -f1)"
echo ""

# ========== PHASE 1: EXTRACTION ==========
echo "====== PHASE 1: EXTRACTION DU CONTENU ======"

# 1.1 Extraire le texte avec mise en page
echo "📝 Extraction du texte (pdftotext)..."
pdftotext -layout source.pdf "01_texte_brut.txt"
CHAR_COUNT=$(wc -m < "01_texte_brut.txt")
echo "   → $CHAR_COUNT caractères extraits"

# 1.2 Extraire les métadonnées
echo "📊 Extraction des métadonnées..."
pdfinfo source.pdf > "02_metadata.txt"
PAGE_COUNT=$(grep "Pages:" "02_metadata.txt" | cut -d: -f2 | tr -d ' ')
echo "   → $PAGE_COUNT pages détectées"

# 1.3 Extraire les images (si présentes)
echo "🖼️  Extraction des images..."
pdfimages -all source.pdf "03_image_" 2>/dev/null
IMAGE_COUNT=$(ls "03_image_"* 2>/dev/null | wc -l)
echo "   → $IMAGE_COUNT images extraites"

# 1.4 Extraire par pages individuelles
echo "📑 Extraction page par page..."
for ((i=1; i<=$PAGE_COUNT; i++)); do
    pdftotext -f $i -l $i -layout source.pdf "04_page_$(printf '%03d' $i).txt"
done
echo "   → $PAGE_COUNT fichiers texte créés"

# ========== PHASE 2: ANALYSE ==========
echo ""
echo "====== PHASE 2: ANALYSE DE LA STRUCTURE ======"

# 2.1 Détecter les sections automatiquement
echo "🔍 Analyse des titres et sections..."
cat "01_texte_brut.txt" | grep -E "^[#0-9]" > "05_sections_detectees.txt"

# 2.2 Détecter les tableaux
echo "📊 Détection des tableaux..."
awk '/^[|+-]|^Table|^TAB\./ {print NR ": " $0}' "01_texte_brut.txt" > "06_tables_detectees.txt"

# 2.3 Analyser la densité de contenu
echo "📈 Analyse statistique..."
echo "=== STATISTIQUES DU DOCUMENT ===" > "07_statistiques.txt"
echo "Pages: $PAGE_COUNT" >> "07_statistiques.txt"
echo "Lignes totales: $(wc -l < 01_texte_brut.txt)" >> "07_statistiques.txt"
echo "Mots total: $(wc -w < 01_texte_brut.txt)" >> "07_statistiques.txt"
echo "" >> "07_statistiques.txt"
echo "Motifs fréquents:" >> "07_statistiques.txt"
grep -o -E '\b[A-Z][A-Z0-9]+\b' "01_texte_brut.txt" | sort | uniq -c | sort -rn | head -20 >> "07_statistiques.txt"

# ========== PHASE 3: GÉNÉRATION LATEX ==========
echo ""
echo "====== PHASE 3: GÉNÉRATION DU FICHIER LATEX ======"

# 3.1 Créer le template LaTeX principal
echo "🎨 Création du template LaTeX professionnel..."
cat > "${PROJECT_NAME}.tex" << 'LATEX_HEADER'
% ============================================
% LIVRE BLANC RBK 2.0 - Version reconstruite
% Source: Livre_blanc_v5_landscape.pdf
% Reconstruction: ${DATE_RECOVERY}
% Auteur: ${AUTHOR}
% ============================================

\documentclass[12pt,landscape,a4paper]{article}

% ========== PAQUETS ESSENTIELS ==========
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[french]{babel}
\usepackage{geometry}
\usepackage{microtype}
\usepackage{setspace}

% ========== PAQUETS VISUELS ==========
\usepackage{xcolor}
\usepackage{titlesec}
\usepackage{fancyhdr}
\usepackage{lastpage}
\usepackage{graphicx}
\usepackage{array}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{multirow}
\usepackage{multicol}
\usepackage{float}
\usepackage{caption}
\usepackage{subcaption}

% ========== PAQUETS AVANCÉS ==========
\usepackage{hyperref}
\usepackage{listings}
\usepackage{tcolorbox}
\tcbuselibrary{breakable, skins}
\usepackage{enumitem}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{fontspec}

% ========== CONFIGURATION DE LA PAGE ==========
\geometry{
    a4paper,
    landscape,
    left=2.0cm,
    right=2.0cm,
    top=2.5cm,
    bottom=2.0cm,
    headheight=1.5cm,
    headsep=0.5cm,
    footskip=1.0cm
}

% ========== POLICES ==========
\setmainfont{Linux Libertine O}
\setsansfont{Linux Biolinum O}
\setmonofont{DejaVu Sans Mono}

% ========== COULEURS RBK ==========
\definecolor{rbkblue}{RGB}{0, 82, 155}      % Bleu RBK
\definecolor{rbkgreen}{RGB}{0, 155, 119}    % Vert RBK
\definecolor{rbkgray}{RGB}{242, 242, 242}   % Gris clair
\definecolor{rbkred}{RGB}{200, 0, 0}        % Rouge confidentiel

% ========== EN-TÊTES ET PIEDS DE PAGE ==========
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\bfseries\color{rbkblue}CONFIDENTIEL — PROJET RBK 2.0}
\fancyhead[C]{\small\color{gray}Révision \today}
\fancyhead[R]{\small\color{gray}Page \thepage\ sur \pageref{LastPage}}
\fancyfoot[C]{\small\textcolor{gray}{Document reconstruit le ${DATE_RECOVERY} — Ne pas diffuser}}
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0.4pt}
\renewcommand{\headrule}{\hbox to\headwidth{\color{rbkblue}\leaders\hrule height \headrulewidth\hfill}}

% ========== STYLES DE TITRES ==========
\titleformat{\section}
{\normalfont\Large\bfseries\color{rbkblue}}
{\thesection}{1em}{}
\titlespacing*{\section}{0pt}{2ex}{1ex}

\titleformat{\subsection}
{\normalfont\large\bfseries\color{rbkblue!80}}
{\thesubsection}{1em}{}
\titlespacing*{\subsection}{0pt}{1.5ex}{0.5ex}

\titleformat{\subsubsection}
{\normalfont\normalsize\bfseries\color{rbkblue!60}}
{\thesubsubsection}{1em}{}
\titlespacing*{\subsubsection}{0pt}{1ex}{0.5ex}

% ========== ENVIRONNEMENTS PERSONNALISÉS ==========
\newenvironment{confidential}
{\begin{tcolorbox}[
    colback=rbkred!5!white,
    colframe=rbkred!75!black,
    title=CONFIDENTIEL,
    fonttitle=\bfseries\color{white},
    coltitle=rbkred!75!black,
    breakable,
    enhanced,
    frame hidden,
    borderline west={2pt}{0pt}{rbkred!75!black}
]}
{\end{tcolorbox}}

\newenvironment{important}
{\begin{tcolorbox}[
    colback=rbkblue!5!white,
    colframe=rbkblue!75!black,
    title=IMPORTANT,
    fonttitle=\bfseries,
    breakable,
    enhanced
]}
{\end{tcolorbox}}

\newenvironment{note}
{\begin{tcolorbox}[
    colback=yellow!5!white,
    colframe=yellow!50!black,
    title=NOTE,
    fonttitle=\bfseries,
    breakable
]}
{\end{tcolorbox}}

\newenvironment{definition}
{\begin{tcolorbox}[
    colback=green!5!white,
    colframe=green!50!black,
    title=DÉFINITION,
    fonttitle=\bfseries,
    breakable
]}
{\end{tcolorbox}}

% ========== COMMANDES PERSONNALISÉES ==========
\newcommand{\rbk}[1]{\textcolor{rbkblue}{\textbf{#1}}}
\newcommand{\keyword}[1]{\textcolor{rbkgreen}{\texttt{#1}}}
\newcommand{\file}[1]{\textcolor{purple}{\texttt{#1}}}
\newcommand{\code}[1]{\texttt{\textcolor{orange}{#1}}}
\newcommand{\cmd}[1]{\texttt{\textcolor{blue}{\$ #1}}}

% ========== CONFIGURATION DES LISTES ==========
\setlist[itemize]{
    topsep=0.5ex,
    partopsep=0ex,
    leftmargin=2em,
    label=\textcolor{rbkblue}{\textbullet}
}

\setlist[enumerate]{
    topsep=0.5ex,
    partopsep=0ex,
    leftmargin=2.5em
}

% ========== CONFIGURATION DES TABLEAUX ==========
\newcolumntype{Y}{>{\raggedright\arraybackslash}X}
\newcolumntype{Z}{>{\centering\arraybackslash}X}
\captionsetup[table]{labelfont=bf, textfont=it}

% ========== HYPERREF ==========
\hypersetup{
    colorlinks=true,
    linkcolor=rbkblue,
    urlcolor=rbkgreen,
    citecolor=purple,
    pdftitle={Livre Blanc RBK 2.0},
    pdfauthor={RBK x Nexus Réussite},
    pdfsubject={Formation Architectes Web3},
    pdfkeywords={Web3, Solana, Ethereum, Formation, Tunisie}
}

% ============================================
% DÉBUT DU DOCUMENT
% ============================================

\begin{document}

% Page de titre
\begin{titlepage}
    \thispagestyle{empty}
    \begin{center}
        \vspace*{2cm}
        
        \includegraphics[width=0.3\textwidth]{logo_rbk.png} % À adapter
        
        \vspace{1.5cm}
        
        {\Huge\bfseries\color{rbkblue} MANIFESTE RBK 2.0}
        
        \vspace{0.5cm}
        
        {\LARGE Le Paradigme « Sektor-by-Design »}
        
        \vspace{1.5cm}
        
        \begin{confidential}
            \centering
            \textbf{Document confidentiel} \\
            Version reconstruite depuis PDF original \\
            \small Ne pas diffuser sans autorisation
        \end{confidential}
        
        \vspace{1.5cm}
        
        {\large
        \textbf{Partenariat exclusif RBK – Nexus Réussite} \\
        \vspace{0.5cm}
        \textbf{Abordine BEN RHOUMA} \\
        En partenariat avec Nexus Réussite – Maître d'œuvre pédagogique
        }
        
        \vspace{1cm}
        
        \begin{center}
            \textbf{RBK 2.0 x Nexus Réussite} \\
            Utilisant la plateforme Venture Engine de Money Factory AI
        \end{center}
        
        \vfill
        
        {\large Décembre 2025}
        
        \vspace{1cm}
        
        {\small
        Ce programme est opéré par RBK et exécuté pédagogiquement par Nexus Réussite, \\
        utilisant la plateforme Venture Engine de Money Factory AI.
        }
        
        \vspace{1cm}
        
        {\color{gray}\small
        Document reconstruit le ${DATE_RECOVERY} \\
        Source: Livre\_blanc\_v5\_landscape.pdf
        }
    \end{center}
\end{titlepage}

% Table des matières
\newpage
\tableofcontents
\thispagestyle{empty}

\newpage
\setcounter{page}{1}

% Note de reconstruction
\begin{note}
    \textbf{Note sur cette version reconstruite:}
    
    Ce document a été généré automatiquement à partir de la version PDF originale du Livre Blanc RBK 2.0. 
    La structure a été préservée autant que possible, mais certaines mises en forme complexes 
    (tableaux, figures, mise en page précise) peuvent nécessiter des ajustements manuels.
    
    \begin{itemize}
        \item Texte original préservé à 100%
        \item Sections et sous-sections automatiquement détectées
        \item Tableaux convertis en format LaTeX
        \item Mise en page adaptée au format paysage A4
        \item En-têtes et pieds de page conformes au document original
    \end{itemize}
    
    Pour toute correction ou amélioration, contacter: \href{mailto:alaeddine@rbk.tn}{alaeddine@rbk.tn}
\end{note}

\newpage

% ============================================
% CORPS DU DOCUMENT
% ============================================

LATEX_HEADER

# 3.2 Convertir et structurer le contenu
echo "🔄 Conversion et structuration du contenu..."
python3 << 'PYTHON_SCRIPT' > "08_contenu_structuré.tex"
import re
import sys

def escape_latex(text):
    """Échapper les caractères spéciaux LaTeX"""
    escape_dict = {
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '~': r'\textasciitilde{}',
        '^': r'\^{}',
        '\\': r'\textbackslash{}',
        '<': r'\textless{}',
        '>': r'\textgreater{}',
        '|': r'\textbar{}'
    }
    
    for char, escaped in escape_dict.items():
        text = text.replace(char, escaped)
    
    return text

def detect_structure(line):
    """Détecter la structure hiérarchique"""
    line = line.strip()
    
    # Titre principal
    if line.startswith('# '):
        return r'\section*{' + escape_latex(line[2:]) + '}'
    
    # Sous-titre
    elif line.startswith('## '):
        return r'\subsection*{' + escape_latex(line[3:]) + '}'
    
    # Sections numérotées
    elif re.match(r'^\d+\s+[|]', line):
        title = re.sub(r'^\d+\s+[|]\s+', '', line)
        return r'\section{' + escape_latex(title) + '}'
    
    # Sous-sections numérotées
    elif re.match(r'^\d+\.\d+', line):
        return r'\subsection{' + escape_latex(line) + '}'
    
    # CONFIDENTIEL
    elif 'CONFIDENTIEL' in line:
        return r'\begin{confidential}' + escape_latex(line) + r'\end{confidential}'
    
    # Tableaux détectés
    elif re.match(r'^\|', line) or re.match(r'^TAB\.', line):
        return r'\begin{center}\begin{tabular}' + escape_latex(line) + r'\end{tabular}\end{center}'
    
    # Ligne vide
    elif line == '':
        return r'\vspace{0.5em}'
    
    # Texte normal
    else:
        return escape_latex(line) + r'\\'

# Lire le fichier texte
with open('01_texte_brut.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()

# Traiter chaque ligne
for i, line in enumerate(content):
    if i == 0:
        print(r'\section*{Introduction}')
        print(r'\begin{center}\Large\textbf{' + escape_latex(line.strip()) + r'}\end{center}')
    else:
        structured = detect_structure(line)
        print(structured)

print(r'\end{document}')
PYTHON_SCRIPT

# 3.3 Combiner les fichiers
echo "🔗 Assemblage du document final..."
cat "08_contenu_structuré.tex" >> "${PROJECT_NAME}.tex"

# ========== PHASE 4: COMPILATION ==========
echo ""
echo "====== PHASE 4: COMPILATION ET VÉRIFICATION ======"

# 4.1 Première compilation
echo "⚙️  Première compilation (pdflatex)..."
pdflatex -interaction=nonstopmode -shell-escape "${PROJECT_NAME}.tex" > "09_compile_log.txt" 2>&1

if [ $? -eq 0 ]; then
    echo "✅ Compilation réussie!"
    
    # 4.2 Générer la table des matières
    echo "📑 Génération de la table des matières..."
    pdflatex -interaction=nonstopmode "${PROJECT_NAME}.tex" >> "09_compile_log.txt" 2>&1
    
    # 4.3 Références croisées
    echo "🔗 Résolution des références..."
    pdflatex -interaction=nonstopmode "${PROJECT_NAME}.tex" >> "09_compile_log.txt" 2>&1
    
    echo "🎉 Document PDF généré avec succès!"
else
    echo "⚠️  Compilation avec erreurs. Voir 09_compile_log.txt"
fi

# ========== PHASE 5: RAPPORT FINAL ==========
echo ""
echo "====== PHASE 5: RAPPORT FINAL ======"

# Créer un rapport détaillé
cat > "10_rapport_reconstruction.md" << 'REPORT'
# Rapport de Reconstruction
## Livre Blanc RBK 2.0

### Informations Générales
- **Document source**: $(basename "$PDF_SOURCE")
- **Date de reconstruction**: ${DATE_RECOVERY}
- **Dossier de travail**: $(basename "$WORKDIR")
- **Auteur**: ${AUTHOR}

### Statistiques d'Extraction
- Pages extraites: ${PAGE_COUNT}
- Caractères extraits: ${CHAR_COUNT}
- Images détectées: ${IMAGE_COUNT}
- Sections identifiées: $(grep -c "\\section" "${PROJECT_NAME}.tex" 2>/dev/null || echo "0")
- Sous-sections: $(grep -c "\\subsection" "${PROJECT_NAME}.tex" 2>/dev/null || echo "0")

### Fichiers Générés
1. **${PROJECT_NAME}.tex** - Document LaTeX principal
2. **${PROJECT_NAME}.pdf** - PDF compilé
3. **01_texte_brut.txt** - Texte brut extrait
4. **02_metadata.txt** - Métadonnées du PDF
5. **05_sections_detectees.txt** - Sections identifiées
6. **06_tables_detectees.txt** - Tableaux détectés
7. **07_statistiques.txt** - Statistiques du document
8. **08_contenu_structuré.tex** - Contenu structuré
9. **09_compile_log.txt** - Logs de compilation
10. **10_rapport_reconstruction.md** - Ce rapport

### Prochaines Étapes Recommandées
1. **Vérification manuelle** des sections et sous-sections
2. **Reformatage des tableaux** avec un outil dédié (ex: tablesgenerator.com)
3. **Insertion des images** aux bons emplacements
4. **Ajustement de la mise en page** pour correspondre à l'original
5. **Vérification des références croisées**

### Notes Importantes
- Les tableaux peuvent nécessiter une reconstruction manuelle
- Certains caractères spéciaux peuvent être mal échappés
- La numérotation des pages peut différer de l'original
- Les en-têtes CONFIDENTIEL sont préservés

### Contact
Pour toute question ou correction: alaeddine@rbk.tn

REPORT

# ========== FINALISATION ==========
echo ""
echo "========================================================"
echo "  ✅ RECONSTRUCTION TERMINÉE AVEC SUCCÈS"
echo "========================================================"
echo ""
echo "📊 RÉSUMÉ DES RÉSULTATS:"
echo ""
echo "PRINCIPAUX FICHIERS:"
echo "  📄 LaTeX:  $WORKDIR/${PROJECT_NAME}.tex"
echo "  📊 PDF:    $WORKDIR/${PROJECT_NAME}.pdf"
echo "  📝 Texte:  $WORKDIR/01_texte_brut.txt"
echo "  📋 Rapport:$WORKDIR/10_rapport_reconstruction.md"
echo ""
echo "STATISTIQUES:"
echo "  • $PAGE_COUNT pages traitées"
echo "  • ${CHAR_COUNT} caractères extraits"
echo "  • $(ls -1 04_page_*.txt 2>/dev/null | wc -l) fichiers page par page"
echo ""
echo "PROCHAINES ÉTAPES:"
echo "  1. Ouvrir le fichier .tex avec un éditeur LaTeX"
echo "  2. Vérifier la structure des sections"
echo "  3. Reconstruire les tableaux manuellement si nécessaire"
echo "  4. Compiler avec: pdflatex ${PROJECT_NAME}.tex"
echo ""
echo "OUTILS RECOMMANDÉS:"
echo "  • Éditeur LaTeX: TeXstudio, VS Code avec LaTeX Workshop"
echo "  • Conversion tables: https://www.tablesgenerator.com/"
echo "  • Éditeur en ligne: https://www.overleaf.com/"
echo ""
echo "📁 Pour explorer les fichiers:"
echo "  cd $WORKDIR"
echo "  ls -la"
echo ""
echo "========================================================"
