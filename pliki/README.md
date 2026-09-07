# Pliki do pobrania (karty katalogowe, certyfikaty)

Ten katalog jest jedynym źródłem plików dla strony **Do pobrania** (`do-pobrania.html`).
Generator (`build.py`) pokazuje przycisk „Pobierz" **wyłącznie** dla pliku, który fizycznie tu leży.
Brak pliku = na stronie widać stan „W przygotowaniu — wysyłamy na życzenie" bez przycisku.
Nie wolno podpinać plików zastępczych ani fikcyjnych dokumentów.

## Konwencja nazw

| Pozycja na stronie | Plik polski | Plik angielski |
|---|---|---|
| Karta katalogowa produktu | `karta-<slug>-pl.pdf` | `karta-<slug>-en.pdf` |
| Certyfikat TÜV | `certyfikat-tuv-pl.pdf` | `certyfikat-tuv-en.pdf` |
| Testy ogniowe EN ISO 6941 / FAR 25.853b | `testy-ogniowe-en-iso-6941-pl.pdf` | `testy-ogniowe-en-iso-6941-en.pdf` |
| Wykaz NSN / NCAGE | `wykaz-nsn-ncage-pl.pdf` | `wykaz-nsn-ncage-en.pdf` |
| Instrukcja konserwacji | `instrukcja-konserwacji-pl.pdf` | `instrukcja-konserwacji-en.pdf` |

`<slug>` to nazwa pliku strony produktu z katalogu `produkty/` (np. `manekin-standard`).
Wystarczy wrzucić plik o właściwej nazwie i wypchnąć do repozytorium — GitHub Actions przebuduje stronę,
a przycisk pojawi się sam (z oznaczeniem języka: PL, EN lub oba).

Materiały producenta (SRP) publikujemy dopiero po otrzymaniu plików i zgody od producenta.

## Stan na 2026-09-07 (audyt)

W repozytorium nie ma jeszcze żadnego pliku PDF. Wszystkie pozycje czekają na materiały od producenta (Fred, SRP).
Dla każdej pozycji potrzebna jest wersja polska (PL) — jeśli producent ma tylko angielską (EN), publikujemy EN
i dopisujemy PL po tłumaczeniu.

| Pozycja | Obecne pliki | Brakujące pliki | Język | Status |
|---|---|---|---|---|
| Karta katalogowa — Manekin ratowniczy Standard | — | karta-manekin-standard-pl/en.pdf | do ustalenia | oczekuje na materiały od Freda |
| Karta katalogowa — Manekin ratowniczy PRO | — | karta-manekin-pro-pl/en.pdf | do ustalenia | oczekuje na materiały od Freda |
| Karta katalogowa — Manekin ratowniczy PRO MILITARY | — | karta-manekin-pro-military-pl/en.pdf | do ustalenia | oczekuje na materiały od Freda |
| Karta katalogowa — Manekin ratowniczy PRO ELITE | — | karta-manekin-pro-elite-pl/en.pdf | do ustalenia | oczekuje na materiały od Freda |
| Karta katalogowa — Manekin ratowniczy PRO ELITE MILITARY | — | karta-manekin-pro-elite-military-pl/en.pdf | do ustalenia | oczekuje na materiały od Freda |
| Karta katalogowa — Manekin ratowniczy z funkcją RKO | — | karta-manekin-rko-pl/en.pdf | do ustalenia | oczekuje na materiały od Freda |
| Karta katalogowa — Manekin do ratownictwa wodnego z funkcją RKO | — | karta-manekin-wodny-rko-pl/en.pdf | do ustalenia | oczekuje na materiały od Freda |
| Karta katalogowa — Manekiny do ratownictwa wodnego | — | karta-manekiny-ratownictwa-wodnego-pl/en.pdf | do ustalenia | oczekuje na materiały od Freda |
| Karta katalogowa — Manekin bariatryczny | — | karta-manekin-bariatryczny-pl/en.pdf | do ustalenia | oczekuje na materiały od Freda |
| Karta katalogowa — Manekiny pożarowe | — | karta-manekiny-pozarowe-pl/en.pdf | do ustalenia | oczekuje na materiały od Freda |
| Karta katalogowa — Symulatory ran | — | karta-symulatory-ran-pl/en.pdf | do ustalenia | oczekuje na materiały od Freda |
| Karta katalogowa — Symulacja medyczna | — | karta-symulacja-medyczna-pl/en.pdf | do ustalenia | oczekuje na materiały od Freda |
| Karta katalogowa — Pozostałe produkty | — | karta-pozostale-produkty-pl/en.pdf | do ustalenia | oczekuje na materiały od Freda |
| Certyfikat TÜV — manekiny Standard / RKO / bariatryczny | — | certyfikat-tuv-pl/en.pdf | do ustalenia | oczekuje na materiały od Freda |
| Wyniki testów ogniowych EN ISO 6941 / FAR 25.853b | — | testy-ogniowe-en-iso-6941-pl/en.pdf | do ustalenia | oczekuje na materiały od Freda |
| Wykaz numerów NSN / kod NCAGE producenta | — | wykaz-nsn-ncage-pl/en.pdf | do ustalenia | oczekuje na materiały od Freda |
| Instrukcja konserwacji i przechowywania manekinów | — | instrukcja-konserwacji-pl/en.pdf | do ustalenia | oczekuje na materiały od Freda |

Pozycja „Przykładowe opisy przedmiotu zamówienia (OPZ)" celowo nie ma pliku — udostępniana na życzenie
przez formularz zapytania (dokument przygotowujemy pod konkretne postępowanie).
