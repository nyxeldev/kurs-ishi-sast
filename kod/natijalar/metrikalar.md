# Aniqlik metrikalari

Etalon to'plamdagi zaifliklar soni: **24**

| Vosita | Topilma | TP | Takroriy | FP | FN | Precision | Recall | F1 |
|---|---|---|---|---|---|---|---|---|
| Bandit | 22 | 19 | 0 | 3 | 5 | 0.86 | 0.79 | 0.83 |
| Semgrep (rasmiy) | 26 | 15 | 10 | 1 | 9 | 0.94 | 0.62 | 0.75 |
| Semgrep (maxsus) | 5 | 5 | 0 | 0 | 19 | 1.00 | 0.21 | 0.34 |
| CodeQL | 17 | 14 | 3 | 0 | 10 | 1.00 | 0.58 | 0.74 |

`Topilma` — vosita bergan xabarlar soni; `TP` — tasdiqlangan etalon
zaifliklar soni; `Takroriy` — ayni bir zaiflik haqidagi qo'shimcha
xabarlar (metrikaga kirmaydi); `FP` — etalonda mavjud bo'lmagan joyga
berilgan xabarlar.


## Yolg'on ijobiy natijalar


### Bandit (3 ta)

- `app.py:17` — B403: Consider possible security implications associated with pickle module.
- `app.py:19` — B404: Consider possible security implications associated with the subprocess
- `utils.py:8` — B404: Consider possible security implications associated with the subprocess

### Semgrep (rasmiy) (1 ta)

- `app.py:124` — open-redirect: Data from request is passed to redirect(). This is an open redirect an

### Semgrep (maxsus) (0 ta)

- yo'q

### CodeQL (0 ta)

- yo'q