# Qiyosiy jadval: zaifliklarning aniqlanishi

| Kod | Fayl:qator | CWE | Zaiflik | Bandit | Semgrep (rasmiy) | Semgrep (maxsus) | CodeQL |
|---|---|---|---|---|---|---|---|
| Z-01 | app.py:30 | CWE-798 | Qattiq kodlangan SECRET_KEY | + | + | - | - |
| Z-02 | app.py:48 | CWE-89 | SQL inyeksiyasi (%-formatlash) | + | + | - | + |
| Z-03 | app.py:64 | CWE-79 | XSS / SSTI | - | + | + | + |
| Z-04 | app.py:73 | CWE-78 | Buyruq inyeksiyasi (subprocess) | + | + | - | + |
| Z-05 | app.py:90 | CWE-502 | Xavfsiz bo'lmagan yaml.load | + | + | - | + |
| Z-06 | app.py:100 | CWE-502 | pickle.loads | + | + | - | + |
| Z-07 | app.py:110 | CWE-94 | Kod inyeksiyasi (eval) | + | + | - | + |
| Z-08 | app.py:141 | CWE-78 | Buyruq inyeksiyasi (os.system) | + | + | - | + |
| Z-09 | app.py:148 | CWE-489 | debug=True | + | + | - | + |
| Z-10 | app.py:148 | CWE-605 | 0.0.0.0 ga bog'lanish | + | + | - | - |
| Z-11 | auth.py:12 | CWE-798 | Qattiq kodlangan DB_PAROL | - | - | + | - |
| Z-12 | auth.py:16 | CWE-798 | Qattiq kodlangan API_KALIT | - | - | + | - |
| Z-13 | auth.py:25 | CWE-327 | MD5 parol uchun | + | + | - | - |
| Z-14 | auth.py:34 | CWE-89 | SQL inyeksiyasi (f-satr) | + | - | - | + |
| Z-15 | auth.py:50 | CWE-330 | random moduli token uchun | + | - | - | - |
| Z-16 | auth.py:57 | CWE-327 | SHA-1 | + | + | - | - |
| Z-17 | auth.py:64 | CWE-617 | assert huquq tekshiruvi uchun | + | - | - | - |
| Z-18 | utils.py:21 | CWE-22 | Yo'l bo'ylab harakatlanish | - | - | - | + |
| Z-19 | utils.py:30 | CWE-78 | Buyruq inyeksiyasi (subprocess.run) | + | + | - | + |
| Z-20 | utils.py:37 | CWE-295 | verify=False | + | + | - | + |
| Z-21 | utils.py:45 | CWE-377 | tempfile.mktemp | + | - | - | + |
| Z-22 | utils.py:54 | CWE-532 | Parol jurnalda | - | - | + | - |
| Z-23 | utils.py:60 | CWE-732 | chmod 0o777 | + | + | - | + |
| Z-24 | utils.py:65 | CWE-390 | E'tiborsiz istisno | + | - | + | - |

`+` — aniqlandi, `-` — o'tkazib yuborildi
