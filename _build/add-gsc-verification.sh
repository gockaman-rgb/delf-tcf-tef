#!/usr/bin/env bash
# Pose la balise de vérification Google Search Console sur toutes les pages du site.
#
# Usage :
#   ./_build/add-gsc-verification.sh VOTRE_CODE
#
# Où trouver VOTRE_CODE :
#   Search Console → Ajouter une propriété → « Préfixe d'URL » → https://delf-tcf-tef.fr
#   → méthode « Balise HTML ». Google affiche :
#       <meta name="google-site-verification" content="AbC123..." />
#   Ne copiez QUE la valeur du content, sans les guillemets.
#
# Idempotent : relancer le script remplace la balise existante au lieu d'en ajouter une seconde.

set -euo pipefail

CODE="${1:-}"
if [ -z "$CODE" ]; then
  echo "Erreur : code de vérification manquant." >&2
  echo "Usage : $0 VOTRE_CODE" >&2
  exit 1
fi

# Le script vit dans site/_build/, on remonte à site/
cd "$(dirname "$0")/.."
ROOT="$(pwd)"
echo "Racine du site : $ROOT"

TAG="<meta name=\"google-site-verification\" content=\"$CODE\">"
N=0

while IFS= read -r f; do
  if grep -q 'name="google-site-verification"' "$f"; then
    # Remplace la balise existante
    python3 - "$f" "$CODE" <<'PY'
import re, sys
path, code = sys.argv[1], sys.argv[2]
s = open(path, encoding='utf-8').read()
s = re.sub(r'<meta name="google-site-verification"[^>]*>',
           f'<meta name="google-site-verification" content="{code}">', s)
open(path, 'w', encoding='utf-8').write(s)
PY
    echo "  maj  $f"
  else
    # Insère juste après <meta charset="utf-8">
    python3 - "$f" "$CODE" <<'PY'
import sys
path, code = sys.argv[1], sys.argv[2]
s = open(path, encoding='utf-8').read()
anchor = '<meta charset="utf-8">'
tag = f'\n<meta name="google-site-verification" content="{code}">'
if anchor in s:
    s = s.replace(anchor, anchor + tag, 1)
    open(path, 'w', encoding='utf-8').write(s)
else:
    sys.exit(f"  !! ancre introuvable dans {path}")
PY
    echo "  pose $f"
  fi
  N=$((N+1))
done < <(find . -name '*.html' -not -path './_build/*' | sort)

echo
echo "$N page(s) traitée(s)."
echo
echo "Étapes suivantes :"
echo "  git add -A && git commit -m 'GSC : balise de verification' && git push"
echo "  attendez le déploiement, puis cliquez « Valider » dans Search Console."
echo
echo "Vérifier que la balise est bien servie en ligne :"
echo "  curl -s https://delf-tcf-tef.fr/ | grep google-site-verification"
