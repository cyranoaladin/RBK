import os

input_file = '/home/alaeddine/Documents/RBK/Livre_blanc_v4.tex'
output_file = '/home/alaeddine/Documents/RBK/Livre_blanc_v5.tex'

with open(input_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
packages_inserted = False
macros_inserted = False
note_cadrage_inserted = False
gabarits_inserted = False

packages_block = r"""
% --- Added for V5 (Strategic Tools) ---
\usepackage{xparse}
\usepackage{colortbl}
\usepackage{pifont}
\usepackage{adjustbox}
\usepackage{ragged2e}
\usepackage{fmtcount}
% \usepackage{hyperref} % Already present
\usepackage{cleveref}
"""

macros_block = r"""
% ============================================================
%  OUTILS STRATÉGIQUES — GABARITS TABLEAUX (SWOT / MoSCoW / RACI / RISQUES / KPI)
% ============================================================

% Colonnes tabularx
\newcolumntype{Y}{>{\RaggedRight\arraybackslash}X}
% \newcolumntype{C}{>{\centering\arraybackslash}m{1.25cm}} % Already defined as X centering in v4 preamble?
% Checking v4 preamble: \newcolumntype{C}{>{\centering\arraybackslash}X}. 
% We need a specific fixed width centering for RACI small columns probably, or stick to X but make sure table fits.
% The prompt requested: \newcolumntype{C}{>{\centering\arraybackslash}m{1.25cm}}
% I will redefine it locally or use a new name to avoid conflict if C is used elsewhere.
% Actually v4 uses C as X centering. I should use a different letter or overwrite if I'm sure.
% Let's use Z for the small fixed width column to be safe, or just use the prompt's definition but renamed to avoid conflict with 'C'.
\newcolumntype{Z}{>{\centering\arraybackslash}m{1.25cm}} 

% Petits marqueurs RACI
\newcommand{\raciR}{\textbf{\color{SolanaPurple}R}}
\newcommand{\raciA}{\textbf{\color{SolanaGreen!60!black}A}}
\newcommand{\raciC}{\textbf{\color{SolanaBlue!70!black}C}}
\newcommand{\raciI}{\textbf{\color{BaseDark}I}}

% Boîte générique “tableau stratégique”
\newtcolorbox{tableBox}[2]{
  enhanced, breakable,
  colback=#2!4, colframe=#2!70!black,
  boxrule=0.6pt, arc=2mm,
  title={\HeadingFont\bfseries #1},
  coltitle=DeepBlack,
  colbacktitle=#2!12,
  drop shadow
}

% ---------- SWOT ----------
\NewDocumentEnvironment{SWOTMatrix}{O{Matrice SWOT}}{
  \begin{tableBox}{#1}{SolanaPurple}
  \renewcommand{\arraystretch}{1.25}
  \begin{tabularx}{\textwidth}{|Y|Y|}
  \hline
  \rowcolor{SolanaGreen!10}\textbf{Forces} & \textbf{Faiblesses}\ \hline
}{
  \end{tabularx}
  \end{tableBox}
}

% ---------- MoSCoW ----------
\NewDocumentEnvironment{MoSCoWTable}{O{Priorisation MoSCoW}}{
  \begin{tableBox}{#1}{SolanaGreen}
  \renewcommand{\arraystretch}{1.25}
  \begin{tabularx}{\textwidth}{|Y|Y|Y|Y|}
  \hline
  \rowcolor{SolanaGreen!12}\textbf{Must have} &
  \textbf{Should have} &
  \textbf{Could have} &
  \textbf{Won't have (for now)}\ \hline
}{
  \end{tabularx}
  \end{tableBox}
}

% ---------- RACI ----------
\NewDocumentEnvironment{RACITable}{O{Matrice RACI} m}{
  % #2 = spécification des colonnes tabularx, ex: {|Y|Z|Z|Z|Z|} (using Z instead of C)
  \begin{tableBox}{#1}{SolanaBlue}
  \renewcommand{\arraystretch}{1.25}
  \begin{tabularx}{\textwidth}{#2}
}{
  \end{tabularx}
  \end{tableBox}
}

% ---------- Registre des risques ----------
\NewDocumentEnvironment{RiskRegister}{O{Registre des risques}}{
  \begin{tableBox}{#1}{SolanaPurple}
  \renewcommand{\arraystretch}{1.25}
  \begin{tabularx}{\textwidth}{|Y|c|c|Y|Y|}
  \hline
  \rowcolor{SolanaPurple!10}\textbf{Risque} & \textbf{P} & \textbf{I} & \textbf{Mesures} & \textbf{Owner}\ \hline
}{
  \end{tabularx}
  \end{tableBox}
}

% ---------- KPI / ROI ----------
\NewDocumentEnvironment{KPITable}{O{KPI \& ROI}}{
  \begin{tableBox}{#1}{SolanaGreen}
  \renewcommand{\arraystretch}{1.25}
  \begin{tabularx}{\textwidth}{|Y|Y|Y|Y|}
  \hline
  \rowcolor{SolanaGreen!12}\textbf{Indicateur} & \textbf{Définition} & \textbf{Cible} & \textbf{Mesure / Source}\ \hline
}{
  \end{tabularx}
  \end{tableBox}
}
"""

for line in lines:
    # 1. Insert Packages
    if not packages_inserted and "Packages généraux" in line:
        new_lines.append(line)
        new_lines.append(packages_block)
        packages_inserted = True
        continue
    
    # 2. Insert Macros after roadmapBox
    if not macros_inserted and "newtcolorbox{roadmapBox}" in line:
        # We need to find the end of this block. It usually spans a few lines.
        # But inserting after the closure is safer.
        # Let's look for "En-têtes/Pieds" which comes after boxes in v4
        pass 
    if not macros_inserted and "% En-têtes/Pieds" in line:
       new_lines.append(macros_block)
       macros_inserted = True
       new_lines.append(line)
       continue

    # 3. Insert Note de Cadrage
    if not note_cadrage_inserted and "input{chapters/01_vision.tex}" in line:
        new_lines.append(line)
        new_lines.append(r"\input{chapters/01a_note_cadrage.tex}" + "\n")
        note_cadrage_inserted = True
        continue
        
    # 4. Insert Gabarits Appendix
    if not gabarits_inserted and "\appendix" in line:
        new_lines.append(line)
        new_lines.append(r"\input{chapters/annexe_z_gabarits.tex}" + "\n")
        gabarits_inserted = True
        continue

    new_lines.append(line)

with open(output_file, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Created Livre_blanc_v5.tex")
