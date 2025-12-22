#!/usr/bin/env bash
set -euo pipefail

latexmk -C -outdir=whitepaper/build
find whitepaper/build -type f -name 'texput.log' -delete || true
