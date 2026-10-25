#!/usr/bin/env bash
# Barcha statik tahlil vositalarini ketma-ket ishga tushirish
# Ishlatish:  bash kod/tahlil/tahlil.sh

set -u
ILDIZ="$(cd "$(dirname "$0")/../.." && pwd)"
OBYEKT="$ILDIZ/kod/zaif-ilova"
NATIJA="$ILDIZ/kod/natijalar"
QOIDALAR="$ILDIZ/kod/tahlil/qoidalar/maxsus-qoidalar.yml"

mkdir -p "$NATIJA"
: > "$NATIJA/00-vaqt.txt"   # vaqt jurnali har ishga tushirishda tozalanadi
echo "=== Statik tahlil boshlandi: $(date '+%Y-%m-%d %H:%M') ==="
echo "Sinov obyekti: $OBYEKT"
echo

# --- Versiyalarni qayd etish (ishda keltirish uchun) ---
{
  echo "# Sinov muhiti"
  echo "Sana: $(date '+%Y-%m-%d %H:%M')"
  echo "OS: $(uname -sr 2>/dev/null || echo 'Windows')"
  echo "Python: $(python --version 2>&1)"
  echo "Bandit: $(bandit --version 2>&1 | head -1 | awk '{print $NF}')"
  echo "Semgrep: $(semgrep --version 2>&1 | head -1)"
  echo "pip-audit: $(pip-audit --version 2>&1 | head -1)"
  echo "CodeQL: $(command -v codeql >/dev/null 2>&1 && codeql version --format=terse 2>&1 | head -1 || echo 'mavjud emas')"
} > "$NATIJA/00-muhit.txt"
cat "$NATIJA/00-muhit.txt"
echo

# --- 1. Bandit ---
echo "[1/5] Bandit ishga tushirilmoqda..."
BOSH=$(date +%s)
bandit -r "$OBYEKT" -f json -o "$NATIJA/01-bandit.json" -q
bandit -r "$OBYEKT" -f txt  -o "$NATIJA/01-bandit.txt" -q
TUGASH=$(date +%s)
echo "    tugadi, $((TUGASH-BOSH)) soniya"
echo "Bandit: $((TUGASH-BOSH)) s" >> "$NATIJA/00-vaqt.txt"

# --- 2. Semgrep (rasmiy qoidalar bazasi, internet kerak) ---
echo "[2/5] Semgrep (p/python + p/security-audit)..."
BOSH=$(date +%s)
semgrep scan --config=p/python --config=p/security-audit \
  --json --metrics=off -o "$NATIJA/02-semgrep.json" "$OBYEKT" || \
  echo "    OGOHLANTIRISH: qoidalar bazasiga ulanib bo'lmadi (internet kerak)"
TUGASH=$(date +%s)
echo "    tugadi, $((TUGASH-BOSH)) soniya"
echo "Semgrep (rasmiy): $((TUGASH-BOSH)) s" >> "$NATIJA/00-vaqt.txt"

# --- 3. Semgrep (maxsus qoidalar — 3.4-band) ---
echo "[3/5] Semgrep (maxsus qoidalar)..."
BOSH=$(date +%s)
semgrep scan --config="$QOIDALAR" --json --metrics=off \
  -o "$NATIJA/03-semgrep-maxsus.json" "$OBYEKT"
TUGASH=$(date +%s)
echo "    tugadi, $((TUGASH-BOSH)) soniya"
echo "Semgrep (maxsus): $((TUGASH-BOSH)) s" >> "$NATIJA/00-vaqt.txt"

# --- 4. pip-audit (SCA) ---
echo "[4/5] pip-audit (bog'liqliklar tahlili)..."
# requirements.txt dagi versiyalar ataylab ziddiyatli (requests 2.19.1
# urllib3<1.24 talab qiladi), shu sababli bog'liqliklarni qayta hisoblash
# o'chiriladi — faqat qadalgan versiyalar tekshiriladi.
PA=(--no-deps --disable-pip)
BOSH=$(date +%s)
pip-audit -r "$OBYEKT/requirements.txt" "${PA[@]}" -f json -o "$NATIJA/04-pip-audit.json" || true
pip-audit -r "$OBYEKT/requirements.txt" "${PA[@]}" > "$NATIJA/04-pip-audit.txt" 2>&1 || true
TUGASH=$(date +%s)
echo "    tugadi, $((TUGASH-BOSH)) soniya"
echo "pip-audit: $((TUGASH-BOSH)) s" >> "$NATIJA/00-vaqt.txt"

# --- 5. CodeQL (semantik tahlil — zaharlangan ma'lumot oqimi) ---
# CodeQL CLI PATH da topilsa ishga tushiriladi. Tahlil uzoq davom etadi
# (sinov mashinasida ~46 daqiqa), shu sababli oxirgi bosqichga qo'yilgan.
# O'rnatish: github/codeql-action relizidan codeql-bundle-win64.tar.gz
echo "[5/5] CodeQL (python-security-extended)..."
if command -v codeql >/dev/null 2>&1; then
  BOSH=$(date +%s)
  codeql database create "$NATIJA/codeql-db" --language=python     --source-root="$OBYEKT" --overwrite
  # MSYS2_ARG_CONV_EXCL — Git Bash so'rov to'plami nomini yo'lga aylantirmasligi uchun
  MSYS2_ARG_CONV_EXCL="codeql/" codeql database analyze "$NATIJA/codeql-db"     "codeql/python-queries:codeql-suites/python-security-extended.qls"     --format=sarif-latest --output="$NATIJA/05-codeql.sarif"     --sarif-category=codeql-python --threads=0
  TUGASH=$(date +%s)
  echo "    tugadi, $((TUGASH-BOSH)) soniya"
  echo "CodeQL: $((TUGASH-BOSH)) s" >> "$NATIJA/00-vaqt.txt"
else
  echo "    O'TKAZIB YUBORILDI: codeql CLI PATH da topilmadi"
fi

echo
echo "=== Tahlil yakunlandi. Natijalar: $NATIJA ==="
echo "Keyingi qadam: python kod/tahlil/hisobot.py"
