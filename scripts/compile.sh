#!/bin/bash
# Script de compilation avancée

set -e  # Stop on error

DOCUMENT="Livre_blanc_v3.tex"
OUTPUT_DIR="./build"
LOG_FILE="$OUTPUT_DIR/compile.log"

echo "🚀 Démarrage de la compilation RBK 2.0..."
echo "========================================"

# Création du dossier build si inexistant
mkdir -p $OUTPUT_DIR

# Nettoyage initial
echo "🧹 Nettoyage des anciens fichiers..."
latexmk -c -outdir=$OUTPUT_DIR

# Compilation avec XeLaTeX
echo "🔄 Compilation avec XeLaTeX..."
# Removed -output-directory here because most latexmk setups handle this, but explicit xelatex requires it.
# The user's script uses explicit xelatex.
if xelatex -synctex=1 -interaction=nonstopmode -file-line-error \
    -shell-escape -output-directory=$OUTPUT_DIR $DOCUMENT > $LOG_FILE 2>&1; then
    echo "✅ Première compilation réussie"
else
    echo "❌ Erreur lors de la première compilation"
    tail -20 $LOG_FILE
    exit 1
fi

# Compilation des bibliographies si nécessaire
if [ -f "references.bib" ]; then
    echo "📚 Compilation de la bibliographie..."
    biber --output-directory=$OUTPUT_DIR $(basename $DOCUMENT .tex) >> $LOG_FILE 2>&1
fi

# Deuxième compilation
echo "🔄 Deuxième compilation..."
xelatex -synctex=1 -interaction=nonstopmode -file-line-error \
    -shell-escape -output-directory=$OUTPUT_DIR $DOCUMENT >> $LOG_FILE 2>&1

# Troisième compilation (pour les références)
echo "🔄 Troisième compilation (références finales)..."
xelatex -synctex=1 -interaction=nonstopmode -file-line-error \
    -shell-escape -output-directory=$OUTPUT_DIR $DOCUMENT >> $LOG_FILE 2>&1

echo "✅ Compilation terminée avec succès!"
echo "📄 PDF disponible dans: $OUTPUT_DIR/$(basename $DOCUMENT .tex).pdf"

# Vérification du fichier PDF
if [ -f "$OUTPUT_DIR/$(basename $DOCUMENT .tex).pdf" ]; then
    PDF_SIZE=$(stat -c%s "$OUTPUT_DIR/$(basename $DOCUMENT .tex).pdf")
    echo "📏 Taille du PDF: $(($PDF_SIZE / 1024 / 1024)) MB"
    
    # Ouverture automatique
    if command -v evince &> /dev/null; then
        evince "$OUTPUT_DIR/$(basename $DOCUMENT .tex).pdf" &
    elif command -v okular &> /dev/null; then
        okular "$OUTPUT_DIR/$(basename $DOCUMENT .tex).pdf" &
    fi
fi

echo "========================================"
echo "✨ Compilation RBK 2.0 terminée avec succès!"
