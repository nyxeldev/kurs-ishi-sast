> ## OGOHLANTIRISH
>
> Bu ombor `kod/zaif-ilova/` papkasida **ataylab zaif qilingan** Python kodini
> saqlaydi. U statik kod tahlili vositalarini (Bandit, Semgrep, CodeQL,
> pip-audit) qiyosiy sinash uchun etalon to'plam (ground truth) vazifasini
> bajaradi — kurs ishining amaliy qismi.
>
> - Bu kod internetga chiqariladigan serverga joylashtirilmaydi
> - `requirements.txt` dagi versiyalar ataylab eskirgan (SCA ni sinash uchun)
> - Undagi hech bir namuna haqiqiy loyihaga ko'chirilmasligi kerak
> - Zaifliklarning to'liq ro'yxati: `kod/zaif-ilova/ZAIFLIKLAR.md`

# Ish boshlash qo'llanmasi

## 1-qadam. Papkani joyiga qo'yish

Arxivni quyidagi manzilga chiqaring:

```
C:\Users\Analyst\Documents\Jahongir\kurs-ishi
```

Ichida `CLAUDE.md` fayli ko'rinib tursa, to'g'ri bo'lgan.

---

## 2-qadam. Claude Code ni shu papkaga ulash

1. Claude Desktop ilovasini oching
2. Yuqoridagi **Code** tabiga o'ting
3. Ish papkasi sifatida `C:\Users\Analyst\Documents\Jahongir\kurs-ishi` ni tanlang

Birinchi buyruq sifatida shuni yozing:

> CLAUDE.md va reja.md ni o'qi. Keyin kod/zaif-ilova/ ni tekshirib ko'r:
> ilova ishga tushadimi, requirements.txt to'g'rimi. Hisobot ber.

---

## 3-qadam. Amaliy qismni bajarish (Claude Code)

Ketma-ketlik:

```
1) Virtual muhit yaratish va vositalarni o'rnatish
2) kod/tahlil/tahlil.sh ni ishga tushirish
3) Natijalarni kod/natijalar/ da tekshirish
4) hisobot.py orqali qiyosiy jadvalni hisoblash
5) Skrinshotlarni ilovalar/ ga saqlash
```

Claude Code ga aytiladigan buyruq:

> kod/tahlil/tahlil.sh dagi bosqichlarni bajar. Har bir vosita uchun
> versiyani va ishlash vaqtini qayd et. Natijalarni kod/natijalar/ ga yoz.

---

## 4-qadam. Matnni yozish (Cowork yoki Code)

Claude Desktop'da **Cowork** tabini xuddi shu papkaga oching.

> matn/01-bob.md ni reja.md ga muvofiq to'liq yoz.
> Har bir faktga manba ko'rsat, manbasiz raqam yozma.

Boblar tartibi: `01-bob` → `02-bob` → amaliy qism → `03-bob` → `00-kirish` → `04-xulosa`

**Kirish va xulosa oxirida yoziladi** — shunda ular haqiqiy natijalarga mos keladi.

---

## 5-qadam. Yakuniy hujjat

> matn/ ichidagi barcha .md fayllarni bitta Word hujjatiga yig'.
> Mundarija, sahifa raqamlari, jadval va rasm nomlari qo'shilsin.
> Natijani ilovalar/kurs-ishi.docx ga saqla.

---

## Foydali eslatmalar

- **Har bir seansdan keyin** `HOLAT.md` ni yangilashni so'rang
- Claude Code tezroq, Cowork hujjat formatlashda qulayroq — ikkalasi bitta limitdan foydalanadi
- Manba sifatida ishlatgan PDF/maqolalarni `manbalar/` ga tashlang, agent ularni o'qiydi
- Agar agent biror raqamni manbasiz yozsa — `CLAUDE.md` ning 2-bo'limini eslatib qo'ying
