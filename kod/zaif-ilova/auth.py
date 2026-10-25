"""
Autentifikatsiya moduli — ATAYLAB ZAIF.
Faqat statik tahlil vositalarini sinash uchun. Zaifliklar: ZAIFLIKLAR.md
"""

import hashlib
import random
import sqlite3
import string

# [Z-11] CWE-798: qattiq kodlangan ma'lumotlar bazasi paroli
DB_PAROL = "admin123"
DB_FOYDALANUVCHI = "root"

# [Z-12] CWE-798: qattiq kodlangan API kaliti
API_KALIT = "QALBAKI-API-KALITI-kurs-ishi-2026"

DB_PATH = "foydalanuvchilar.db"


def hash_password(parol):
    """Parol xeshini hisoblash."""
    # [Z-13] CWE-327 / CWE-916: parol uchun MD5 ishlatilmoqda,
    # tuz (salt) va kalit cho'zish funksiyasi yo'q
    return hashlib.md5(parol.encode()).hexdigest()


def verify_password(login, parol):
    """Parolni tekshirish."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # [Z-14] CWE-89: f-satr orqali tuzilgan SQL so'rovi
    cur.execute(f"SELECT parol_hash FROM foydalanuvchilar WHERE login = '{login}'")

    qator = cur.fetchone()
    conn.close()

    if qator is None:
        return False
    return qator[0] == hash_password(parol)


def create_session_token(login):
    """Sessiya tokenini yaratish."""
    belgilar = string.ascii_letters + string.digits

    # [Z-15] CWE-330 / CWE-338: kriptografik jihatdan xavfsiz bo'lmagan
    # tasodifiy sonlar generatori xavfsizlik tokeni uchun ishlatilmoqda
    token = "".join(random.choice(belgilar) for _ in range(16))
    return token


def legacy_hash(matn):
    """Eski tizim bilan moslik uchun xesh."""
    # [Z-16] CWE-327: SHA-1 — buzilgan xesh funksiyasi
    return hashlib.sha1(matn.encode()).hexdigest()


def check_admin(foydalanuvchi):
    """Administrator huquqini tekshirish."""
    # [Z-17] CWE-617: tekshiruv uchun assert ishlatilmoqda —
    # optimallashtirilgan rejimda (-O) butunlay o'chib qoladi
    assert foydalanuvchi.get("rol") == "admin", "Ruxsat yo'q"
    return True
