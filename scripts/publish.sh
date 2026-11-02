#!/usr/bin/env bash
# Publica la web en Hostinger: regenera site/, hace commit y actualiza la rama `hostinger`
# (Hostinger la descarga automáticamente por el webhook de GitHub).
set -euo pipefail
cd "$(dirname "$0")/.."
python3 build/build.py
cp media-kit/MIAGAZINE-Media-Kit-2026-*.pdf site/media-kit/ 2>/dev/null || true
git add -A
git diff --cached --quiet || git commit -m "${1:-Update site}"
BR=$(git rev-parse --abbrev-ref HEAD)
git push -u origin "$BR"
git branch -D hostinger 2>/dev/null || true
git subtree split --prefix=site -b hostinger
git push -f origin hostinger
echo "Publicado: rama hostinger actualizada"
