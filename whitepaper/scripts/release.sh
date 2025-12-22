#!/usr/bin/env bash
set -euo pipefail

# Usage: ./whitepaper/scripts/release.sh 4.0.0 "Scale & Impact" "2026-01"
VERSION=${1:?"Version (ex: 4.0.0) requise"}
LABEL=${2:-}
DATE=${3:-$(date +%Y-%m-%d)}

# 1) Générer la version
cat > whitepaper/src/version.tex <<EOF
{\large \color{black!60} Version ${VERSION} — ${DATE} ${LABEL:+(${LABEL})}}
EOF

# 2) Build
make build

# 3) Publier dans releases/
mkdir -p releases
cp whitepaper/build/main.pdf "releases/Livre_blanc_RBK_v${VERSION}.pdf"

echo "Release générée: releases/Livre_blanc_RBK_v${VERSION}.pdf"