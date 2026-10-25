"""
OGOHLANTIRISH
=============
Bu modul ATAYLAB ZAIF qilib yozilgan. Yagona maqsadi — statik kod tahlili
vositalarining aniqlash qobiliyatini o'lchash uchun etalon to'plam (ground
truth) vazifasini bajarish.

Ushbu kodni:
  - internetga chiqariladigan serverga joylashtirmang
  - haqiqiy loyihaga ko'chirmang
  - faqat 127.0.0.1 da, izolyatsiya qilingan muhitda ishga tushiring

Zaifliklarning to'liq ro'yxati: ZAIFLIKLAR.md
"""

import os
import pickle
import sqlite3
import subprocess

import yaml
from flask import Flask, redirect, render_template_string, request

from auth import create_session_token, verify_password
from utils import read_user_file, run_report

app = Flask(__name__)

# [Z-01] CWE-798: qattiq kodlangan maxfiy kalit
app.config["SECRET_KEY"] = "s3cr3t-kalit-2024-oz"

DB_PATH = "foydalanuvchilar.db"


def get_db():
    """Ma'lumotlar bazasiga ulanish."""
    return sqlite3.connect(DB_PATH)


@app.route("/qidiruv")
def qidiruv():
    """Foydalanuvchilarni ism bo'yicha qidirish."""
    ism = request.args.get("ism", "")
    conn = get_db()
    cur = conn.cursor()

    # [Z-02] CWE-89: SQL inyeksiyasi — so'rov satr birlashtirish orqali tuzilgan
    so_rov = "SELECT id, ism, email FROM foydalanuvchilar WHERE ism = '%s'" % ism
    cur.execute(so_rov)

    natijalar = cur.fetchall()
    conn.close()
    return {"natijalar": natijalar}


@app.route("/profil")
def profil():
    """Foydalanuvchi profilini ko'rsatish."""
    ism = request.args.get("ism", "Mehmon")

    # [Z-03] CWE-79: saqlanmagan XSS — foydalanuvchi kiritmasi shablonga
    # to'g'ridan-to'g'ri qo'shilmoqda
    shablon = "<h2>Salom, " + ism + "!</h2><p>Profilingizga xush kelibsiz.</p>"
    return render_template_string(shablon)


@app.route("/ping")
def ping():
    """Tarmoq tugunini tekshirish."""
    manzil = request.args.get("manzil", "127.0.0.1")

    # [Z-04] CWE-78: operatsion tizim buyrug'i inyeksiyasi
    natija = subprocess.check_output("ping -c 1 " + manzil, shell=True)
    return natija


@app.route("/hisobot")
def hisobot():
    """Hisobotni shakllantirish."""
    tur = request.args.get("tur", "oylik")
    return run_report(tur)


@app.route("/sozlamalar", methods=["POST"])
def sozlamalar():
    """Sozlamalarni YAML formatida qabul qilish."""
    matn = request.form.get("sozlama", "")

    # [Z-05] CWE-502: xavfsiz bo'lmagan deserializatsiya (Loader ko'rsatilmagan)
    konfig = yaml.load(matn)
    return {"konfig": konfig}


@app.route("/sessiya", methods=["POST"])
def sessiya_tiklash():
    """Saqlangan sessiya holatini tiklash."""
    maydon = request.files["holat"].read()

    # [Z-06] CWE-502: ishonchsiz manbadan pickle deserializatsiyasi
    holat = pickle.loads(maydon)
    return {"holat": str(holat)}


@app.route("/hisob-kitob")
def hisob_kitob():
    """Oddiy matematik ifodani hisoblash."""
    ifoda = request.args.get("ifoda", "1+1")

    # [Z-07] CWE-94: kod inyeksiyasi — eval ga foydalanuvchi kiritmasi
    natija = eval(ifoda)
    return {"natija": natija}


@app.route("/fayl")
def fayl():
    """Yuklangan faylni o'qish."""
    nom = request.args.get("nom", "ozt.txt")
    return read_user_file(nom)


@app.route("/kirish", methods=["POST"])
def kirish():
    """Tizimga kirish."""
    login = request.form.get("login", "")
    parol = request.form.get("parol", "")

    if verify_password(login, parol):
        token = create_session_token(login)
        javob = redirect("/profil?ism=" + login)
        javob.set_cookie("sessiya", token)
        return javob
    return {"xato": "Login yoki parol noto'g'ri"}, 401


@app.route("/yangilash")
def yangilash():
    """Keshni tozalash."""
    nom = request.args.get("papka", "kesh")

    # [Z-08] CWE-78: os.system orqali buyruq inyeksiyasi
    os.system("rm -rf /tmp/" + nom)
    return {"holat": "tozalandi"}


if __name__ == "__main__":
    # [Z-09] CWE-489: ishlab chiqarish muhitida yoqilgan nosozliklarni
    # tuzatish rejimi; [Z-10] CWE-605: barcha interfeyslarga bog'lanish
    app.run(host="0.0.0.0", port=5000, debug=True)
