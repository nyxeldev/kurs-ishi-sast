# Topilmalarning etalon to'plam bilan moslashtirilishi

Har bir vosita xabarining qaysi etalon zaiflikka bog'langani.
`FP` — hech qaysi etalon yozuviga bog'lanmagan xabar.


## Bandit

| Fayl:qator | Qoida | Vosita CWE | Bog'landi | Etalon CWE |
|---|---|---|---|---|
| app.py:17 | `B403` | CWE-502 | FP | — |
| app.py:19 | `B404` | CWE-78 | FP | — |
| app.py:30 | `B105` | CWE-259 | Z-01 | CWE-798 |
| app.py:48 | `B608` | CWE-89 | Z-02 | CWE-89 |
| app.py:73 | `B602` | CWE-78 | Z-04 | CWE-78 |
| app.py:90 | `B506` | CWE-20 | Z-05 | CWE-502 |
| app.py:100 | `B301` | CWE-502 | Z-06 | CWE-502 |
| app.py:110 | `B307` | CWE-78 | Z-07 | CWE-94 |
| app.py:141 | `B605` | CWE-78 | Z-08 | CWE-78 |
| app.py:148 | `B104` | CWE-605 | Z-10 | CWE-605 |
| app.py:148 | `B201` | CWE-94 | Z-09 | CWE-489 |
| auth.py:25 | `B324` | CWE-327 | Z-13 | CWE-327 |
| auth.py:34 | `B608` | CWE-89 | Z-14 | CWE-89 |
| auth.py:50 | `B311` | CWE-330 | Z-15 | CWE-330 |
| auth.py:57 | `B324` | CWE-327 | Z-16 | CWE-327 |
| auth.py:64 | `B101` | CWE-703 | Z-17 | CWE-617 |
| utils.py:8 | `B404` | CWE-78 | FP | — |
| utils.py:30 | `B602` | CWE-78 | Z-19 | CWE-78 |
| utils.py:37 | `B501` | CWE-295 | Z-20 | CWE-295 |
| utils.py:45 | `B306` | CWE-377 | Z-21 | CWE-377 |
| utils.py:60 | `B103` | CWE-732 | Z-23 | CWE-732 |
| utils.py:67 | `B110` | CWE-703 | Z-24 | CWE-390 |

## Semgrep (rasmiy)

| Fayl:qator | Qoida | Vosita CWE | Bog'landi | Etalon CWE |
|---|---|---|---|---|
| app.py:30 | `avoid_hardcoded_config_SECRET_KEY` | CWE-489 | Z-01 | CWE-798 |
| app.py:43 | `sql-injection-db-cursor-execute` | CWE-89 | Z-02 | CWE-89 |
| app.py:48 | `tainted-sql-string` | CWE-704 | Z-02 | CWE-89 |
| app.py:63 | `raw-html-format` | CWE-79 | Z-03 | CWE-79 |
| app.py:63 | `raw-html-format` | CWE-79 | Z-03 | CWE-79 |
| app.py:64 | `render-template-string` | CWE-96 | Z-03 | CWE-79 |
| app.py:73 | `dangerous-subprocess-use` | CWE-78 | Z-04 | CWE-78 |
| app.py:73 | `subprocess-injection` | CWE-78 | Z-04 | CWE-78 |
| app.py:73 | `subprocess-shell-true` | CWE-78 | Z-04 | CWE-78 |
| app.py:90 | `insecure-deserialization` | CWE-502 | Z-05 | CWE-502 |
| app.py:100 | `avoid-pickle` | CWE-502 | Z-06 | CWE-502 |
| app.py:100 | `insecure-deserialization` | CWE-502 | Z-06 | CWE-502 |
| app.py:107 | `user-eval` | CWE-95 | Z-07 | CWE-94 |
| app.py:110 | `eval-detected` | CWE-95 | Z-07 | CWE-94 |
| app.py:110 | `eval-injection` | CWE-95 | Z-07 | CWE-94 |
| app.py:124 | `open-redirect` | CWE-601 | FP | — |
| app.py:138 | `command-injection-os-system` | CWE-78 | Z-08 | CWE-78 |
| app.py:141 | `dangerous-system-call` | CWE-78 | Z-08 | CWE-78 |
| app.py:141 | `os-system-injection` | CWE-78 | Z-08 | CWE-78 |
| app.py:148 | `avoid_app_run_with_bad_host` | CWE-668 | Z-10 | CWE-605 |
| app.py:148 | `debug-enabled` | CWE-489 | Z-09 | CWE-489 |
| auth.py:25 | `insecure-hash-algorithm-md5` | CWE-327 | Z-13 | CWE-327 |
| auth.py:57 | `insecure-hash-algorithm-sha1` | CWE-327 | Z-16 | CWE-327 |
| utils.py:30 | `subprocess-shell-true` | CWE-78 | Z-19 | CWE-78 |
| utils.py:37 | `disabled-cert-validation` | CWE-295 | Z-20 | CWE-295 |
| utils.py:60 | `insecure-file-permissions` | CWE-276 | Z-23 | CWE-732 |

## Semgrep (maxsus)

| Fayl:qator | Qoida | Vosita CWE | Bog'landi | Etalon CWE |
|---|---|---|---|---|
| app.py:64 | `flask-shablon-inyeksiyasi` | CWE-79 | Z-03 | CWE-79 |
| auth.py:12 | `ozbekcha-qattiq-kodlangan-sir` | CWE-798 | Z-11 | CWE-798 |
| auth.py:16 | `ozbekcha-qattiq-kodlangan-sir` | CWE-798 | Z-12 | CWE-798 |
| utils.py:54 | `jurnalga-maxfiy-malumot` | CWE-532 | Z-22 | CWE-532 |
| utils.py:65 | `etiborsiz-istisno` | CWE-390 | Z-24 | CWE-390 |

## CodeQL

| Fayl:qator | Qoida | Vosita CWE | Bog'landi | Etalon CWE |
|---|---|---|---|---|
| app.py:49 | `py/sql-injection` | CWE-89 | Z-02 | CWE-89 |
| app.py:64 | `py/reflective-xss` | CWE-79 | Z-03 | CWE-79 |
| app.py:64 | `py/template-injection` | CWE-74 | Z-03 | CWE-79 |
| app.py:73 | `py/command-line-injection` | CWE-78 | Z-04 | CWE-78 |
| app.py:90 | `py/unsafe-deserialization` | CWE-502 | Z-05 | CWE-502 |
| app.py:91 | `py/reflective-xss` | CWE-79 | FP | — |
| app.py:100 | `py/unsafe-deserialization` | CWE-502 | Z-06 | CWE-502 |
| app.py:101 | `py/reflective-xss` | CWE-79 | FP | — |
| app.py:110 | `py/code-injection` | CWE-94 | Z-07 | CWE-94 |
| app.py:141 | `py/command-line-injection` | CWE-78 | Z-08 | CWE-78 |
| app.py:148 | `py/flask-debug` | CWE-215 | Z-09 | CWE-489 |
| auth.py:34 | `py/sql-injection` | CWE-89 | Z-14 | CWE-89 |
| utils.py:22 | `py/path-injection` | CWE-22 | Z-18 | CWE-22 |
| utils.py:30 | `py/command-line-injection` | CWE-78 | Z-19 | CWE-78 |
| utils.py:37 | `py/request-without-cert-validation` | CWE-295 | Z-20 | CWE-295 |
| utils.py:45 | `py/insecure-temporary-file` | CWE-377 | Z-21 | CWE-377 |
| utils.py:60 | `py/overly-permissive-file` | CWE-732 | Z-23 | CWE-732 |