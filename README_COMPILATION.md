# Instructions de Compilation - Livre Blanc RBK v3.0

Ce document est configuré pour être compilé avec le moteur **XeLaTeX** afin de supporter les polices modernes et les caractères Unicode.

## Prérequis
- Distribution TeX Live 2023 ou supérieure.
- Packages requis : `fontspec`, `tikz`, `pgfplots`, `tcolorbox`, `fontawesome5`, `listings`, `pgfgantt`, `pdflscape`.
- Polices système : **Inter** (doit être installée sur le système).

## Commande de Compilation
Exécutez la commande suivante dans votre terminal :

```bash
xelatex -interaction=nonstopmode Livre_blanc_v3.tex
```

Répétez la commande 2 fois pour assurer la génération correcte de la table des matières et des références croisées.

## Notes
- Le document utilise la police **Inter** par défaut.
- Les couleurs sont définies selon la charte Solana (SolanaGreen, SolanaPurple, SolanaBlue).
- En cas d'erreur de compilation liée aux polices, assurez-vous que `fonts-inter` est installé (`sudo apt install fonts-inter`).
