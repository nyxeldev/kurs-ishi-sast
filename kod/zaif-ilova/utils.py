"""
Yordamchi funksiyalar moduli — ATAYLAB ZAIF.
Faqat statik tahlil vositalarini sinash uchun. Zaifliklar: ZAIFLIKLAR.md
"""

import logging
import os
import subprocess
import tempfile

import requests

YUKLAMALAR_PAPKASI = "yuklamalar"
TASHQI_XIZMAT = "https://hisobot.example.uz/api/v1"


def read_user_file(nom):
    """Yuklamalar papkasidan faylni o'qish."""
    # [Z-18] CWE-22: yo'l bo'ylab harakatlanish (path traversal) —
    # fayl nomi normallashtirilmagan va papka chegarasi tekshirilmagan
    yo_l = os.path.join(YUKLAMALAR_PAPKASI, nom)
    with open(yo_l, "r", encoding="utf-8") as f:
        return f.read()


def run_report(tur):
    """Tashqi skript orqali hisobot shakllantirish."""
    # [Z-19] CWE-78: shell=True bilan satr birlashtirish
    buyruq = "python hisobot_generator.py --tur " + tur
    natija = subprocess.run(buyruq, shell=True, capture_output=True)
    return natija.stdout


def fetch_external_data(endpoint):
    """Tashqi xizmatdan ma'lumot olish."""
    # [Z-20] CWE-295: TLS sertifikati tekshiruvi o'chirilgan
    javob = requests.get(TASHQI_XIZMAT + endpoint, verify=False, timeout=10)
    return javob.json()


def create_temp_report(mazmun):
    """Vaqtinchalik hisobot faylini yaratish."""
    # [Z-21] CWE-377: xavfsiz bo'lmagan vaqtinchalik fayl yaratish
    # (poyga holati — race condition)
    yo_l = tempfile.mktemp(suffix=".txt")
    with open(yo_l, "w", encoding="utf-8") as f:
        f.write(mazmun)
    return yo_l


def log_login_attempt(login, parol):
    """Kirish urinishini jurnalga yozish."""
    # [Z-22] CWE-532: maxfiy ma'lumot jurnalga yozilmoqda
    logging.info("Kirish urinishi: login=%s parol=%s", login, parol)


def set_permissions(yo_l):
    """Fayl huquqlarini o'rnatish."""
    # [Z-23] CWE-732: haddan tashqari keng fayl huquqlari
    os.chmod(yo_l, 0o777)


def tekshiruvni_otkazish(yo_l):
    """Fayl yaxlitligini tekshirish."""
    try:
        set_permissions(yo_l)
    except Exception:
        # [Z-24] CWE-390: istisno holati e'tiborsiz qoldirilmoqda —
        # xavfsizlik tekshiruvining ishdan chiqishi yashiriladi
        pass


def bogliq_modul_ishlatish():
    """Tashqi modulni chaqirish."""
    natija = {}
    try:
        natija = fetch_external_data("/holat")
    except Exception as xato:
        logging.error("Tashqi xizmat xatosi: %s", xato)
    return natija
