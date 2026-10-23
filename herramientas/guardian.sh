#!/usr/bin/env bash
# Guardián anti-fuga: impide que este repo publique datos de una instalación
# real (servidores, correos, identificadores, teléfonos, claves).
#
# Revisa todos los archivos del repo (los ignorados por .gitignore no) contra:
#   1. patrones genéricos, aquí abajo;
#   2. una lista privada de textos exactos, FUERA del repo, si existe:
#      $GUARDIAN_PATRONES o ~/.config/guardian-anti-fuga/patrones.txt
#
# Nunca imprime lo que encontró: solo archivo, línea y tipo. Así tampoco filtra
# nada en los registros públicos de GitHub Actions.
#
# Uso: herramientas/guardian.sh   (sale con 1 si encuentra algo)
set -u
cd "$(git rev-parse --show-toplevel)" || exit 2

YO="herramientas/guardian.sh"
PRIVADOS="${GUARDIAN_PATRONES:-$HOME/.config/guardian-anti-fuga/patrones.txt}"
# Datos que salen en publico A PROPOSITO (un contacto, un usuario de GitHub...).
PUBLICOS="herramientas/guardian-permitidos.txt"
BORDE='(^|[^A-Za-z0-9_])'
FALLOS=0

archivos() { git ls-files -co --exclude-standard | grep -v -x -e "$YO" -e "$PUBLICOS"; }
# Quita las lineas que solo contienen datos publicos permitidos.
permitidos() { if [ -s "$PUBLICOS" ]; then grep -v -F -f <(grep -v -E '^\s*(#|$)' "$PUBLICOS"); else cat; fi; }

# tipo|expresión regular extendida
GENERICOS=(
  "servidor de Hostinger|srv[0-9]{4,}\.hstgr\.cloud"
  "dirección IP|${BORDE}([0-9]{1,3}\.){3}[0-9]{1,3}"
  "identificador de Superchat|${BORDE}(mc|cv|ct|us|ib|tn|la|wh)_[A-Za-z0-9]{15,}"
  "usuario de Slack|${BORDE}U0[A-Z0-9]{8,10}([^A-Za-z0-9]|$)"
  "teléfono|\+[0-9]{2}[ -]?[0-9]{3}[ -]?[0-9]{2,3}[ -]?[0-9]{2,3}"
  "referencia de 1Password con id real|op://[^/[:space:]]+/[a-z0-9]{26}"
  "clave de API|sk-ant-|sk_live_|sk_test_|ghp_[A-Za-z0-9]{20,}|github_pat_|xox[abpr]-|AKIA[0-9A-Z]{16}|-----BEGIN [A-Z ]*PRIVATE KEY"
  "clave larga en hexadecimal|[0-9a-fA-F]{48,}"
)
# Lo que sí puede salir: ejemplos y direcciones locales.
PERMITIDO='127\.0\.0\.1|0\.0\.0\.0|example\.(com|org)|tudominio|tuproveedor|correo\.com|noreply'

reportar() { # archivo:línea tipo
  echo "  ✗ $1  ($2)"
  FALLOS=$((FALLOS + 1))
}

while IFS= read -r f; do
  [ -f "$f" ] || continue
  for par in "${GENERICOS[@]}"; do
    tipo="${par%%|*}"; regex="${par#*|}"
    grep -n -I -E "$regex" -- "$f" 2>/dev/null | grep -v -E "$PERMITIDO" | permitidos | cut -d: -f1 |
      while IFS= read -r n; do echo "$f:$n|$tipo"; done
  done
  # Correos que no son de ejemplo
  grep -n -I -o -E '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' -- "$f" 2>/dev/null |
    grep -v -E "$PERMITIDO|^[0-9]+:tu@|^[0-9]+:usuario%40|^[0-9]+:panel@tudominio" | permitidos | cut -d: -f1 |
    while IFS= read -r n; do echo "$f:$n|correo electrónico"; done
  if [ -f "$PRIVADOS" ]; then
    grep -n -I -i -F -f <(grep -v -E '^\s*(#|$)' "$PRIVADOS") -- "$f" 2>/dev/null | cut -d: -f1 |
      while IFS= read -r n; do echo "$f:$n|dato privado de tu lista"; done
  fi
done < <(archivos) | sort -u > "${TMPDIR:-/tmp}/guardian.$$"

while IFS='|' read -r donde tipo; do reportar "$donde" "$tipo"; done < "${TMPDIR:-/tmp}/guardian.$$"
rm -f "${TMPDIR:-/tmp}/guardian.$$"

if [ ! -f "$PRIVADOS" ]; then
  echo "Aviso: sin lista privada ($PRIVADOS); solo se revisaron los patrones genéricos."
fi
if [ "$FALLOS" -gt 0 ]; then
  echo "Guardián: $FALLOS línea(s) con datos que no deben publicarse. Nada se sube hasta quitarlos."
  exit 1
fi
echo "Guardián: limpio."
