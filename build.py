#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator statycznych stron serwisu SRP Polska.
Uruchom: python3 build.py  -> generuje pliki HTML w katalogu głównym.
Treści edytuj poniżej (PRODUCTS, COURSES, teksty w funkcjach stron).
"""
import os, html, json

ROOT = os.path.dirname(os.path.abspath(__file__))

# --- dane edytowalne przez automaty (n8n) i ludzi: data/site.json ---------
def load_site_data():
    path = os.path.join(ROOT, "data", "site.json")
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"! data/site.json nieczytelny ({e}) — używam wartości domyślnych")
        return {}

SITE = load_site_data()
_firma = SITE.get("firma", {})

BRAND = _firma.get("nazwa") or "SRP Polska"
DISTRIBUTOR = _firma.get("opis") or "Wyłączny dystrybutor produktów SRP w Polsce"
PHONE = _firma.get("telefon") or "+48 000 000 000"
EMAIL = _firma.get("email") or "biuro@twojadomena.pl"
NAZWA_PELNA = _firma.get("nazwa_pelna") or ""
ADRES_ULICA = _firma.get("adres_ulica") or ""
ADRES_MIASTO = _firma.get("adres_miasto") or ""
NIP = _firma.get("nip") or ""
KRS = _firma.get("krs") or ""
REGON = _firma.get("regon") or ""
# blok danych rejestrowych — wymog ustawy o swiadczeniu uslug droga elektroniczna
if NAZWA_PELNA:
    DANE_REJESTROWE = (f"{NAZWA_PELNA}<br>{ADRES_ULICA}<br>{ADRES_MIASTO}<br>"
                       f"NIP {NIP} &nbsp;·&nbsp; KRS {KRS} &nbsp;·&nbsp; REGON {REGON}")
else:
    DANE_REJESTROWE = "[dane rejestrowe do uzupełnienia]"
# adres serwisu: własna domena po jej uruchomieniu, do tego czasu GitHub Pages
_domena = SITE.get("domena", {}) or {}
DOMAIN_ACTIVE = bool(_domena.get("aktywna")) and bool(_domena.get("adres"))
HOSTING = (_domena.get("hosting") or "pages").strip().lower()
DOMAIN = (_domena.get("adres") or "").strip()
for _pref in ("https://", "http://"):
    if DOMAIN.startswith(_pref):
        DOMAIN = DOMAIN[len(_pref):]
DOMAIN = DOMAIN.strip("/")
BASE_URL = f"https://{DOMAIN}" if DOMAIN_ACTIVE else "https://ogradost.github.io/srp"
FORM_ENDPOINT = (SITE.get("formularze", {}) or {}).get("endpoint", "").strip()

# atrybuty formularzy: z webhookiem n8n (AJAX) albo tryb "kanał w przygotowaniu"
if FORM_ENDPOINT:
    form_attrs = f'action="{FORM_ENDPOINT}" method="post" data-lead-form="1"'
    FORM_NOTE = (f"Odpowiadamy zwykle w ciągu jednego dnia roboczego. Administratorem Twoich danych jest {BRAND}. "
                 "Podane dane przetwarzamy wyłącznie w celu obsługi tego zapytania i kontaktu w sprawie oferty — "
                 "nie wykorzystujemy ich do marketingu bez osobnej zgody. Masz prawo dostępu do swoich danych, "
                 "ich sprostowania, usunięcia i ograniczenia przetwarzania. "
                 "<a href=\"/polityka-prywatnosci.html\">Pełna informacja o przetwarzaniu danych</a>.")
else:
    form_attrs = 'action="#" method="post" data-lead-form="0"'
    FORM_NOTE = (f'Wysyłka formularza jest w trakcie uruchamiania — napisz bezpośrednio na '
                 f'<a href="mailto:{EMAIL}">{EMAIL}</a> lub zadzwoń: '
                 f'<a href="tel:{PHONE.replace(" ", "")}">{PHONE}</a>.')

# ---------------------------------------------------------------- produkty
PRODUCTS = [
    {
        "slug": "manekin-pro-elite-military",
        "name": "Manekin ratowniczy PRO ELITE MILITARY",
        "short": "Najbardziej zaawansowany fantom taktyczny SRP — drogi oddechowe, tętno, dźwięki oddechu i trzy krwawiące rany do treningu TCCC.",
        "features": [
            "Zintegrowany symulator dróg oddechowych: rurka nosowo-gardłowa, ustno-gardłowa, i-gel / maska krtaniowa oraz intubacja",
            "Unoszenie klatki piersiowej przy prawidłowej wentylacji; ruch nadbrzusza sygnalizuje błędną technikę",
            "Wyczuwalne, regulowane tętno (0 / 70 / 120 uderzeń na minutę) na obu rękach",
            "Wbudowany głośnik — odgłosy oddechu i dźwięki scenariusza",
            "Trzy realistyczne rany z podłączeniem zewnętrznego źródła krwi: amputacja urazowa lewej nogi (staza taktyczna), rana postrzałowa prawej pachwiny (packing), rana cięta lewego ramienia (ucisk bezpośredni / opatrunek uciskowy)",
            "Zachowuje się jak osoba nieprzytomna — przegubowa konstrukcja o realistycznym rozkładzie masy",
        ],
        "specs": [
            ("Wzrost", "180 cm"),
            ("Masa", "50 / 60 / 70 / 80 kg (na zamówienie 40–90 kg)"),
            ("Zakres temperatur pracy", "od −30°C do +70°C"),
            ("Materiał", "wytrzymała skóra, elementy z wzmocnionego silikonu, drogi oddechowe z PVC (zamek do czyszczenia w warunkach polowych)"),
            ("W zestawie", "umundurowanie maskujące M90, buty zamocowane na stałe, butelki i przewody do symulacji krwotoku"),
        ],
        "use": "Szkolenia wojskowe i służb ratowniczych: zabezpieczenie dróg oddechowych, tamowanie krwotoków, złożone scenariusze urazowe (TCCC / TECC).",
    },
    {
        "slug": "manekin-pro-elite",
        "name": "Manekin ratowniczy PRO ELITE",
        "short": "Zaawansowany fantom do treningu zabezpieczania dróg oddechowych i kontroli krwotoków, z dostępem donaczyniowym i głośnikiem scenariuszowym.",
        "features": [
            "Symulator dróg oddechowych: rurka nosowo-gardłowa i ustno-gardłowa, i-gel, maska krtaniowa, intubacja",
            "Wentylacja usta-usta, przez maskę i workiem samorozprężalnym z widoczną pracą klatki piersiowej",
            "Wyczuwalne, regulowane tętno (0 / 70 / 120/min) na obu rękach",
            "Wbudowany głośnik — odgłosy oddechu i dźwięki scenariusza",
            "Trzy rany z zewnętrznym źródłem krwi: otwarte złamanie kości udowej (staza), rana postrzałowa pachwiny (packing), rana cięta ramienia (ucisk / opatrunek)",
            "Punkty wkłuć obwodowych (PVK) na przedramionach i grzbietach dłoni",
            "Wyjmowane drogi oddechowe (zamek) i otwierana sekcja brzuszna do serwisu",
            "Współpracuje z kamerami termowizyjnymi FLIR / IR",
        ],
        "specs": [
            ("Wzrost", "180 cm"),
            ("Masa", "50 / 60 / 70 / 80 kg (na zamówienie 40–90 kg)"),
            ("Zakres temperatur pracy", "od −30°C do +70°C"),
            ("Materiał", "wytrzymała, ekologiczna skóra, elementy silikonowe, wzmocnione przewody PVC"),
            ("W zestawie", "czarne umundurowanie taktyczne M90, buty na stałe, butelki i przewody do symulacji krwi"),
        ],
        "use": "Zaawansowane szkolenia służb ratowniczych, wojska i personelu medycznego — scenariusze urazowe łączące drogi oddechowe, wentylację i kontrolę krwotoków.",
    },
    {
        "slug": "manekin-pro-military",
        "name": "Manekin ratowniczy PRO MILITARY",
        "short": "Fantom pola walki z raną amputacyjną i masywnym krwotokiem — przygotowuje operatorów na realne obrażenia zanim zobaczą je naprawdę.",
        "features": [
            "Rozległa rana wybuchowa / amputacyjna lewej nogi do treningu zakładania stazy taktycznej",
            "Symulacja masywnego krwotoku z zewnętrznym źródłem krwi",
            "Przegubowa, proporcjonalnie wyważona, anatomicznie poprawna konstrukcja",
            "Możliwość wkłuć obwodowych na przedramionach i grzbiecie dłoni",
            "Współpracuje z kamerami termowizyjnymi FLIR / IR",
            "Zaprojektowany do pracy w trudnych warunkach polowych",
        ],
        "specs": [
            ("Wzrost", "180 cm"),
            ("Masa", "50 / 60 / 70 / 80 kg (na zamówienie 40–90 kg)"),
            ("Zakres temperatur pracy", "od −30°C do +70°C"),
            ("Materiał", "gruba, ekologiczna skóra, trwałe elementy silikonowe"),
            ("W zestawie", "umundurowanie M90, buty na stałe, butelka i przewód przyłączeniowy 1 m"),
        ],
        "use": "Szkolenia wojskowe i taktyczno-medyczne z masywnych krwotoków i amputacji urazowych w warunkach polowych.",
    },
    {
        "slug": "manekin-pro",
        "name": "Manekin ratowniczy PRO",
        "short": "Uniwersalny fantom urazowy z otwartym złamaniem kości udowej — realistyczna masa, przeguby i opcjonalne moduły rozbudowy.",
        "features": [
            "Realistyczna masa i opór — zachowuje się jak osoba nieprzytomna",
            "Otwarte złamanie kości udowej z podłączeniem zewnętrznego źródła krwi",
            "Punkty wkłuć obwodowych na przedramionach i grzbiecie dłoni",
            "Współpracuje z kamerami termowizyjnymi FLIR / IR",
            "Moduły opcjonalne: odgłosy oddechu i obustronne tętno, rana postrzałowa pachwiny, rana cięta ramienia, adapter dróg oddechowych",
        ],
        "specs": [
            ("Wzrost", "180 cm"),
            ("Masa", "50 / 60 / 70 / 80 kg (na zamówienie 40–90 kg)"),
            ("Zakres temperatur pracy", "od −30°C do +70°C"),
            ("Materiał", "gruba, ekologiczna skóra, trwałe elementy silikonowe"),
            ("W zestawie", "odzież taktyczna M90, buty zamocowane na stałe"),
        ],
        "use": "Ratownictwo polowe, taktyczna opieka nad poszkodowanym, ćwiczenia ewakuacji i transportu — straż pożarna, wojsko, ratownictwo medyczne.",
    },
    {
        "slug": "manekin-standard",
        "name": "Manekin ratowniczy Standard",
        "short": "Klasyczny, niezwykle wytrzymały manekin ewakuacyjny do ćwiczeń w dymie, wysokiej temperaturze i na wodzie. Wersja dorosła i dziecięca.",
        "features": [
            "Przegubowy i proporcjonalnie wyważony (anatomicznie poprawny)",
            "Zachowuje się jak osoba nieprzytomna",
            "Bardzo dobrze widoczny w kamerach termowizyjnych (FLIR / IR)",
            "Wytrzymuje bardzo wysokie temperatury — testy ogniowe wg EN ISO 6941 i FAR 25.853b, certyfikat TÜV",
            "Gruba, ekologiczna skóra, podwójne szwy i wzmocnione punkty przeciążeń",
            "W zestawie kombinezon ochronny i buty na stałe",
        ],
        "specs": [
            ("Wersja dorosła (nr art. 15-9181)", "wzrost 180 cm; masa 50 / 60 / 70 / 80 kg (na zamówienie 40–90 kg); kolor czarny"),
            ("Wersja dziecięca (nr art. 15-9183)", "wzrost 100 cm; masa 15 kg — odpowiednik ok. 3-letniego dziecka; kolor czarny"),
            ("Akcesoria", "torba transportowa ze wzmocnionego PVC (nr art. 15-5150)"),
        ],
        "use": "Przeszukiwanie pomieszczeń w dymie i wysokiej temperaturze, ratownictwo wodne, wypadki komunikacyjne (ewakuacja i stabilizacja), ćwiczenia z termowizją, ewakuacje budynków, ratownictwo wysokościowe, nauka technik podnoszenia w ochronie zdrowia.",
    },
    {
        "slug": "symulatory-ran",
        "name": "Symulatory ran",
        "short": "Bardzo realistyczne symulatory obrażeń do nauki kontroli krwotoków — staza, packing, opatrunek uciskowy. Jasny i ciemny odcień skóry.",
        "features": [
            "Zaawansowany materiał odwzorowuje opór tkanek miękkich i reakcję mięśni",
            "Realistyczna geometria ran: nieregularne kanały i ukryte punkty krwawienia",
            "Złączki 6 mm do podłączenia zewnętrznego źródła krwi",
            "Trwały silikon przeznaczony do wielokrotnego użytku",
            "Warianty: SRP Tourniquet Trainer (ramię z raną masywną, 80 × 23 × 12 cm, nr art. 16-1010 / 16-1010-DK), symulator rany postrzałowej (15,3 × 12,5 × 8 cm, nr art. 16-1000 / 16-1000-DK), symulator rany kłutej (nr art. 16-1001 / 16-1001-DK), nakładki ran — otwarte złamanie uda (15-4100) i rana cięta (15-4101 / 15-4101-DK)",
            "Akcesoria: krew symulacyjna (także zapachowa), strzykawki ciśnieniowe 2000 ml, butelki 1000 ml, przewody PVC 1–50 m, gaza do packingu, stazy CAT Gen 7 i SAM XT",
        ],
        "specs": [
            ("Odcienie skóry", "jasny i ciemny"),
            ("Materiał", "trwały silikon o wysokiej odporności na wielokrotne użycie"),
        ],
        "use": "Kursy kontroli krwotoków (Stop the Bleed), szkolenia wojskowe, medyczne i służb ratowniczych.",
    },
    {
        "slug": "manekin-rko",
        "name": "Manekin ratowniczy z funkcją RKO",
        "short": "Fantom terenowy łączący realistyczną ewakuację z pełnowartościową resuscytacją — zgodny z systemem ShockLink™ do ćwiczeń z prawdziwym defibrylatorem.",
        "features": [
            "Zintegrowana, wysokiej jakości funkcja RKO (uciśnięcia i wentylacja)",
            "Przegubowy i wyważony jak prawdziwy człowiek; zachowuje się jak osoba nieprzytomna",
            "Zgodność z ShockLink™ — bezpieczny trening z użyciem rzeczywistego defibrylatora",
            "Certyfikat TÜV, podwójne szwy, wzmocnione punkty przeciążeń",
            "Model 15-9181HLRI dodatkowo: intubacja przez usta i nos, wymienne oczy o różnej wielkości źrenic (NATO Stock No 6910-64-000-7335)",
        ],
        "specs": [
            ("Wzrost", "ok. 180 cm"),
            ("Masa", "ok. 45 kg"),
            ("Modele", "15-9181HLR (RKO) oraz 15-9181HLRI (RKO + intubacja)"),
            ("Materiał", "gruba, ekologiczna skóra"),
            ("W zestawie", "kombinezon ochronny i buty na stałe"),
            ("Opcje", "ramiona do wkłuć obwodowych, system ShockLink"),
        ],
        "use": "Ćwiczenia łączące ewakuację poszkodowanego z natychmiastową resuscytacją — straż pożarna, ratownictwo medyczne, zakłady przemysłowe.",
    },
    {
        "slug": "manekin-wodny-rko",
        "name": "Manekin do ratownictwa wodnego z funkcją RKO",
        "short": "Umożliwia wdechy ratownicze i uciśnięcia klatki piersiowej bezpośrednio w środowisku wodnym. Realistyczna pozycja pływania.",
        "features": [
            "Wentylacja i uciśnięcia klatki piersiowej możliwe w wodzie",
            "Przegubowa konstrukcja — zachowuje się jak osoba nieprzytomna",
            "Realistyczne unoszenie klatki piersiowej przy wdechach",
            "Realistyczna pozycja pływania na powierzchni wody",
            "Wymienne drogi oddechowe/płuca i część twarzowa",
            "Odblaski z przodu i z tyłu, D-ring na nodze do zabezpieczenia na wodzie płynącej",
        ],
        "specs": [
            ("Długość", "180 cm"),
            ("Masa", "50 kg (40 kg na sucho)"),
            ("Materiał", "wzmocnione PVC, podwójne szwy"),
            ("Numery", "nr art. 15-9161FH, NATO Stock No 6910-64-000-5406"),
        ],
        "use": "Ratownictwo wodne powierzchniowe i lodowe, szkolenia ratowników na basenach i kąpieliskach, ćwiczenia dekontaminacji.",
    },
    {
        "slug": "manekiny-ratownictwa-wodnego",
        "name": "Manekiny do ratownictwa wodnego",
        "short": "Wariant pływający (dorosły) i tonący (dziecięcy) do ćwiczeń powierzchniowych, lodowych i nurkowych.",
        "features": [
            "Model dorosły pływający (nr art. 15-9161F): 180 cm, ok. 50 kg (40 kg na sucho), czarny z żółtą głową, realistyczna pozycja pływania, możliwość podgrzania do 65°C do ćwiczeń z termowizją, punkty kotwiczenia na wodzie płynącej",
            "Model dziecięcy tonący (nr art. 15-9161SB): ok. 100 cm, 20 kg (18 kg na sucho), żółty, przeznaczony do opadania na dno — ratownictwo nurkowe i baseny",
            "Przegubowe konstrukcje, podwójne szwy, wzmocnione punkty przeciążeń, odblaski z przodu i z tyłu",
        ],
        "specs": [
            ("Materiał", "wzmocnione (pancerne) PVC"),
            ("Akcesoria", "torba transportowo-magazynowa ze wzmocnionego PVC (nr art. 15-5150)"),
        ],
        "use": "Ratownictwo wodne i lodowe, ćwiczenia powierzchniowe, ratownictwo nurkowe, szkolenia ratowników basenowych.",
    },
    {
        "slug": "manekin-bariatryczny",
        "name": "Manekin bariatryczny",
        "short": "Fantom o masie 100–160 kg do nauki technik podnoszenia i ewakuacji osób o dużej masie ciała.",
        "features": [
            "Przegubowy i proporcjonalnie wyważony (anatomicznie poprawny)",
            "Zachowuje się jak osoba nieprzytomna",
            "Gruba, ekologiczna skóra; podwójne szwy i wzmocnione punkty przeciążeń",
            "Odporny na bardzo wysokie temperatury — testy ogniowe EN ISO 6941 i FAR 25.853b, certyfikat TÜV",
        ],
        "specs": [
            ("Nr art.", "15-9171"),
            ("Wzrost", "ok. 180 cm"),
            ("Masa", "100–160 kg (do wyboru)"),
            ("Kolor", "czarny lub naturalna skóra"),
            ("W zestawie", "spodnie, koszula, buty na stałe"),
        ],
        "use": "Nauka ergonomii i technik podnoszenia, ewakuacja osób bariatrycznych — straż pożarna, ratownictwo medyczne, szpitale i opieka zdrowotna.",
    },
    {
        "slug": "manekiny-pozarowe",
        "name": "Manekiny pożarowe",
        "short": "Manekiny i akcesoria do ćwiczeń gaszenia odzieży palącej się na człowieku — wielokrotnego użytku, bez substancji toksycznych.",
        "features": [
            "SRP Manekin pożarowy (nr art. 15-9281): ok. 150 cm, ok. 10 kg; tkanina ognioodporna, przód wzmocniony podwójną warstwą z chemicznie utwardzanego włókna E-glass, wodoodporny tył, niepalne wypełnienie",
            "SRP Poduszka pożarowa (nr art. 15-9982): ok. 50 × 50 cm (możliwe inne wymiary), ok. 2 kg, laminowana tkanina z włókna szklanego",
            "Koce gaśnicze (nr art. 15-9289): 120 × 180 cm, na zamówienie do 54 m²",
            "Torba transportowa (nr art. 15-9281B)",
            "Bez substancji toksycznych i metali ciężkich; konstrukcja do wielokrotnych podpaleń w warunkach kontrolowanych",
        ],
        "specs": [
            ("Rozpalanie", "na zewnątrz: 50% podpałka płynna + 50% denaturat; w pomieszczeniach: sam denaturat"),
        ],
        "use": "Ćwiczenia gaszenia odzieży metodą tłumienia — straż pożarna, przemysł, ośrodki szkoleniowe.",
    },
    {
        "slug": "symulacja-medyczna",
        "name": "Symulacja medyczna",
        "short": "Trenażery procedur: wkłucia obwodowe i odbarczenie odmy prężnej.",
        "features": [
            "SRP PVK Patch (nr art. 16-1300): wielorazowa silikonowa nakładka do nauki kaniulacji żył obwodowych; 10 × 7 cm; zintegrowana sztuczna żyła z ochroną przed przekłuciem; paski rzepowe do montażu na ramieniu lub manekinie; w zestawie strzykawka 10 ml; silikon klasy medycznej",
            "SRP TraumaThorax Box (nr art. 16-1400): trenażer odbarczania odmy (nakłucie ratunkowe / torakotomia); 17 × 12 × 11 cm; słyszalny syk powietrza przy poprawnym wykonaniu; szybki reset zwykłym balonem; w zestawie moduł klatki i 15 balonów",
            "Moduły Thorax 3-pak (nr art. 16-1401): wymienne moduły silikonowe z wbudowanymi żebrami — palpacyjne wyznaczanie miejsca wkłucia",
        ],
        "specs": [
            ("Produkcja", "Szwecja"),
        ],
        "use": "Szkolenia przedszpitalne i kliniczne, cywilne i wojskowe — nauka wkłuć obwodowych i odbarczania odmy prężnej.",
    },
    {
        "slug": "pozostale-produkty",
        "name": "Pozostałe produkty",
        "short": "Akcesoria i uzupełnienie oferty: krew symulacyjna, stazy, materiały do packingu, torby transportowe oraz produkty partnerów.",
        "features": [
            "Krew symulacyjna — standardowa i zapachowa",
            "Stazy taktyczne CAT Gen 7 i SAM XT",
            "Gaza do packingu ran, strzykawki ciśnieniowe, butelki, przewody PVC",
            "Torby transportowe i magazynowe ze wzmocnionego PVC",
            "Produkty firm partnerskich z zakresu symulacji medycznej i defibrylacji — zapytaj o dostępność w Polsce",
        ],
        "specs": [],
        "use": "Uzupełnienie wyposażenia ośrodków szkoleniowych i instruktorów.",
    },
]

# ---------------------------------------------------------------- szkolenia
# międzynarodowe piktogramy (inline SVG, kanoniczne kolory znaków bezpieczeństwa)
ICO_STOP_BLEED = """<svg viewBox="0 0 48 48" role="img" aria-label="Kontrola krwotoków"><polygon points="15,2 33,2 46,15 46,33 33,46 15,46 2,33 2,15" fill="#c8102e"/><path d="M24 11c4.2 6 8 10.4 8 15.2A8 8 0 1 1 16 26.2C16 21.4 19.8 17 24 11z" fill="#fff"/></svg>"""
ICO_AED = """<svg viewBox="0 0 48 48" role="img" aria-label="RKO / AED"><rect width="48" height="48" rx="8" fill="#009639"/><path d="M24 40c-8.5-6.2-14-11.4-14-18.2C10 17 13.7 13 18.4 13c2.3 0 4.4 1 5.6 2.7A6.9 6.9 0 0 1 29.6 13C34.3 13 38 17 38 21.8 38 28.6 32.5 33.8 24 40z" fill="#fff"/><path d="M26.5 15.5 19 27h5l-3.5 10L30 24.5h-5l3.5-9z" fill="#009639"/></svg>"""
ICO_STAR_LIFE = """<svg viewBox="0 0 48 48" role="img" aria-label="Służby ratownicze"><rect width="48" height="48" rx="8" fill="#0057a8"/><g fill="#fff"><rect x="21" y="5" width="6" height="38" rx="1.5"/><rect x="21" y="5" width="6" height="38" rx="1.5" transform="rotate(60 24 24)"/><rect x="21" y="5" width="6" height="38" rx="1.5" transform="rotate(120 24 24)"/></g><circle cx="24" cy="24" r="6.5" fill="#0057a8"/><circle cx="24" cy="24" r="4.5" fill="#fff"/></svg>"""
ICO_CHILD = """<svg viewBox="0 0 48 48" role="img" aria-label="RKO dzieci"><rect width="48" height="48" rx="8" fill="#009639"/><path d="M19 34c-6-4.4-10-8.2-10-13a6 6 0 0 1 10.4-4A6 6 0 0 1 29.8 21c0 4.8-4.8 8.6-10.8 13z" fill="#fff"/><path d="M34 42c-4.2-3-7-5.7-7-9a4.2 4.2 0 0 1 7.3-2.8A4.2 4.2 0 0 1 41.6 33c0 3.3-3.4 6-7.6 9z" fill="#fff"/></svg>"""
ICO_FIRST_AID = """<svg viewBox="0 0 48 48" role="img" aria-label="Pierwsza pomoc"><rect width="48" height="48" rx="8" fill="#009639"/><path d="M19 9h10v10h10v10H29v10H19V29H9V19h10z" fill="#fff"/></svg>"""
ICO_INSTRUCTOR = """<svg viewBox="0 0 48 48" role="img" aria-label="Kursy instruktorskie"><rect width="48" height="48" rx="8" fill="#0057a8"/><path d="M24 12 4 20l20 8 14-5.6V31h4v-9.4z" fill="#fff"/><path d="M14 27.8V34c0 2.8 4.5 5 10 5s10-2.2 10-5v-6.2l-10 4z" fill="#fff"/></svg>"""
ICO_TECC = """<svg viewBox="0 0 48 48" role="img" aria-label="TECC"><rect width="48" height="48" rx="8" fill="#3d4a3a"/><path d="M24 6l14 5v11c0 9-6 16.4-14 20C16 38.4 10 31 10 22V11z" fill="#fff"/><path d="M21 16h6v5h5v6h-5v5h-6v-5h-5v-6h5z" fill="#3d4a3a"/></svg>"""

COURSES = [
    (ICO_STOP_BLEED, "Stop the Bleed — zatrzymaj krwotok", "Międzynarodowo certyfikowany kurs kontroli krwotoków: staza, packing rany, opatrunek uciskowy. Zajęcia na realistycznych symulatorach ran SRP."),
    (ICO_AED, "RKO osób dorosłych", "Podstawowa resuscytacja krążeniowo-oddechowa z użyciem AED."),
    (ICO_STAR_LIFE, "RKO dla służb i personelu interwencyjnego", "Rozszerzony program dla strażaków, policjantów i ratowników — praca w zespole, scenariusze."),
    (ICO_TECC, "TECC — taktyczna opieka nad poszkodowanym", "Tactical Emergency Casualty Care: postępowanie z poszkodowanym urazowym w środowisku zagrożenia — dla służb mundurowych i zespołów interwencyjnych. Prowadzą instruktorzy z certyfikatem TECC."),
    (ICO_CHILD, "RKO dzieci i wypadki z udziałem dzieci", "Resuscytacja niemowląt i dzieci, postępowanie przy zadławieniu i najczęstszych urazach."),
    (ICO_FIRST_AID, "Pierwsza pomoc S-XABCDE", "Systematyczne badanie i zaopatrywanie poszkodowanego według schematu XABCDE."),
    (ICO_INSTRUCTOR, "Kursy instruktorskie", "Przygotowanie instruktorów RKO (dorośli / dzieci / służby) i pierwszej pomocy — prowadzone przez certyfikowanych wykładowców z doświadczeniem operacyjnym."),
]

# ---------------------------------------------------------------- branże (B2B)
SEGMENTS = [
    {
        "anchor": "straz-pozarna",
        "name": "Straż pożarna (PSP i OSP)",
        "desc": "Przeszukiwanie pomieszczeń w dymie i wysokiej temperaturze, ćwiczenia z termowizją, ewakuacja z budynków i wysokości, wypadki komunikacyjne, gaszenie odzieży palącej się na człowieku.",
        "products": ["manekin-standard", "manekin-rko", "manekiny-pozarowe", "manekin-bariatryczny"],
    },
    {
        "anchor": "wojsko",
        "name": "Wojsko i obrona",
        "desc": "Taktyczna opieka nad poszkodowanym (TCCC), masywne krwotoki i amputacje urazowe, drogi oddechowe w warunkach polowych. Wybrane produkty mają numery magazynowe NATO (NSN) i umundurowanie M90.",
        "products": ["manekin-pro-elite-military", "manekin-pro-military", "symulatory-ran", "symulacja-medyczna"],
    },
    {
        "anchor": "ratownictwo-medyczne",
        "name": "Ratownictwo medyczne i szpitale",
        "desc": "RKO z defibrylatorem (ShockLink™), zabezpieczanie dróg oddechowych, wkłucia obwodowe, odbarczanie odmy, ergonomia podnoszenia pacjentów — także bariatrycznych.",
        "products": ["manekin-rko", "manekin-pro-elite", "symulacja-medyczna", "manekin-bariatryczny"],
    },
    {
        "anchor": "ratownictwo-wodne",
        "name": "Ratownictwo wodne (WOPR, baseny)",
        "desc": "Ratownictwo powierzchniowe i lodowe, ratownictwo nurkowe (wariant tonący), RKO bezpośrednio w wodzie, ćwiczenia na wodzie płynącej.",
        "products": ["manekiny-ratownictwa-wodnego", "manekin-wodny-rko", "manekin-standard"],
    },
    {
        "anchor": "przemysl-bhp",
        "name": "Przemysł i służby BHP",
        "desc": "Zakładowe służby ratownicze i ewakuacyjne: ćwiczenia ewakuacji hal i biurowców, pierwsza pomoc, gaszenie odzieży, scenariusze wypadków przy pracy.",
        "products": ["manekin-standard", "manekiny-pozarowe", "manekin-rko", "symulatory-ran"],
    },
    {
        "anchor": "edukacja",
        "name": "Uczelnie i ośrodki szkoleniowe",
        "desc": "Symulacja medyczna, kursy pierwszej pomocy i kwalifikowanej pierwszej pomocy, kursy instruktorskie — sprzęt odporny na codzienną, intensywną eksploatację.",
        "products": ["symulacja-medyczna", "symulatory-ran", "manekin-pro", "manekin-rko"],
    },
]

# ---------------------------------------------------------------- porównanie modeli
# kolumny: PRO ELITE MILITARY | PRO ELITE | PRO MILITARY | PRO | Standard | z funkcją RKO
COMPARE_COLS = [
    ("manekin-pro-elite-military", "PRO ELITE MILITARY"),
    ("manekin-pro-elite", "PRO ELITE"),
    ("manekin-pro-military", "PRO MILITARY"),
    ("manekin-pro", "PRO"),
    ("manekin-standard", "Standard"),
    ("manekin-rko", "z funkcją RKO"),
]
COMPARE_ROWS = [
    ("Wzrost", ["180 cm", "180 cm", "180 cm", "180 cm", "180 cm (dziecięcy 100 cm)", "ok. 180 cm"]),
    ("Masa", ["50–80 kg (40–90 na zam.)", "50–80 kg (40–90 na zam.)", "50–80 kg (40–90 na zam.)", "50–80 kg (40–90 na zam.)", "50–80 kg / dziecięcy 15 kg", "ok. 45 kg"]),
    ("Rany krwawiące (zewn. źródło krwi)", ["3 (amputacja, postrzał, cięta)", "3 (złamanie uda, postrzał, cięta)", "1 (amputacja urazowa)", "1 (złamanie uda) + moduły opcjonalne", "—", "—"]),
    ("Drogi oddechowe / intubacja", ["tak — pełny symulator", "tak — pełny symulator", "—", "adapter opcjonalny", "—", "model 15-9181HLRI: intubacja"]),
    ("Regulowane tętno (0/70/120)", ["tak, obie ręce", "tak, obie ręce", "—", "moduł opcjonalny", "—", "—"]),
    ("Głośnik (oddech, scenariusz)", ["tak", "tak", "—", "moduł opcjonalny", "—", "—"]),
    ("Wkłucia obwodowe (PVK)", ["tak", "tak", "tak", "tak", "—", "ramiona opcjonalne"]),
    ("Funkcja RKO / defibrylacja", ["—", "—", "—", "—", "—", "tak, zgodny z ShockLink™"]),
    ("Termowizja FLIR / IR", ["tak", "tak", "tak", "tak", "tak", "tak"]),
    ("Testy ogniowe / TÜV", ["—", "—", "—", "—", "EN ISO 6941, FAR 25.853b, TÜV", "TÜV"]),
    ("Typowe zastosowanie", ["TCCC, wojsko, medycyna taktyczna", "służby ratownicze, medycyna, wojsko", "pole walki, masywne krwotoki", "ratownictwo polowe, ewakuacja", "dym, ogień, woda, ewakuacja", "ewakuacja + resuscytacja"]),
]

# ---------------------------------------------------------------- FAQ (B2B)
FAQS = [
    ("Jaki jest czas realizacji zamówienia?",
     "Produkty SRP są wykonywane ręcznie w Szwecji, dlatego termin zależy od konfiguracji i wielkości zamówienia — typowo kilka tygodni. W ofertach i postępowaniach przetargowych podajemy wiążący termin dostawy."),
    ("Czy można zamówić nietypową konfigurację?",
     "Tak. Manekiny dostępne są w masach 40–90 kg na zamówienie, symulatory ran w jasnym i ciemnym odcieniu skóry, a manekin bariatryczny w zakresie 100–160 kg. Dobierzemy konfigurację pod Wasze scenariusze ćwiczeń."),
    ("Jak wygląda gwarancja i serwis?",
     "Manekiny ratownicze objęte są 12-miesięczną gwarancją na wady produkcyjne, wybrane produkty dłuższą — do 20 lat. Zapewniamy obsługę serwisową i części na terenie Polski oraz naprawy pogwarancyjne."),
    ("Czy wspieracie zamówienia publiczne?",
     "Tak — przygotowujemy opisy przedmiotu zamówienia z parametrami technicznymi, dostarczamy certyfikaty (TÜV, testy ogniowe EN ISO 6941 / FAR 25.853b) i utrzymujemy warunki oferty w okresie związania. Zobacz sekcję „Zamówienia publiczne”."),
    ("Czy można zobaczyć i przetestować produkty przed zakupem?",
     "Tak. Organizujemy bezpłatne pokazy w siedzibie klienta — manekiny można wziąć do ręki, przenieść, sprawdzić na własnych noszach i w swoich procedurach. Możliwe są też testy sprzętu przed większym zamówieniem."),
    ("Czy oferujecie leasing lub najem?",
     "Dla instytucji i firm oferujemy finansowanie ratalne, leasing oraz najem długoterminowy [do potwierdzenia z partnerem finansowym]. Napisz — policzymy warianty w wycenie."),
    ("Czy do sprzętu można dokupić szkolenie wdrożeniowe?",
     "Tak — najczęściej wybierany wariant to pakiet: sprzęt + szkolenie instruktorów klienta z jego wykorzystania w scenariuszach. Szkolenia prowadzą certyfikowani instruktorzy z doświadczeniem operacyjnym."),
    ("Czy produkty mają numery magazynowe NATO (NSN)?",
     "Wybrane produkty tak, m.in. manekin z funkcją RKO i intubacją (NSN 6910-64-000-7335) oraz manekin wodny z RKO (NSN 6910-64-000-5406). Producent posiada kod NCAGE: AE82N."),
]

# ---------------------------------------------------------------- strefa wiedzy
ARTICLES = [
    {
        "slug": "jak-wybrac-manekin-ratowniczy",
        "title": "Jak wybrać manekin ratowniczy? Przewodnik dla jednostek i ośrodków",
        "seo_title": "Jak wybrać manekin ratowniczy? Przewodnik",
        "desc": "Pięć pytań przed zakupem manekina ratowniczego: scenariusze, masa, środowisko (woda, ogień), "
                "trwałość i akcesoria. Przewodnik dla jednostek i ośrodków.",
        "lead": "Zakup manekina to inwestycja na lata intensywnej eksploatacji. Oto pięć pytań, które warto sobie zadać przed wyborem modelu — zanim porównacie ceny.",
        "body": """
<h3>1. Do jakich scenariuszy będzie służył?</h3>
<p>Inny sprzęt jest potrzebny do przeszukiwania zadymionych pomieszczeń, inny do taktycznej opieki nad
poszkodowanym, a jeszcze inny do resuscytacji. Jeśli trenujecie głównie ewakuację — kluczowa jest
realistyczna masa, przeguby i wytrzymałość (model Standard). Jeśli scenariusze medyczne — funkcje
takie jak drogi oddechowe, tętno i krwawiące rany (linia PRO / PRO ELITE).</p>
<h3>2. Jaka masa?</h3>
<p>Realizm rośnie z masą, ale rośnie też obciążenie ćwiczących. W praktyce jednostki wybierają
60–70 kg do ćwiczeń zespołowych, a 80 kg do egzaminów i selekcji. Masy niestandardowe (40–90 kg)
dostępne są na zamówienie — warto dobrać je do rzeczywistych procedur, np. pracy w rocie.</p>
<h3>3. W jakim środowisku?</h3>
<p>Do wody przeznaczone są wyłącznie modele z wzmocnionego PVC (pływające lub tonące). Do ćwiczeń
z ogniem i wysoką temperaturą — modele testowane ogniowo (EN ISO 6941, FAR 25.853b, certyfikat TÜV).
Manekiny skórzane sprawdzą się wszędzie tam, gdzie liczy się realizm dotyku i termowizja.</p>
<h3>4. Ile wytrzyma?</h3>
<p>W kalkulacji opłacalności liczy się nie cena zakupu, lecz koszt na jedno ćwiczenie. Ręcznie szyte
manekiny z grubej skóry, z podwójnymi szwami i wzmocnionymi punktami przeciążeń, pracują w jednostkach
codziennie przez wiele lat — a serwis i części dostępne są w Polsce.</p>
<h3>5. Co poza manekinem?</h3>
<p>Zaplanujcie od razu akcesoria: torbę transportową, krew symulacyjną i materiały do packingu przy
scenariuszach urazowych, a przy resuscytacji — system ShockLink™ do ćwiczeń z prawdziwym
defibrylatorem. Pakiet sprzęt + szkolenie wdrożeniowe daje najszybszy zwrot z inwestycji.</p>
<p><strong>Nie wiesz, który model wybrać?</strong> Zobacz <a href="../porownanie-manekinow.html">porównanie
modeli</a> albo <a href="../zapytanie-ofertowe.html">umów bezpłatny pokaz</a> — przywieziemy sprzęt do Twojej jednostki.</p>
""",
    },
    {
        "slug": "scenariusze-cwiczen-z-manekinem",
        "title": "6 scenariuszy ćwiczeń, które wyciągną maksimum z manekina ratowniczego",
        "seo_title": "6 scenariuszy ćwiczeń z manekinem ratowniczym",
        "desc": "Sześć scenariuszy ćwiczeń z manekinem ratowniczym: przeszukiwanie z termowizją, ewakuacja "
                "z wysokości, wypadek drogowy, RKO, kąpielisko i wypadek masowy.",
        "lead": "Manekin to nie rekwizyt do przenoszenia z punktu A do B. Dobrze zaprojektowany scenariusz zmienia go w pełnoprawnego „poszkodowanego”. Sześć sprawdzonych pomysłów.",
        "body": """
<h3>1. Przeszukiwanie w zerowej widoczności z termowizją</h3>
<p>Manekin skórzany bardzo dobrze odwzorowuje sygnaturę cieplną człowieka w kamerze FLIR. Ukryjcie go
w zadymionym pomieszczeniu w nietypowej pozycji (za drzwiami, pod oknem) i ćwiczcie systematykę
przeszukiwania oraz komunikację roty.</p>
<h3>2. Ewakuacja z wysokości</h3>
<p>Pełna masa i ruchome przeguby wymuszają poprawną pracę z noszami, trójkątem ewakuacyjnym
i technikami linowymi — błędy w mocowaniu widać natychmiast.</p>
<h3>3. Wypadek komunikacyjny</h3>
<p>Manekin w roli kierowcy: stabilizacja odcinka szyjnego, wydobycie z pojazdu, przekazanie zespołowi
medycznemu. Wariant zaawansowany: model PRO z krwawiącym złamaniem uda — priorytety się zmieniają.</p>
<h3>4. Wydobycie + natychmiastowa resuscytacja</h3>
<p>Model z funkcją RKO pozwala połączyć ewakuację z resuscytacją bez zmiany „poszkodowanego”:
po wyniesieniu ze strefy zespół od razu przechodzi do uciśnięć i wentylacji, a z systemem ShockLink™ —
do defibrylacji prawdziwym urządzeniem.</p>
<h3>5. Kąpielisko / basen</h3>
<p>Wariant tonący do ratownictwa nurkowego i pływający do powierzchniowego. Manekin wodny z RKO
umożliwia wdechy ratownicze już w wodzie — najtrudniejszy i najczęściej pomijany element szkolenia.</p>
<h3>6. Masowy wypadek w zakładzie</h3>
<p>Kilka manekinów + symulatory ran = segregacja (triage) pod presją czasu. Ukryte punkty krwawienia
w symulatorach wymuszają pełne badanie urazowe, a nie „odhaczanie” poszkodowanych.</p>
<p>Po każdym scenariuszu — krótki debriefing: co widzieliśmy, co zrobiliśmy, co zmieniamy. To tam
powstaje realna wartość szkoleniowa. <a href="../szkolenia.html">Możemy poprowadzić takie ćwiczenia
u Was</a> — z naszym sprzętem i instruktorami.</p>
""",
    },
    {
        "slug": "kontrola-krwotokow-stop-the-bleed",
        "title": "Kontrola krwotoków: dlaczego „Stop the Bleed” powinno być standardem, nie dodatkiem",
        "seo_title": "Stop the Bleed: kontrola krwotoków w szkoleniu",
        "desc": "Dlaczego kontrola krwotoków powinna być standardem szkoleń: ucisk, opatrunek, staza, packing "
                "rany. Jak zorganizować kurs Stop the Bleed z symulatorami ran.",
        "lead": "Masywny krwotok potrafi zabić w kilka minut — zanim na miejsce dotrze zespół ratownictwa medycznego. Umiejętność jego zatrzymania to najbardziej „opłacalna” kompetencja pierwszej pomocy.",
        "body": """
<h3>Trzy techniki, które ratują życie</h3>
<p><strong>Ucisk bezpośredni</strong> — pierwsza i najczęściej wystarczająca reakcja.
<strong>Opatrunek uciskowy</strong> — gdy trzeba zwolnić ręce. <strong>Staza taktyczna</strong> —
przy masywnych krwotokach z kończyn; poprawnie założona staza to kwestia sekund, ale wymaga
przećwiczenia pod obciążeniem stresem. Do ran pachwiny i szyi pozostaje
<strong>packing rany</strong> — technika, której nie da się nauczyć z prezentacji.</p>
<h3>Dlaczego symulator, a nie „na sucho”?</h3>
<p>Różnica między wiedzą a umiejętnością powstaje w rękach. Realistyczny symulator odwzorowuje opór
tkanek, nieregularne kanały rany i ukryte punkty krwawienia — kursant czuje, kiedy packing jest
skuteczny, bo krwawienie (z zewnętrznego źródła) realnie się zatrzymuje. To zupełnie inny poziom
ćwiczenia niż zwijanie bandaża na zdrowym przedramieniu.</p>
<h3>Jak zorganizować szkolenie w organizacji?</h3>
<p>Optymalny format to 2–4 godziny w małych grupach, z rotacją na stanowiskach: staza, packing,
opatrunek uciskowy. Sprzęt: symulatory ran (jasny i ciemny odcień skóry), stazy treningowe CAT/SAM,
gaza do packingu i krew symulacyjna. Kurs kończy się scenariuszem łączonym pod presją czasu.</p>
<p>Prowadzimy <a href="../szkolenia.html">certyfikowane kursy Stop the Bleed</a> i dostarczamy
<a href="../produkty/symulatory-ran.html">kompletne zestawy symulatorów</a> dla instruktorów
i ośrodków szkoleniowych.</p>
""",
    },
]

# ---------------------------------------------------------------- opinie klientów
# UWAGA: wpisuj wyłącznie PRAWDZIWE opinie za zgodą autora (fikcyjne recenzje to
# nieuczciwa praktyka rynkowa). Format:
# TESTIMONIALS = [
#     ("Treść opinii…", "Imię Nazwisko / stopień", "Jednostka / organizacja"),
# ]
TESTIMONIALS = [
    (o.get("tresc", ""), o.get("autor", ""), o.get("organizacja", ""))
    for o in (SITE.get("opinie", {}) or {}).get("wpisy", [])
    if o.get("tresc")
]

# „Meldunek: fantomy w służbie” — dziennik wdrożeń (anonimizowany, bez nazw odbiorców,
# więc nie wymaga zgód na referencję). Źródło: data/site.json → meldunek.wpisy
# (edytowalne przez n8n po zamknięciu dostawy w CRM).
DEPLOYMENTS = [
    (w.get("data", ""), w.get("model", ""), w.get("odbiorca", ""), w.get("region", ""), w.get("logo"))
    for w in (SITE.get("meldunek", {}) or {}).get("wpisy", [])
    if w.get("model")
]

# ---------------------------------------------------------------- szablon
def esc(s): return html.escape(s, quote=False)

def placeholder(label, cls="ph"):
    return f'<div class="{cls}"><span>📷 {esc(label)}</span></div>'

# --- pobrane materiały (img/) ---------------------------------------------
IMG_DIR = os.path.join(ROOT, "img")
import re as _re

def _files(prefix, exts):
    if not os.path.isdir(IMG_DIR):
        return []
    rx = _re.compile(rf"^{_re.escape(prefix)}-\d+\.({exts})$", _re.I)
    return sorted(f for f in os.listdir(IMG_DIR) if rx.match(f))

def images_for(prefix):
    return _files(prefix, "jpg|jpeg|png|webp|gif")

def videos_for(prefix):
    return _files(prefix, "mp4|webm")

def _size(f):
    return os.path.getsize(os.path.join(IMG_DIR, f))

def main_image(prefix):
    imgs = images_for(prefix)
    return max(imgs, key=_size) if imgs else None

def gallery_images(prefix, limit=6):
    """zdjęcia poza głównym; pomija miniatury (<40 KB)"""
    main = main_image(prefix)
    return [f for f in images_for(prefix) if f != main and _size(f) > 40_000][:limit]

def thumb_path(f):
    """miniatura 640 px z img/thumb/ (zawsze .jpg); None gdy brak"""
    t = os.path.splitext(f)[0] + ".jpg"
    return t if os.path.exists(os.path.join(IMG_DIR, "thumb", t)) else None

def pic(prefix, label, cls="ph", depth=0, thumb=False):
    """zdjęcie z img/ (największe dla prefiksu) albo placeholder; prefix może być
    też konkretną nazwą pliku (z kropką). thumb=True -> miniatura do kart/kafli."""
    p = "../" * depth
    f = prefix if (prefix and "." in prefix) else (main_image(prefix) if prefix else None)
    if f and os.path.exists(os.path.join(IMG_DIR, f)):
        t = thumb_path(f) if thumb else None
        src = f"{p}img/thumb/{t}" if t else f"{p}img/{f}"
        return (f'<div class="{cls} has-img"><img src="{src}" alt="{esc(label)}" loading="lazy" decoding="async"></div>')
    return placeholder(label, cls)

DESC_DOMYSLNY = ("Szwedzkie manekiny ratownicze i symulatory ran SRP — wyłączny dystrybutor w Polsce. "
                 "Sprzęt treningowy dla straży pożarnej, wojska, ratownictwa medycznego i wodnego.")

# Unikalne opisy meta (do 160 znaków) dla stron, które nie przekazują własnego opisu do head().
# Podstawiane w seo_postprocess() po ścieżce pliku — dzięki temu nie trzeba ruszać każdej funkcji strony.
SEO_OPISY = {
    "index.html": "Manekiny ratownicze i symulatory ran SRP ze Szwecji. Wyłączny dystrybutor w Polsce: "
                  "sprzedaż, pokazy, serwis i szkolenia dla straży, wojska i ratownictwa.",
    "produkty/index.html": "Katalog manekinów ratowniczych SRP: modele Standard, PRO, RKO, wodne i ogniowe "
                           "oraz symulatory ran. Parametry, masy, zastosowania i wycena.",
    "dla-kogo.html": "Dobór manekinów treningowych dla straży pożarnej, wojska, ratownictwa medycznego "
                     "i wodnego, szpitali i ośrodków szkoleniowych. Polecane modele SRP.",
    "porownanie-manekinow.html": "Porównanie manekinów ratowniczych SRP: masa, materiał, funkcje RKO, praca "
                                 "w wodzie i ogniu. Tabela pomaga wybrać model do Waszych ćwiczeń.",
    "zamowienia-publiczne.html": "Manekiny ratownicze w zamówieniach publicznych: opis przedmiotu zamówienia, "
                                 "kody CPV i NATO, certyfikaty oraz wsparcie w postępowaniu.",
    "do-pobrania.html": "Karty katalogowe, certyfikaty i materiały informacyjne o manekinach ratowniczych "
                        "i symulatorach ran SRP do pobrania.",
    "faq.html": "Najczęstsze pytania o zakup manekinów ratowniczych SRP: ceny, czas dostawy, gwarancja, "
                "serwis, masy niestandardowe i pokazy sprzętu.",
    "wiedza/index.html": "Strefa wiedzy SRP Polska: jak wybrać manekin ratowniczy, scenariusze ćwiczeń, "
                         "kontrola krwotoków. Artykuły dla instruktorów i jednostek.",
    "szkolenia.html": "Szkolenia RKO, pierwszej pomocy, Stop the Bleed i TECC z użyciem manekinów "
                      "i symulatorów ran SRP. Certyfikowani instruktorzy, zajęcia u klienta.",
    "warunki-zakupu.html": "Warunki zakupu sprzętu SRP: zamówienie, płatność, czas i koszt dostawy, "
                           "gwarancja i serwis w Polsce. Informacje dla firm i instytucji.",
    "zapytanie-ofertowe.html": "Zapytanie ofertowe na manekiny ratownicze, symulatory ran i szkolenia SRP. "
                               "Umów bezpłatny pokaz sprzętu. Odpowiadamy w jeden dzień roboczy.",
    "o-nas.html": "SRP Polska (TURBOMEDIC Sp. z o.o.) — wyłączny dystrybutor szwedzkich manekinów "
                  "ratowniczych SRP. Doradztwo, sprzedaż, serwis i szkolenia w całej Polsce.",
    "aktualnosci.html": "Aktualności SRP Polska: wdrożenia manekinów ratowniczych, szkolenia, pokazy "
                        "i nowości w ofercie szwedzkiego producenta SRP.",
    "kontakt.html": "Kontakt z SRP Polska: telefon +48 660 408 679, e-mail kontakt@srp-polska.pl. "
                    "Wyłączny dystrybutor manekinów ratowniczych SRP, Wrocław.",
    "polityka-prywatnosci.html": "Polityka prywatności serwisu srp-polska.pl: administrator danych, cele "
                                 "i podstawy przetwarzania, prawa osób, brak plików cookie.",
    "404.html": "Strona nie istnieje. Przejdź do katalogu manekinów ratowniczych SRP lub na stronę "
                "główną SRP Polska.",
}

def head(title, depth=0, desc=None):
    p = "../" * depth
    d = " ".join((desc or DESC_DOMYSLNY).split())[:300]
    return f"""<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} | {BRAND}</title>
<meta name="description" content="{esc(d)}">
<link rel="icon" type="image/svg+xml" href="{p}img/srp-logo.svg">
<meta property="og:title" content="{esc(title)} | {BRAND}">
<meta property="og:description" content="{esc(d)}">
<meta property="og:image" content="{BASE_URL}/img/home-01.jpg">
<meta property="og:type" content="website">
<meta property="og:locale" content="pl_PL">
<meta name="twitter:card" content="summary_large_image">
<link rel="stylesheet" href="{p}css/style.css">
</head>
<body>
<header class="topbar">
  <div class="wrap nav-wrap">
    <a class="logo" href="{p}index.html"><img class="logo-img" src="{p}img/srp-logo.svg" alt="SRP — Svenska Räddningsprodukter"></a>
    <input type="checkbox" id="nav-toggle" hidden><label for="nav-toggle" class="burger" aria-label="Menu">☰</label>
    <nav>
      <a href="{p}produkty/index.html">Produkty</a>
      <a href="{p}dla-kogo.html">Dla kogo</a>
      <a href="{p}szkolenia.html">Szkolenia</a>
      <a href="{p}index.html#meldunek">Meldunek</a>
      <a href="{p}zamowienia-publiczne.html">Przetargi</a>
      <a href="{p}wiedza/index.html">Wiedza</a>
      <a href="{p}o-nas.html">O nas</a>
      <a href="{p}kontakt.html">Kontakt</a>
      <a class="nav-cta" href="{p}zapytanie-ofertowe.html">Umów pokaz / wycena</a>
    </nav>
  </div>
</header>
"""

def footer(depth=0):
    p = "../" * depth
    return f"""
<footer>
  <div class="wrap foot-grid">
    <div>
      <h4>{BRAND}</h4>
      <p>{DISTRIBUTOR}</p>
      <p class="rejestr">{DANE_REJESTROWE}</p>
      <p><a href="tel:{PHONE.replace(' ', '')}">{PHONE}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      <p><a href="{p}polityka-prywatnosci.html">Polityka prywatności</a></p>
    </div>
    <div>
      <h4>Producent</h4>
      <p>Svenska Räddningsprodukter AB<br>Bergslagsgatan 1F<br>SE-733 31 Sala, Szwecja</p>
      <p>Ręczna produkcja w Szwecji od 2009 r.</p>
    </div>
    <div>
      <h4>Na skróty</h4>
      <p><a href="{p}produkty/index.html">Produkty</a><br>
      <a href="{p}porownanie-manekinow.html">Porównanie modeli</a><br>
      <a href="{p}dla-kogo.html">Rozwiązania dla branż</a><br>
      <a href="{p}index.html#meldunek">Meldunek: fantomy w służbie</a><br>
      <a href="{p}zamowienia-publiczne.html">Zamówienia publiczne</a><br>
      <a href="{p}do-pobrania.html">Do pobrania</a><br>
      <a href="{p}wiedza/index.html">Strefa wiedzy</a><br>
      <a href="{p}faq.html">Pytania i odpowiedzi</a><br>
      <a href="{p}szkolenia.html">Szkolenia</a><br>
      <a href="{p}zapytanie-ofertowe.html">Zapytanie ofertowe</a><br>
      <a href="{p}warunki-zakupu.html">Warunki zakupu</a><br>
      <a href="{p}aktualnosci.html">Aktualności</a><br>
      <a href="{p}kontakt.html">Kontakt</a></p>
    </div>
  </div>
  <div class="wrap copyright">© {BRAND}. Produkty SRP® są znakiem towarowym Svenska Räddningsprodukter AB. MADE IN SWEDEN.</div>
</footer>
<script>
/* wysyłka formularzy do webhooka n8n (bez przeładowania strony) */
(function(){{
  document.querySelectorAll('form[data-lead-form="1"]').forEach(function(f){{
    f.addEventListener('submit', function(ev){{
      ev.preventDefault();
      var btn=f.querySelector('button[type=submit]'), old=btn?btn.innerHTML:'';
      if(btn){{ btn.disabled=true; btn.innerHTML='Wysyłanie…'; }}
      var fd=new FormData(f), data={{}};
      fd.forEach(function(v,k){{ data[k]= data[k] ? [].concat(data[k],v) : v; }});
      data._strona=location.pathname; data._czas=new Date().toISOString();
      fetch(f.action,{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify(data)}})
        .then(function(r){{ if(!r.ok) throw 0;
          f.innerHTML = (data.typ==='newsletter')
            ? '<div class="form-ok"><strong>Dziękujemy — jesteś na liście.</strong><p>Materiały wysyłamy najwyżej raz w miesiącu. Zgodę możesz wycofać w każdej chwili.</p></div>'
            : '<div class="form-ok"><strong>Dziękujemy — zapytanie dotarło.</strong><p>Odpowiadamy zwykle w ciągu jednego dnia roboczego.</p></div>'; }})
        .catch(function(){{ if(btn){{ btn.disabled=false; btn.innerHTML=old; }}
          alert('Nie udało się wysłać. Napisz na {EMAIL} lub zadzwoń: {PHONE}.'); }});
    }});
  }});
}})();
</script>
</body>
</html>"""

def btn(href, label):
    return f'<a class="btn" href="{href}">{esc(label)} <span class="arr">→</span></a>'

def seo_postprocess(path, html_out):
    """Adres kanoniczny, og:url, unikalny opis meta wg SEO_OPISY, noindex dla strony 404."""
    url = BASE_URL + "/" + ("" if path == "index.html" else path)
    if path == "404.html":
        extra = '<meta name="robots" content="noindex">\n'
    else:
        extra = f'<link rel="canonical" href="{url}">\n<meta property="og:url" content="{url}">\n'
    html_out = html_out.replace("</head>", extra + "</head>", 1)
    d = SEO_OPISY.get(path)
    if d:
        d = esc(" ".join(d.split()))
        html_out = _re.sub(r'(<meta name="description" content=")[^"]*(")',
                           lambda m: m.group(1) + d + m.group(2), html_out, count=1)
        html_out = _re.sub(r'(<meta property="og:description" content=")[^"]*(")',
                           lambda m: m.group(1) + d + m.group(2), html_out, count=1)
    return html_out

def write(path, content):
    if path.endswith(".html"):
        content = seo_postprocess(path, content)
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("✓", path)

def render_meldunek_pusty():
    """Meldunek bez wpisów — kotwica #meldunek musi istnieć, bo linkuje do niej nawigacja i stopka.
    Zero danych przykładowych: uczciwa informacja, kiedy pojawią się wpisy."""
    return '''
    <div class="meldunek" id="meldunek">
      <div class="m-head"><span class="m-dot"></span> MELDUNEK: FANTOMY W SŁUŻBIE</div>
      <div class="m-foot">Dziennik dostaw w Polsce. Wpisy publikujemy po każdej dostawie i wyłącznie za zgodą jednostki
      — bez nazw własnych, z modelem, typem odbiorcy i regionem. Referencje udostępniamy na życzenie:
      <a href="kontakt.html" style="color:#e6e6e6">napisz do nas</a>.</div>
    </div>'''

def render_meldunek(deps):
    """sekcja „Meldunek: fantomy w służbie” — licznik + karuzela wpisów"""
    def odm(n, one, few, many):
        if n == 1: return one
        if 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14: return few
        return many
    n_units = len(deps)
    n_regions = len({d[3] for d in deps})
    w_odm = odm(n_units, "wdrożenie", "wdrożenia", "wdrożeń")
    r_odm = odm(n_regions, "region", "regiony", "regionów")
    shield = ('<svg viewBox="0 0 48 48" aria-hidden="true"><path d="M24 6l14 5v11c0 9-6 16.4-14 20'
              'C16 38.4 10 31 10 22V11z" fill="none" stroke="#4a4a4a" stroke-width="2.5"/>'
              '<path d="M21 17h6v4h4v6h-4v4h-6v-4h-4v-6h4z" fill="#4a4a4a"/></svg>')
    def d_logo(entry):
        logo = entry[4] if len(entry) > 4 and entry[4] else None
        if logo and os.path.exists(os.path.join(IMG_DIR, "klienci", logo)):
            return f'<span class="d-logo"><img src="img/klienci/{logo}" alt="logo jednostki" loading="lazy"></span>'
        return f'<span class="d-logo">{shield}</span>'
    rows = "\n".join(
        f'''<div class="deploy">{d_logo(e)}<span class="d-date">{esc(e[0])}</span>
        <div class="d-body"><strong>{esc(e[1])}</strong><span>{esc(e[2])} · {esc(e[3])}</span></div>
        <span class="stamp">W SŁUŻBIE</span></div>'''
        for e in deps)
    return f'''
    <div class="meldunek" id="meldunek">
      <div class="m-head"><span class="m-dot"></span> MELDUNEK: FANTOMY W SŁUŻBIE</div>
      <div class="m-stats"><b data-n="{n_units}">0</b> {w_odm} &nbsp;·&nbsp; <b data-n="{n_regions}">0</b> {r_odm} &nbsp;·&nbsp; status: <b>operacyjne</b></div>
      <div class="m-viewport"><div class="m-track">
      {rows}
      </div></div>
      <div class="m-foot">Dziennik aktualizowany po każdej dostawie. Nazwy jednostek publikujemy wyłącznie za ich zgodą.</div>
    </div>
    <script>
    (function(){{
      var track=document.querySelector('.m-track'); if(!track) return;
      var vp=document.querySelector('.m-viewport'), VISIBLE=3;
      function setH(){{ var s=0,i; for(i=0;i<VISIBLE&&i<track.children.length;i++) s+=track.children[i].offsetHeight; vp.style.height=s+'px'; }}
      if(track.children.length>VISIBLE){{
        setH(); window.addEventListener('resize',setH);
        setInterval(function(){{
          var h=track.children[0].offsetHeight;
          track.style.transition='transform .6s ease';
          track.style.transform='translateY(-'+h+'px)';
          track.addEventListener('transitionend',function te(){{
            track.removeEventListener('transitionend',te);
            track.style.transition='none';
            track.appendChild(track.children[0]);
            track.style.transform='translateY(0)';
            setH();
          }});
        }},3200);
      }}
      var nums=document.querySelectorAll('.m-stats b[data-n]');
      var io=new IntersectionObserver(function(es){{
        es.forEach(function(e){{
          if(!e.isIntersecting) return; io.unobserve(e.target);
          var end=+e.target.getAttribute('data-n'), t0=performance.now(), dur=1400;
          requestAnimationFrame(function step(t){{
            var p=Math.min(1,(t-t0)/dur);
            e.target.textContent=Math.round(end*(1-Math.pow(1-p,3)));
            if(p<1) requestAnimationFrame(step);
          }});
        }});
      }},{{threshold:.4}});
      nums.forEach(function(n){{io.observe(n);}});
    }})();
    </script>'''

# ---------------------------------------------------------------- CSS
CSS = """
/* kroje pisma hostowane lokalnie — zero polaczen do stron trzecich */
@font-face{font-family:'Barlow';font-style:normal;font-weight:400;font-display:swap;src:url(../fonts/Barlow-400-latin-ext.woff2) format('woff2');unicode-range:U+0100-02BA, U+02BD-02C5, U+02C7-02CC, U+02CE-02D7, U+02DD-02FF, U+0304, U+0308, U+0329, U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF}
@font-face{font-family:'Barlow';font-style:normal;font-weight:400;font-display:swap;src:url(../fonts/Barlow-400-latin.woff2) format('woff2');unicode-range:U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD}
@font-face{font-family:'Barlow';font-style:normal;font-weight:500;font-display:swap;src:url(../fonts/Barlow-500-latin-ext.woff2) format('woff2');unicode-range:U+0100-02BA, U+02BD-02C5, U+02C7-02CC, U+02CE-02D7, U+02DD-02FF, U+0304, U+0308, U+0329, U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF}
@font-face{font-family:'Barlow';font-style:normal;font-weight:500;font-display:swap;src:url(../fonts/Barlow-500-latin.woff2) format('woff2');unicode-range:U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD}
@font-face{font-family:'Barlow';font-style:normal;font-weight:600;font-display:swap;src:url(../fonts/Barlow-600-latin-ext.woff2) format('woff2');unicode-range:U+0100-02BA, U+02BD-02C5, U+02C7-02CC, U+02CE-02D7, U+02DD-02FF, U+0304, U+0308, U+0329, U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF}
@font-face{font-family:'Barlow';font-style:normal;font-weight:600;font-display:swap;src:url(../fonts/Barlow-600-latin.woff2) format('woff2');unicode-range:U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD}
@font-face{font-family:'Barlow';font-style:normal;font-weight:700;font-display:swap;src:url(../fonts/Barlow-700-latin-ext.woff2) format('woff2');unicode-range:U+0100-02BA, U+02BD-02C5, U+02C7-02CC, U+02CE-02D7, U+02DD-02FF, U+0304, U+0308, U+0329, U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF}
@font-face{font-family:'Barlow';font-style:normal;font-weight:700;font-display:swap;src:url(../fonts/Barlow-700-latin.woff2) format('woff2');unicode-range:U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD}
@font-face{font-family:'Barlow Condensed';font-style:italic;font-weight:600;font-display:swap;src:url(../fonts/BarlowCondensed-600i-latin-ext.woff2) format('woff2');unicode-range:U+0100-02BA, U+02BD-02C5, U+02C7-02CC, U+02CE-02D7, U+02DD-02FF, U+0304, U+0308, U+0329, U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF}
@font-face{font-family:'Barlow Condensed';font-style:italic;font-weight:600;font-display:swap;src:url(../fonts/BarlowCondensed-600i-latin.woff2) format('woff2');unicode-range:U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD}
@font-face{font-family:'Barlow Condensed';font-style:italic;font-weight:800;font-display:swap;src:url(../fonts/BarlowCondensed-800i-latin-ext.woff2) format('woff2');unicode-range:U+0100-02BA, U+02BD-02C5, U+02C7-02CC, U+02CE-02D7, U+02DD-02FF, U+0304, U+0308, U+0329, U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF}
@font-face{font-family:'Barlow Condensed';font-style:italic;font-weight:800;font-display:swap;src:url(../fonts/BarlowCondensed-800i-latin.woff2) format('woff2');unicode-range:U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD}

:root{
  --yellow:#f5e003; --black:#0d0d0d; --dark:#161616; --paper:#ffffff;
  --ink:#1c1c1c; --muted:#5a5a5a; --line:#e5e5e5;
}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Barlow',system-ui,sans-serif;color:var(--ink);background:var(--paper);line-height:1.6}
img{max-width:100%}
a{color:inherit}
.wrap{max-width:1200px;margin:0 auto;padding:0 24px}

/* nagłówki w stylu SRP */
h1,h2,.disp{font-family:'Barlow Condensed',sans-serif;font-style:italic;font-weight:800;text-transform:uppercase;letter-spacing:.5px;line-height:1.05}
h2{font-size:clamp(28px,4vw,44px);margin-bottom:18px}
h3{font-size:20px;margin-bottom:10px;text-transform:uppercase;letter-spacing:.5px}

/* pasek górny */
.topbar{position:sticky;top:0;z-index:50;background:var(--black);color:#fff}
.nav-wrap{display:flex;align-items:center;justify-content:space-between;min-height:78px;gap:16px}
.logo{display:flex;align-items:center;text-decoration:none}
.logo-img{height:54px;width:auto;display:block}
nav{display:flex;align-items:center;gap:22px;flex-wrap:wrap}
nav a{color:#fff;text-decoration:none;text-transform:uppercase;font-size:13.5px;font-weight:600;letter-spacing:1px}
nav a:hover{color:var(--yellow)}
nav a.ico{background:#fff;color:var(--black);padding:8px 11px;border-radius:2px}
.burger{display:none;font-size:26px;color:#fff;cursor:pointer}

/* hero */
.hero{position:relative;background:
  linear-gradient(rgba(10,12,8,.55),rgba(10,12,8,.7)),
  repeating-linear-gradient(115deg,#2c3527 0 60px,#37402f 60px 120px,#242c1f 120px 180px);
  color:#fff;padding:110px 0 120px}
.hero .kicker{font-family:'Barlow Condensed';font-style:italic;font-weight:600;font-size:clamp(22px,3vw,34px);color:var(--yellow);text-transform:uppercase}
.hero .hero-title{margin:0;font-weight:inherit;font-style:normal;letter-spacing:0}
.hero .hero-title .kicker,.hero .hero-title .disp{display:block}
.hero .disp{font-size:clamp(44px,7vw,86px);color:transparent;-webkit-text-stroke:2px var(--yellow);text-transform:uppercase}
.hero .disp .solid{color:var(--yellow);-webkit-text-stroke:0}
.hero p{max-width:560px;margin:22px 0 30px}
.hero-note{position:absolute;right:0;bottom:0;background:rgba(0,0,0,.55);font-size:11px;padding:4px 10px;color:#cfcfcf}

/* przyciski */
.btn{display:inline-block;border:2px solid currentColor;padding:13px 26px;text-decoration:none;text-transform:uppercase;font-weight:700;font-size:13px;letter-spacing:1.5px;transition:.2s}
.btn .arr{margin-left:8px}
.btn:hover{background:var(--yellow);border-color:var(--yellow);color:var(--black)}
.btn.solid{background:var(--yellow);border-color:var(--yellow);color:var(--black)}
.btn.solid:hover{background:#fff;border-color:#fff}

/* sekcje */
section{padding:72px 0}
section.dark{background:var(--dark);color:#fff}
section.gray{background:#f4f4f2}
.lead{max-width:820px;font-size:18px;color:var(--muted)}
section.dark .lead{color:#c9c9c9}
.center{text-align:center}
.badge{display:inline-block;background:var(--yellow);color:var(--black);font-family:'Barlow Condensed';font-style:italic;font-weight:800;text-transform:uppercase;font-size:15px;padding:4px 14px;margin-bottom:14px;letter-spacing:1px}

/* siatki */
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:26px}
.grid4{display:grid;grid-template-columns:repeat(4,1fr);gap:22px}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center}

/* karty */
.card{background:#fff;border:1px solid var(--line);display:flex;flex-direction:column}
.card .body{padding:20px 22px 26px;flex:1;display:flex;flex-direction:column;gap:10px}
.card h3{font-family:'Barlow Condensed';font-style:italic;font-weight:800;font-size:22px}
.card p{font-size:14.5px;color:var(--muted);flex:1}
.card .btn{align-self:flex-start;font-size:11.5px;padding:9px 16px}
section.dark .card{background:#1f1f1f;border-color:#2c2c2c;color:#fff}
section.dark .card p{color:#b5b5b5}

/* placeholder zdjęcia */
.ph{aspect-ratio:4/3;background:repeating-linear-gradient(135deg,#3a4234 0 40px,#454e3d 40px 80px);display:flex;align-items:center;justify-content:center;color:#e6e6e6;font-size:12.5px;text-align:center;padding:10px}
.ph.tall{aspect-ratio:3/4}
.ph.wide{aspect-ratio:16/7}
.ph span{background:rgba(0,0,0,.45);padding:6px 12px;border-radius:3px}
.ph.has-img{padding:0;background:none}
.ph.has-img img{width:100%;height:100%;object-fit:cover;display:block}
.gallery{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:10px}
.gallery img{width:100%;aspect-ratio:1;object-fit:cover;display:block;border:1px solid var(--line);cursor:pointer}
video{width:100%;display:block;background:#000;margin-top:14px}

/* strona produktu */
.crumbs{font-size:13px;color:var(--muted);margin:26px 0 6px;text-transform:uppercase;letter-spacing:1px}
.crumbs a{color:var(--muted)}
.prod-grid{display:grid;grid-template-columns:1.05fr .95fr;gap:48px;align-items:start}
ul.feat{list-style:none;display:grid;gap:10px;margin:18px 0}
ul.feat li{padding-left:26px;position:relative;font-size:15.5px}
ul.feat li::before{content:"▸";position:absolute;left:2px;color:#b3a600;font-weight:800}
table.specs{width:100%;border-collapse:collapse;margin:18px 0;font-size:15px}
table.specs th{white-space:nowrap;text-align:left;vertical-align:top;padding:10px 18px 10px 0;font-weight:700}
table.specs td,table.specs th{border-bottom:1px solid var(--line);padding-top:10px;padding-bottom:10px}
.usebox{background:#f4f4f2;border-left:4px solid var(--yellow);padding:16px 20px;margin:20px 0;font-size:15px}

/* listy szkoleń */
.course{border:1px solid var(--line);padding:22px 26px;background:#fff}
.course-ico{display:inline-block;width:54px;height:54px;margin-bottom:12px}
.course-ico svg{width:100%;height:100%;display:block;filter:drop-shadow(0 1px 2px rgba(0,0,0,.18))}
.certs{display:flex;flex-wrap:wrap;gap:28px;align-items:flex-start;margin-top:18px}
.certs figure{width:150px;text-align:center}
.certs img{width:100%;height:90px;object-fit:contain;background:#fff;border:1px solid var(--line);padding:10px}
.certs figcaption{font-size:12.5px;color:var(--muted);margin-top:6px;text-transform:uppercase;letter-spacing:.5px}

/* opinie */
.quote{border:1px solid var(--line);background:#fff;padding:26px 28px;position:relative}
.quote::before{content:"”";font-family:'Barlow Condensed';font-style:italic;font-weight:800;font-size:64px;color:var(--yellow);position:absolute;top:2px;right:18px;line-height:1}
.quote p{font-size:15.5px;color:var(--ink)}
.quote .who{margin-top:16px;font-weight:700;font-size:14px}
.quote .who span{display:block;font-weight:400;color:var(--muted);font-size:13px}
.refbox{border:2px solid var(--yellow);background:#fffdf0;padding:30px 34px;margin-top:32px;max-width:760px}
.refbox h3{font-family:'Barlow Condensed';font-style:italic;font-weight:800;font-size:24px;margin-bottom:8px}
.refbox p{color:var(--muted);margin-bottom:18px}
.consent{display:flex;gap:10px;align-items:flex-start;max-width:600px;margin-top:14px;font-size:13.5px;color:var(--muted);font-weight:400;line-height:1.5}
.consent input{width:auto;margin-top:3px;flex:none}
.consent a{color:inherit;text-decoration:underline}
.newsletter .consent{color:#4a4a2a}
.form-ok{border:2px solid var(--yellow);background:#fffdf0;padding:26px 30px}
.form-ok strong{font-family:'Barlow Condensed';font-style:italic;font-weight:800;font-size:22px;display:block;margin-bottom:6px}
.form-ok p{color:var(--muted);font-size:15px}

/* meldunek — dziennik wdrożeń */
.meldunek{background:var(--black);color:#e6e6e6;padding:26px 30px;margin-top:32px;max-width:860px;border-left:6px solid var(--yellow);scroll-margin-top:96px}
.m-head{font-family:'Barlow Condensed';font-style:italic;font-weight:800;font-size:22px;color:var(--yellow);letter-spacing:1px;display:flex;align-items:center;gap:10px}
.m-dot{width:10px;height:10px;border-radius:50%;background:#3ddc55;box-shadow:0 0 8px #3ddc55;animation:puls 1.6s infinite}
@keyframes puls{50%{opacity:.35}}
.m-stats{font-size:13.5px;color:#9a9a9a;margin:8px 0 18px;text-transform:uppercase;letter-spacing:1px}
.m-stats b{color:var(--yellow)}
.deploy{display:flex;align-items:center;gap:18px;padding:13px 0;border-top:1px solid #2b2b2b}
.d-logo{width:46px;height:46px;border-radius:50%;background:#242424;border:1px solid #383838;display:flex;align-items:center;justify-content:center;flex:none;overflow:hidden}
.d-logo svg{width:26px;height:26px}
.d-logo img{width:100%;height:100%;object-fit:contain;padding:5px;background:#fff}
.d-date{font-family:'Barlow Condensed';font-weight:800;font-style:italic;color:var(--yellow);font-size:17px;min-width:74px}
.d-body{flex:1;display:flex;flex-direction:column}
.d-body strong{font-size:15.5px}
.d-body span{font-size:13px;color:#9a9a9a}
.stamp{font-family:'Barlow Condensed';font-style:italic;font-weight:800;font-size:13px;letter-spacing:2px;color:var(--yellow);border:2px solid var(--yellow);padding:3px 10px;transform:rotate(-6deg);white-space:nowrap}
.m-foot{border-top:1px solid #2b2b2b;margin-top:4px;padding-top:12px;font-size:12px;color:#7a7a7a}
.m-viewport{overflow:hidden}
.m-track{will-change:transform}
@media(max-width:600px){.deploy{flex-wrap:wrap}.stamp{margin-left:88px}}
.course h3{font-family:'Barlow Condensed';font-style:italic;font-weight:800;font-size:22px}
.course p{color:var(--muted);font-size:15px}

/* formularze */
form{display:grid;gap:16px;max-width:680px}
label{font-weight:600;font-size:14px;display:grid;gap:6px}
input,textarea,select{font:inherit;padding:11px 13px;border:1.5px solid #cfcfcf;background:#fff;width:100%}
input:focus,textarea:focus,select:focus{outline:2px solid var(--yellow)}
form .btn{justify-self:start;cursor:pointer;background:var(--yellow);border-color:var(--yellow)}
.note{font-size:13px;color:var(--muted)}

/* stopka */
footer{background:var(--black);color:#d6d6d6;padding:56px 0 24px;font-size:14.5px}
.foot-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:36px}
footer h4{font-family:'Barlow Condensed';font-style:italic;text-transform:uppercase;color:var(--yellow);font-size:19px;margin-bottom:10px}
footer a{color:#d6d6d6}
.rejestr{font-size:12.5px;color:#9a9a9a;line-height:1.7}
.copyright{border-top:1px solid #2a2a2a;margin-top:40px;padding-top:18px;font-size:12.5px;color:#8a8a8a}

/* podstrony — nagłówek */
.page-head{background:linear-gradient(rgba(10,10,10,.82),rgba(10,10,10,.88)),url("../img/home-02.jpg") center/cover,var(--black);color:#fff;padding:72px 0}
.page-head h1{font-size:clamp(34px,5vw,58px);color:var(--yellow)}
.page-head p{color:#c9c9c9;max-width:760px;margin-top:10px}

/* --- rozszerzenia B2B --- */
.nav-cta{background:var(--yellow);color:var(--black)!important;padding:10px 16px;border-radius:2px;font-weight:800!important}
.nav-cta:hover{background:#fff;color:var(--black)!important}

.trustbar{background:var(--yellow);color:var(--black);padding:18px 0}
.trustbar .wrap{display:flex;flex-wrap:wrap;gap:10px 34px;justify-content:center;align-items:center}
.trustbar span{font-family:'Barlow Condensed';font-style:italic;font-weight:800;text-transform:uppercase;font-size:16px;letter-spacing:.5px}

.steps{display:grid;grid-template-columns:repeat(4,1fr);gap:24px;margin-top:38px}
.step{border-top:4px solid var(--yellow);padding-top:16px}
.step .no{font-family:'Barlow Condensed';font-style:italic;font-weight:800;font-size:40px;color:var(--yellow);line-height:1}
.step h3{font-family:'Barlow Condensed';font-style:italic;font-weight:800;font-size:21px;margin:8px 0 6px}
.step p{font-size:14.5px;color:#b5b5b5}
section:not(.dark) .step p{color:var(--muted)}

details.faq{border:1px solid var(--line);background:#fff;padding:0 22px;margin-bottom:10px}
details.faq summary{cursor:pointer;font-weight:700;font-size:16px;padding:16px 0;list-style:none;position:relative;padding-right:34px}
details.faq summary::after{content:"+";position:absolute;right:2px;top:12px;font-size:24px;color:#b3a600;font-weight:800}
details.faq[open] summary::after{content:"–"}
details.faq p{padding:0 0 18px;color:var(--muted);font-size:15px}

table.cmp{width:100%;border-collapse:collapse;font-size:13.5px;background:#fff}
table.cmp th,table.cmp td{border:1px solid var(--line);padding:10px 12px;text-align:left;vertical-align:top}
table.cmp thead th{background:var(--black);color:var(--yellow);font-family:'Barlow Condensed';font-style:italic;font-size:16px;letter-spacing:.5px;text-transform:uppercase}
table.cmp tbody th{background:#f4f4f2;white-space:normal;font-weight:700}
table.cmp tbody tr:hover td{background:#fffbe0}
.cmp-scroll{overflow-x:auto}
.cmp-scroll table{min-width:980px}

.seg{border:1px solid var(--line);background:#fff;padding:26px 28px;display:flex;flex-direction:column;gap:12px}
.seg h3{font-family:'Barlow Condensed';font-style:italic;font-weight:800;font-size:24px}
.seg p{color:var(--muted);font-size:15px;flex:1}
.seg .tags{display:flex;flex-wrap:wrap;gap:8px}
.seg .tags a{font-size:12.5px;text-transform:uppercase;letter-spacing:.5px;font-weight:700;text-decoration:none;border:1.5px solid var(--black);padding:5px 10px}
.seg .tags a:hover{background:var(--yellow);border-color:var(--yellow)}

.dl{display:flex;justify-content:space-between;align-items:center;gap:16px;border:1px solid var(--line);background:#fff;padding:16px 20px;margin-bottom:10px}
.dl .meta{font-size:13px;color:var(--muted)}
.dl .btn{font-size:11px;padding:8px 14px;white-space:nowrap}

.article-body h3{font-family:'Barlow Condensed';font-style:italic;font-weight:800;font-size:24px;margin:30px 0 10px}
.article-body p{margin-bottom:14px;font-size:16.5px;max-width:820px}
.article-body a{color:#8a7f00;font-weight:600}

.checks{display:grid;grid-template-columns:repeat(2,1fr);gap:8px 22px;margin:4px 0}
.checks label{display:flex;gap:10px;align-items:flex-start;font-weight:500;font-size:14.5px}
.checks input{width:auto;margin-top:3px}

.newsletter{background:var(--yellow);padding:56px 0}
.newsletter h2{color:var(--black)}
.newsletter form{display:flex;flex-wrap:wrap;gap:12px;max-width:560px}
form .consent{flex-basis:100%}
.newsletter .btn{background:var(--black);color:var(--yellow);border-color:var(--black)}

@media(max-width:960px){
  .steps{grid-template-columns:repeat(2,1fr)}
  .checks{grid-template-columns:1fr}
  .newsletter form{flex-direction:column}
}
@media(max-width:960px){
  .grid3,.grid4{grid-template-columns:repeat(2,1fr)}
  .grid2,.prod-grid,.foot-grid{grid-template-columns:1fr}
  nav{display:none;position:absolute;top:78px;left:0;right:0;background:var(--black);flex-direction:column;padding:20px;align-items:flex-start}
  #nav-toggle:checked ~ nav{display:flex}
  .burger{display:block}
}
@media(max-width:600px){.grid3,.grid4{grid-template-columns:1fr}}
"""

# ---------------------------------------------------------------- strony
def page_home():
    cards = "\n".join(
        f'<div class="card">{pic(p["slug"], p["name"], thumb=True)}<div class="body"><h3>{esc(p["name"])}</h3>'
        f'<p>{esc(p["short"])}</p>{btn("produkty/" + p["slug"] + ".html", "Czytaj więcej")}</div></div>'
        for p in PRODUCTS
    )
    courses = "\n".join(f'<div class="course"><span class="course-ico">{i}</span><h3>{esc(n)}</h3><p>{esc(d)}</p></div>' for i, n, d in COURSES)
    by_slug = {p["slug"]: p for p in PRODUCTS}
    segs = "\n".join(
        f'<div class="seg"><h3>{esc(s["name"])}</h3><p>{esc(s["desc"])}</p><div class="tags">'
        + "".join(f'<a href="produkty/{sl}.html">{esc(by_slug[sl]["name"].replace("Manekin ratowniczy ", "").replace("Manekin do ", ""))}</a>' for sl in s["products"])
        + f'</div><a class="btn" href="dla-kogo.html#{s["anchor"]}" style="align-self:flex-start;font-size:11.5px;padding:9px 16px">Czytaj więcej <span class="arr">→</span></a></div>'
        for s in SEGMENTS
    )
    faqs = "\n".join(f'<details class="faq"><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q, a in FAQS[:4])
    # kotwica #meldunek zawsze istnieje (nawigacja i stopka do niej linkują) — bez wpisów pokazujemy uczciwy stan pusty
    deploys_html = render_meldunek(DEPLOYMENTS) if DEPLOYMENTS else render_meldunek_pusty()
    if TESTIMONIALS:
        quotes = ('<div class="grid3" style="margin-top:36px">' + "\n".join(
            f'<div class="quote"><p>„{esc(t)}”</p><div class="who">{esc(n)}<span>{esc(o)}</span></div></div>'
            for t, n, o in TESTIMONIALS) + "</div>") + deploys_html
    elif DEPLOYMENTS:
        quotes = deploys_html
    else:
        quotes = """<div class="refbox">
      <h3>Twoja jednostka może być naszą pierwszą polską referencją</h3>
      <p>Rozpoczynamy dystrybucję w Polsce i budujemy listę referencyjną. Umów bezpłatny pokaz,
      przetestuj sprzęt w swoich procedurach — a jeśli spełni oczekiwania, Twoja opinia pojawi się
      w tym miejscu.</p>
      <a class="btn solid" href="zapytanie-ofertowe.html">Umów pokaz i przetestuj <span class="arr">→</span></a>
    </div>""" + deploys_html
    hero_bg = ('style="background-image:linear-gradient(rgba(10,12,8,.55),rgba(10,12,8,.7)),'
               "url('img/home-01.jpg');background-size:cover;background-position:center\"") if main_image("home") else ""
    org_ld = json.dumps({
        "@context": "https://schema.org", "@type": "Organization",
        "name": BRAND, "description": DISTRIBUTOR, "url": BASE_URL,
        "email": EMAIL, "telephone": PHONE.replace(" ", ""),
        "logo": BASE_URL + "/img/srp-logo.svg", "areaServed": "PL",
        "legalName": NAZWA_PELNA, "taxID": NIP, "vatID": "PL" + NIP,
        "address": {"@type": "PostalAddress", "streetAddress": ADRES_ULICA,
                     "postalCode": ADRES_MIASTO.split(" ")[0], "addressLocality": " ".join(ADRES_MIASTO.split(" ")[1:]),
                     "addressCountry": "PL"},
        "contactPoint": {"@type": "ContactPoint", "telephone": PHONE.replace(" ", ""),
                          "email": EMAIL, "contactType": "sales", "availableLanguage": ["pl", "en"]},
    }, ensure_ascii=False)
    body = f"""
<script type="application/ld+json">{org_ld}</script>
<div class="hero" {hero_bg}>
  <div class="wrap">
    <h1 class="hero-title"><span class="kicker">Przenieś swój trening ratowniczy</span>
    <span class="disp">na wyższy<br><span class="solid">poziom</span></span></h1>
    <p>Szukasz sprzętu treningowego najwyższej jakości? Jesteśmy wyłącznym dystrybutorem szwedzkich
    manekinów ratowniczych i symulatorów ran SRP w Polsce. Skontaktuj się z nami, aby poznać
    właściwości produktów, ceny i dostępność.</p>
    <a class="btn solid" href="zapytanie-ofertowe.html">Umów bezpłatny pokaz <span class="arr">→</span></a>
    &nbsp; {btn("porownanie-manekinow.html", "Porównaj modele")}
  </div>
</div>

<div class="trustbar"><div class="wrap">
  <span>🇸🇪 Made in Sweden — ręcznie od 2009</span>
  <span>Certyfikaty TÜV · EN ISO 6941</span>
  <span>Kody NATO (NSN / NCAGE)</span>
  <span>Serwis i części w Polsce</span>
  <span>Wsparcie zamówień publicznych</span>
</div></div>

<section>
  <div class="wrap grid3">
    <div class="card">{pic("home-02.jpg", "Manekiny ratownicze", thumb=True)}<div class="body">
      <h3>Manekiny ratownicze</h3><p>Wysokiej jakości manekiny do ćwiczeń na lądzie i w wodzie — od ewakuacji w dymie po scenariusze taktyczno-medyczne.</p>
      {btn("produkty/index.html", "Czytaj więcej")}</div></div>
    <div class="card">{pic("szkolenia", "Szkolenia", thumb=True)}<div class="body">
      <h3>Szkolenia</h3><p>Kursy RKO, pierwszej pomocy i kontroli krwotoków prowadzone przez certyfikowanych instruktorów z doświadczeniem operacyjnym.</p>
      {btn("szkolenia.html", "Czytaj więcej")}</div></div>
    <div class="card">{pic("symulatory-ran", "Symulatory ran", thumb=True)}<div class="body">
      <h3>Symulatory ran</h3><p>Bardzo realistyczne symulatory obrażeń do szkoleń z tamowania krwotoków — staza, packing, opatrunek uciskowy.</p>
      {btn("produkty/symulatory-ran.html", "Czytaj więcej")}</div></div>
  </div>
</section>

<section class="dark">
  <div class="wrap grid2">
    <div>
      <span class="badge">Witamy</span>
      <h2>Szwedzka jakość.<br>Polska dystrybucja.</h2>
      <p class="lead">Svenska Räddningsprodukter AB to szwedzki producent symulatorów ran i manekinów
      treningowych najwyższej jakości — do zastosowań lądowych i wodnych. Od 2009 roku firma rozwija
      i wytwarza ręcznie swoje produkty w Sali (Västmanland), z myślą o profesjonalistach z ratownictwa,
      ochrony zdrowia, wojska i służb mundurowych.</p>
      <p class="lead" style="margin-top:14px">Jako wyłączny dystrybutor SRP w Polsce zapewniamy doradztwo,
      sprzedaż, serwis i szkolenia z użyciem oryginalnego sprzętu.</p>
    </div>
    {pic("home-12.jpg", "Produkcja SRP", "ph tall", thumb=True)}
  </div>
</section>

<section class="gray">
  <div class="wrap">
    <span class="badge">Made in Sweden</span>
    <h2>Produkty do realistycznego treningu ratowniczego</h2>
    <p class="lead">Manekiny SRP odwzorowują rzeczywiste ciało człowieka pod względem masy, ruchomości
    stawów i oporu. Dzięki temu sprawdzają się w najbardziej wymagających ćwiczeniach: przeszukiwaniu
    pomieszczeń w dymie, ewakuacji, ratownictwie wodnym i taktycznej opiece nad poszkodowanym.</p>
    <div class="grid4" style="margin-top:40px">{cards}</div>
  </div>
</section>

<section>
  <div class="wrap grid2">
    <div>
      <span class="badge">Jasny cel</span>
      <h2>Żeby na ostro czuło się jak za drugim razem</h2>
      <p class="lead">Cała filozofia rozwoju produktów SRP sprowadza się do jednego: trening ma być tak
      realistyczny, żeby prawdziwa sytuacja była już „tym drugim razem”. Ręcznie wykonywane produkty
      z logo SRP to znak jakości — funkcjonalności, realizmu i trwałości.</p>
    </div>
    {pic("home-06.jpg", "Ćwiczenia służb ratowniczych z manekinem SRP", thumb=True)}
  </div>
</section>

<section class="dark">
  <div class="wrap">
    <span class="badge">Szkolenia</span>
    <h2>Instruktorzy z doświadczeniem operacyjnym</h2>
    <p class="lead">Oferujemy szkolenia prowadzone przez instruktorów z międzynarodowymi certyfikatami
    Stop the Bleed®, ERC i TECC oraz wieloletnim doświadczeniem w służbach interwencyjnych —
    od podstawowej RKO po taktyczną opiekę nad poszkodowanym.</p>
    <div class="grid3" style="margin-top:36px">{courses}</div>
    <div style="margin-top:36px">{btn("szkolenia.html", "Zobacz wszystkie szkolenia")}</div>
  </div>
</section>

<section>
  <div class="wrap">
    <span class="badge">Zaufanie i opinie</span>
    <h2>Sprawdzeni w codziennej służbie</h2>
    <p class="lead">Produkty SRP od 2009 roku pracują na co dzień w jednostkach straży pożarnej,
    policji, wojska, ratownictwa medycznego i morskiego — wszędzie tam, gdzie sprzęt musi wytrzymać
    setki ćwiczeń rocznie. Producent został wyróżniony m.in. nagrodą zrównoważonego rozwoju (2025),
    a jego rozwiązania opisywały media branżowe i ogólnokrajowe w Szwecji.</p>
    {quotes}
  </div>
</section>

<section class="gray">
  <div class="wrap">
    <span class="badge">Dla kogo</span>
    <h2>Rozwiązania dopasowane do Twojej służby</h2>
    <p class="lead">Inne potrzeby ma rota gaśnicza, inne zespół medyczny, a jeszcze inne ośrodek
    szkoleniowy. Zobacz, co sprawdza się w Twojej branży.</p>
    <div class="grid3" style="margin-top:36px">{segs}</div>
  </div>
</section>

<section>
  <div class="wrap">
    <span class="badge">Proces zakupu</span>
    <h2>Od pierwszej rozmowy do gotowego ośrodka ćwiczeń</h2>
    <div class="steps">
      <div class="step"><div class="no">01</div><h3>Konsultacja i dobór</h3>
        <p>Rozmawiamy o Waszych scenariuszach ćwiczeń i budżecie — doradzimy konfigurację zamiast sprzedawać „z katalogu”.</p></div>
      <div class="step"><div class="no">02</div><h3>Bezpłatny pokaz</h3>
        <p>Przywozimy sprzęt do Twojej jednostki. Testujesz go na własnych noszach, w swoich procedurach, ze swoim zespołem.</p></div>
      <div class="step"><div class="no">03</div><h3>Oferta lub przetarg</h3>
        <p>Przygotowujemy wycenę, dokumentację do zamówień publicznych (OPZ, certyfikaty) i warianty finansowania.</p></div>
      <div class="step"><div class="no">04</div><h3>Dostawa i wdrożenie</h3>
        <p>Dostawa, szkolenie instruktorów z wykorzystania sprzętu w scenariuszach oraz serwis i części w Polsce.</p></div>
    </div>
  </div>
</section>

<section class="gray">
  <div class="wrap">
    <span class="badge">FAQ</span>
    <h2>Najczęstsze pytania kupujących</h2>
    <div style="margin-top:26px;max-width:860px">{faqs}</div>
    <div style="margin-top:26px">{btn("faq.html", "Wszystkie pytania i odpowiedzi")}</div>
  </div>
</section>

<div class="newsletter">
  <div class="wrap">
    <h2>Bądź na bieżąco</h2>
    <p style="margin:6px 0 18px;max-width:640px">Nowe produkty, terminy szkoleń otwartych i praktyczne
    materiały dla instruktorów — maksymalnie raz w miesiącu, bez spamu.</p>
    <form {form_attrs}>
      <input type="email" name="email" placeholder="Twój adres e-mail" required>
      <button class="btn" type="submit">Zapisz się</button>
    <input type="hidden" name="typ" value="newsletter">
    <label class="consent"><input type="checkbox" name="zgoda_marketing" required> <span>Chcę otrzymywać materiały i informacje o produktach oraz szkoleniach na podany adres e-mail. Zgodę mogę wycofać w każdej chwili, a jej brak nie wpływa na możliwość kontaktu z nami. <a href="/polityka-prywatnosci.html">Informacja o przetwarzaniu danych</a>.</span></label>
    </form>
  </div>
</div>
"""
    return head("Manekiny ratownicze i symulatory ran SRP") + body + footer()

def page_products_index():
    cards = "\n".join(
        f'<div class="card">{pic(p["slug"], p["name"], depth=1, thumb=True)}<div class="body"><h3>{esc(p["name"])}</h3>'
        f'<p>{esc(p["short"])}</p>{btn(p["slug"] + ".html", "Czytaj więcej")}</div></div>'
        for p in PRODUCTS
    )
    body = f"""
<div class="page-head"><div class="wrap"><h1>Produkty</h1>
<p>Szwedzkie manekiny ratownicze, symulatory ran i trenażery medyczne SRP — ręcznie wykonane,
przetestowane w praktyce, zaprojektowane na lata intensywnych ćwiczeń.</p></div></div>
<section><div class="wrap grid3">{cards}</div></section>
"""
    return head("Manekiny ratownicze i fantomy — katalog", 1) + body + footer(1)

def page_product(p):
    feats = "\n".join(f"<li>{esc(f)}</li>" for f in p["features"])
    specs = "\n".join(f"<tr><th>{esc(k)}</th><td>{esc(v)}</td></tr>" for k, v in p["specs"])
    specs_html = f'<h3>Dane techniczne</h3><table class="specs">{specs}</table>' if specs else ""
    gal = gallery_images(p["slug"])
    gallery_html = ('<div class="gallery">' + "".join(
        f'<a href="../img/{f}" target="_blank"><img src="{("../img/thumb/" + thumb_path(f)) if thumb_path(f) else ("../img/" + f)}" alt="{esc(p["name"])} — zdjęcie" loading="lazy" decoding="async"></a>'
        for f in gal) + "</div>") if gal else ""
    vids = videos_for(p["slug"])
    video_html = "".join(
        f'<video controls preload="metadata"><source src="../img/{f}" type="video/mp4"></video>'
        for f in vids)
    if vids:
        video_html += '<p class="note">Film produktowy SRP. [Przed publikacją skompresuj plik — oryginał jest bardzo duży.]</p>'
    is_manikin = p["slug"] in {c[0] for c in COMPARE_COLS}
    cmp_link = ('<p class="note" style="margin-top:14px">Nie wiesz, który model wybrać? '
                '<a href="../porownanie-manekinow.html"><strong>Zobacz porównanie wszystkich manekinów →</strong></a></p>') if is_manikin else ""
    jsonld = ('<script type="application/ld+json">{"@context":"https://schema.org","@type":"Product",'
              f'"name":{json.dumps(p["name"], ensure_ascii=False)},'
              f'"description":{json.dumps(p["short"], ensure_ascii=False)},'
              '"brand":{"@type":"Brand","name":"SRP"},'
              '"manufacturer":{"@type":"Organization","name":"Svenska Räddningsprodukter AB"},'
              '"countryOfOrigin":"SE"}</script>')
    body = jsonld + f"""
<div class="wrap crumbs"><a href="../index.html">Start</a> / <a href="index.html">Produkty</a> / {esc(p["name"])}</div>
<section style="padding-top:20px">
  <div class="wrap prod-grid">
    <div>
      {pic(p["slug"], p["name"], depth=1)}
      {gallery_html}
      {video_html}
    </div>
    <div>
      <h1 class="disp" style="font-size:clamp(30px,4vw,44px)">{esc(p["name"])}</h1>
      <p class="lead" style="margin-top:12px">{esc(p["short"])}</p>
      <h3 style="margin-top:26px">Najważniejsze cechy</h3>
      <ul class="feat">{feats}</ul>
      {specs_html}
      <div class="usebox"><strong>Zastosowanie:</strong> {esc(p["use"])}</div>
      <a class="btn solid" href="../zapytanie-ofertowe.html">Zapytaj o cenę <span class="arr">→</span></a>
      &nbsp; {btn("../zapytanie-ofertowe.html", "Umów bezpłatny pokaz")}
      {cmp_link}
      <p class="note">Do produktu dołączamy: kartę katalogową PDF, dokumenty do postępowań (certyfikaty,
      deklaracje) oraz opcjonalne szkolenie wdrożeniowe — <a href="../do-pobrania.html">zobacz materiały do pobrania</a>.</p>
    </div>
  </div>
</section>
"""
    return head(p["name"], 1, p["short"]) + body + footer(1)

CERT_DIR = os.path.join(IMG_DIR, "certyfikaty")

def cert_logos():
    """logotypy certyfikatów z img/certyfikaty/ (nazwa pliku = podpis)"""
    if not os.path.isdir(CERT_DIR):
        return []
    return sorted(f for f in os.listdir(CERT_DIR)
                  if f.lower().endswith((".png", ".jpg", ".jpeg", ".svg", ".webp")))

def page_trainings():
    courses = "\n".join(f'<div class="course"><span class="course-ico">{i}</span><h3>{esc(n)}</h3><p>{esc(d)}</p></div>' for i, n, d in COURSES)
    logos = cert_logos()
    if logos:
        certs = '<div class="certs">' + "".join(
            f'<figure><img src="img/certyfikaty/{f}" alt="{esc(os.path.splitext(f)[0])}" loading="lazy">'
            f'<figcaption>{esc(os.path.splitext(f)[0].replace("-", " ").replace("_", " "))}</figcaption></figure>'
            for f in logos) + "</div>"
    else:
        certs = """<div class="trustbar" style="background:#f4f4f2;border:1px solid var(--line);margin-top:14px"><div class="wrap" style="padding:0">
      <span>Stop the Bleed® — certyfikowani instruktorzy</span>
      <span>Wytyczne resuscytacji ERC</span>
      <span>TECC — Tactical Emergency Casualty Care</span>
      <span>Doświadczenie operacyjne służb</span>
    </div></div>"""
    body = f"""
<div class="page-head"><div class="wrap"><h1>Szkolenia</h1>
<p>Szkolenia prowadzą instruktorzy z wieloletnim doświadczeniem w służbach interwencyjnych,
posiadający międzynarodowe certyfikaty: Stop the Bleed®, wytycznych resuscytacji ERC oraz
TECC (Tactical Emergency Casualty Care). Zajęcia praktyczne odbywają się na realistycznych
symulatorach ran i manekinach SRP.</p></div></div>
<section><div class="wrap">
  <div class="grid3">{courses}</div>
  <div style="margin-top:44px">
    <h3>Certyfikaty i standardy</h3>
    <p class="lead" style="margin-top:8px">Nasi instruktorzy posiadają aktualne certyfikaty —
    kursy prowadzimy według międzynarodowych wytycznych.</p>
    {certs}
  </div>
  <p class="lead" style="margin-top:40px">Szkolimy w siedzibie klienta lub we wskazanym ośrodku, na sprzęcie,
  który potem możesz mieć u siebie. Zapytaj o program szyty na miarę Twojej organizacji.</p>
  <div style="margin-top:20px">{btn("zapytanie-ofertowe.html", "Zapytaj o termin i wycenę")}</div>
</div></section>
"""
    return head("Szkolenia RKO, pierwsza pomoc, Stop the Bleed", 0) + body + footer()

def page_terms():
    body = f"""
<div class="page-head"><div class="wrap"><h1>Warunki zakupu</h1>
<p>Poniższe warunki dotyczą sprzedaży prowadzonej przez {BRAND} na terenie Polski.
[Do weryfikacji prawnej i uzupełnienia danymi Twojej firmy.]</p></div></div>
<section><div class="wrap" style="max-width:860px">
  <h3>Płatności</h3>
  <p>Instytucje i firmy: płatność przelewem na podstawie faktury VAT, termin 30 dni (możliwa e-faktura).
  Zastrzegamy możliwość weryfikacji płatniczej i przedpłaty przy pierwszym zamówieniu.
  Klienci indywidualni: przedpłata lub płatność za pobraniem.</p>
  <h3 style="margin-top:26px">Dostawa</h3>
  <p>Wysyłka kurierem na terenie całej Polski. Manekiny ratownicze ze względu na gabaryty wysyłane są
  jako przesyłki paletowe. Koszt transportu i opakowania doliczany jest do zamówienia, o ile nie
  uzgodniono inaczej.</p>
  <h3 style="margin-top:26px">Gwarancja</h3>
  <p>Manekiny ratownicze: 12 miesięcy od dostawy na wady produkcyjne. Pozostałe produkty: zgodnie ze
  specyfikacją — dla wybranych pozycji nawet do 20 lat. Gwarancja nie obejmuje uszkodzeń wynikających
  z niewłaściwego użytkowania; naprawy poza autoryzowanym serwisem powodują utratę gwarancji.</p>
  <h3 style="margin-top:26px">Zwroty</h3>
  <p>Zwrot możliwy w ciągu 14 dni — produkt nieużywany, w oryginalnym opakowaniu, z kompletem
  dokumentów. Koszt przesyłki zwrotnej ponosi kupujący; zwracana jest wartość produktu bez kosztów
  dostawy.</p>
  <h3 style="margin-top:26px">Reklamacje</h3>
  <p>Niezgodność dostawy, uszkodzenia transportowe lub braki prosimy zgłaszać w ciągu 5 dni roboczych
  od odbioru — prześlemy instrukcję bezpłatnego zwrotu.</p>
  <h3 style="margin-top:26px">Zastrzeżenie własności</h3>
  <p>Towar pozostaje własnością sprzedawcy do momentu pełnej zapłaty.</p>
</div></section>
"""
    return head("Warunki zakupu, dostawa i gwarancja") + body + footer()

def page_quote():
    prods = "\n".join(f'<label><input type="checkbox" name="products" value="{p["slug"]}"> {esc(p["name"])}</label>' for p in PRODUCTS)
    body = f"""
<div class="page-head"><div class="wrap"><h1>Zapytanie ofertowe</h1>
<p>Wypełnij formularz — przygotujemy wycenę z aktualną dostępnością, terminem dostawy i wariantami
finansowania. Odpowiadamy zwykle w ciągu jednego dnia roboczego. Przygotowujemy również kompletną
dokumentację do zamówień publicznych.</p></div></div>
<section><div class="wrap">
<form {form_attrs} style="max-width:820px">
  <div class="grid2" style="gap:16px;align-items:start">
    <label>Imię i nazwisko <input name="name" required></label>
    <label>Organizacja / jednostka <input name="org"></label>
    <label>E-mail służbowy <input type="email" name="email" required></label>
    <label>Telefon <input type="tel" name="phone"></label>
    <label>NIP (do oferty) <input name="nip"></label>
    <label>Rodzaj organizacji
      <select name="type"><option>— wybierz —</option><option>Straż pożarna (PSP/OSP)</option>
      <option>Wojsko / obrona</option><option>Ratownictwo medyczne / szpital</option>
      <option>Ratownictwo wodne</option><option>Przemysł / BHP</option>
      <option>Uczelnia / ośrodek szkoleniowy</option><option>Inna</option></select></label>
  </div>
  <fieldset style="border:1px solid var(--line);padding:16px 20px">
    <legend style="font-weight:700;padding:0 8px">Interesujące produkty (zaznacz dowolne)</legend>
    <div class="checks">{prods}
      <label><input type="checkbox" name="products" value="szkolenie"> Szkolenie / kurs</label>
    </div>
  </fieldset>
  <div class="checks">
    <label><input type="checkbox" name="demo"> Chcę umówić <strong>bezpłatny pokaz</strong> w naszej siedzibie</label>
    <label><input type="checkbox" name="tender"> Zapytanie dotyczy <strong>postępowania przetargowego</strong></label>
    <label><input type="checkbox" name="financing"> Interesuje mnie <strong>leasing / najem / raty</strong></label>
    <label><input type="checkbox" name="training"> Poproszę o wycenę <strong>pakietu ze szkoleniem wdrożeniowym</strong></label>
  </div>
  <label>Wiadomość (ilości, konfiguracja — np. masa manekina, planowany termin)
    <textarea name="msg" rows="6"></textarea></label>
  <button class="btn" type="submit">Wyślij zapytanie <span class="arr">→</span></button>
  <p class="note">{FORM_NOTE}</p>
</form>
</div></section>
"""
    return head("Wycena manekinów ratowniczych i szkoleń") + body + footer()

def page_about():
    body = f"""
<div class="page-head"><div class="wrap"><h1>O nas</h1></div></div>
<section><div class="wrap grid2">
  <div>
    <span class="badge">Producent</span>
    <h2>Svenska Räddningsprodukter AB</h2>
    <p class="lead">Firma została założona w 2009 roku przez Fredrika Forsberga, by wypełnić lukę na
    rynku realistycznych manekinów treningowych. Produkty powstają ręcznie w Sali (Västmanland)
    w Szwecji i trafiają do straży pożarnej, policji, wojska, ratownictwa medycznego i morskiego
    oraz na rynek cywilny. Od 2022 roku ofertę uzupełniają realistyczne symulatory ran do nauki
    kontroli krwotoków.</p>
    <p class="lead" style="margin-top:14px">Filozofia marki: trening ma być tak realistyczny, żeby
    prawdziwe zdarzenie było już „tym drugim razem”.</p>
  </div>
  {pic("home-05.jpg", "Produkty SRP", "ph tall", thumb=True)}
</section>
<section class="gray"><div class="wrap grid2">
  {placeholder("Zdjęcie: zespół dystrybutora w Polsce")}
  <div>
    <span class="badge">Dystrybutor</span>
    <h2>{BRAND}</h2>
    <p class="lead">Jesteśmy wyłącznym dystrybutorem produktów SRP na rynku polskim. Zapewniamy pełną
    obsługę w języku polskim: doradztwo w doborze sprzętu do scenariuszy ćwiczeń, bezpłatne pokazy
    w siedzibie klienta, wsparcie zamówień publicznych, serwis i części oraz szkolenia z użyciem
    dostarczanego sprzętu.</p>
    <p class="lead" style="margin-top:14px">Współpracujemy bezpośrednio z producentem w Szwecji, dzięki
    czemu oferujemy pełną konfigurowalność produktów — od niestandardowych mas manekinów po dobór
    modułów urazowych pod konkretne programy szkoleniowe.</p>
  </div>
</div></section>
"""
    return head("O nas — dystrybutor SRP w Polsce") + body + footer()

def page_news():
    body = f"""
<div class="page-head"><div class="wrap"><h1>Aktualności</h1>
<p>Wdrożenia, targi, nowe produkty i terminy szkoleń.</p></div></div>
<section><div class="wrap">
  <div class="grid3">
  <div class="card">{pic("home-05.jpg", "Produkty SRP", thumb=True)}<div class="body"><h3>Produkty SRP oficjalnie w Polsce</h3>
  <p>Rozpoczynamy oficjalną, wyłączną dystrybucję szwedzkich manekinów ratowniczych i symulatorów ran
  SRP na rynku polskim. Zapraszamy jednostki i ośrodki szkoleniowe na bezpłatne pokazy sprzętu.</p>
  {btn("zapytanie-ofertowe.html", "Umów pokaz")}</div></div>
  </div>
  <p class="lead" style="margin-top:34px">Tu będą pojawiać się informacje o targach, pokazach,
  wdrożeniach u klientów i nowościach produktowych. Chcesz je dostawać na skrzynkę?
  <a href="wiedza/index.html"><strong>Zapisz się na nasze materiały →</strong></a></p>
</div></section>
"""
    return head("Aktualności — wdrożenia i szkolenia") + body + footer()

def page_contact():
    body = f"""
<div class="page-head"><div class="wrap"><h1>Kontakt</h1></div></div>
<section><div class="wrap grid2" style="align-items:start">
  <div>
    <h3>{BRAND}</h3>
    <p>{DISTRIBUTOR}</p>
    <p style="margin-top:12px">{DANE_REJESTROWE}</p>
    <p style="margin-top:14px"><strong>Telefon:</strong> <a href="tel:{PHONE.replace(' ', '')}">{PHONE}</a><br>
    <strong>E-mail:</strong> <a href="mailto:{EMAIL}">{EMAIL}</a></p>
    <h3 style="margin-top:30px">Producent</h3>
    <p>Svenska Räddningsprodukter AB<br>Bergslagsgatan 1F, SE-733 31 Sala, Szwecja</p>
  </div>
  <form {form_attrs}>
    <label>Imię i nazwisko <input name="name" required></label>
    <label>E-mail <input type="email" name="email" required></label>
    <label>Telefon <input type="tel" name="phone"></label>
    <label>Wiadomość <textarea name="msg" rows="6" required></textarea></label>
    <button class="btn" type="submit">Wyślij <span class="arr">→</span></button>
    <p class="note">{FORM_NOTE}</p>
  </form>
</div></section>
"""
    return head("Kontakt — dystrybutor manekinów SRP") + body + footer()

def page_segments():
    by_slug = {p["slug"]: p for p in PRODUCTS}
    blocks = []
    for s in SEGMENTS:
        prods = "\n".join(
            f'<div class="card">{pic(sl, by_slug[sl]["name"], thumb=True)}<div class="body"><h3>{esc(by_slug[sl]["name"])}</h3>'
            f'<p>{esc(by_slug[sl]["short"])}</p>{btn("produkty/" + sl + ".html", "Czytaj więcej")}</div></div>'
            for sl in s["products"]
        )
        blocks.append(f"""
<section id="{s["anchor"]}" style="padding:56px 0;border-bottom:1px solid var(--line)">
  <div class="wrap">
    <h2>{esc(s["name"])}</h2>
    <p class="lead">{esc(s["desc"])}</p>
    <div class="grid4" style="margin-top:30px">{prods}</div>
    <div style="margin-top:26px">{btn("zapytanie-ofertowe.html", "Umów pokaz dla swojej jednostki")}</div>
  </div>
</section>""")
    body = f"""
<div class="page-head"><div class="wrap"><h1>Dla kogo</h1>
<p>Ten sam manekin może służyć zupełnie różnym celom — dlatego zamiast katalogu pokazujemy
rozwiązania: co sprawdza się w Twojej służbie i od czego warto zacząć.</p></div></div>
{''.join(blocks)}
"""
    return head("Manekiny dla straży, wojska i szpitali") + body + footer()

def page_compare():
    thead = "<tr><th>Cecha</th>" + "".join(f"<th>{esc(n)}</th>" for _, n in COMPARE_COLS) + "</tr>"
    rows = "\n".join(
        f"<tr><th>{esc(feat)}</th>" + "".join(f"<td>{esc(v)}</td>" for v in vals) + "</tr>"
        for feat, vals in COMPARE_ROWS
    )
    links = "<tr><th>Karta produktu</th>" + "".join(
        f'<td><a href="produkty/{sl}.html"><strong>Zobacz →</strong></a></td>' for sl, _ in COMPARE_COLS) + "</tr>"
    body = f"""
<div class="page-head"><div class="wrap"><h1>Porównanie manekinów</h1>
<p>Wszystkie manekiny lądowe SRP w jednej tabeli — od podstawowej ewakuacji po pełną medycynę
taktyczną. Jeśli potrzebujesz pomocy w doborze, po prostu opisz nam swoje scenariusze ćwiczeń.</p></div></div>
<section><div class="wrap">
  <div class="cmp-scroll"><table class="cmp"><thead>{thead}</thead><tbody>{rows}{links}</tbody></table></div>
  <p class="note" style="margin-top:16px">Do ćwiczeń w wodzie zobacz osobno:
  <a href="produkty/manekiny-ratownictwa-wodnego.html">manekiny do ratownictwa wodnego</a> oraz
  <a href="produkty/manekin-wodny-rko.html">manekin wodny z funkcją RKO</a>.</p>
  <div style="margin-top:26px"><a class="btn solid" href="zapytanie-ofertowe.html">Poproś o wycenę wybranych modeli <span class="arr">→</span></a></div>
</div></section>
"""
    return head("Porównanie manekinów ratowniczych") + body + footer()

def page_tenders():
    body = f"""
<div class="page-head"><div class="wrap"><h1>Zamówienia publiczne</h1>
<p>Kupujesz w trybie ustawy Pzp? Przygotowanie dobrego postępowania na sprzęt szkoleniowy to nasza
codzienność — pomagamy na każdym etapie, od szacowania wartości po dostawę i odbiór.</p></div></div>
<section><div class="wrap grid2" style="align-items:start">
  <div>
    <h2>Jak wspieramy zamawiających</h2>
    <ul class="feat">
      <li><strong>Opis przedmiotu zamówienia</strong> — przekazujemy neutralne opisy techniczne z mierzalnymi parametrami (wymiary, masy, materiały, certyfikaty), gotowe do wykorzystania w OPZ</li>
      <li><strong>Szacowanie wartości zamówienia</strong> — niewiążąca wycena do ustalenia budżetu postępowania</li>
      <li><strong>Dokumenty</strong> — certyfikaty TÜV, wyniki testów ogniowych (EN ISO 6941, FAR 25.853b), deklaracje, karty katalogowe, numery NSN dla jednostek wojskowych</li>
      <li><strong>Stabilność oferty</strong> — utrzymujemy ceny i terminy w całym okresie związania ofertą</li>
      <li><strong>Realizacja</strong> — dostawa z protokołem odbioru, szkolenie wdrożeniowe, gwarancja i serwis w Polsce</li>
    </ul>
    <div style="margin-top:22px"><a class="btn solid" href="zapytanie-ofertowe.html">Zapytaj o materiały do postępowania <span class="arr">→</span></a></div>
  </div>
  <div>
    <h2>Dlaczego parametry mają znaczenie</h2>
    <p class="lead">Najtańszy manekin w postępowaniu rzadko jest najtańszy w eksploatacji. Parametry,
    które warto ująć w kryteriach, by porównywać porównywalne:</p>
    <ul class="feat">
      <li>materiał poszycia i konstrukcja szwów (skóra, podwójne szwy, wzmocnione punkty przeciążeń)</li>
      <li>certyfikowana odporność ogniowa przy ćwiczeniach z temperaturą</li>
      <li>zakres mas i anatomiczne wyważenie (realizm ewakuacji)</li>
      <li>dostępność serwisu, części i gwarancja na terenie Polski</li>
      <li>możliwość rozbudowy (moduły ran, RKO, drogi oddechowe) zamiast wymiany sprzętu</li>
    </ul>
    <p class="note">Materiał ma charakter informacyjny i nie stanowi porady prawnej.</p>
  </div>
</div></section>
"""
    return head("Manekiny ratownicze w przetargach") + body + footer()

def page_downloads():
    items = "\n".join(
        f'<div class="dl"><div><strong>Karta katalogowa — {esc(p["name"])}</strong>'
        f'<div class="meta">PDF · [do uzupełnienia oficjalnym plikiem]</div></div>'
        f'<a class="btn" href="#">Pobierz</a></div>'
        for p in PRODUCTS
    )
    body = f"""
<div class="page-head"><div class="wrap"><h1>Do pobrania</h1>
<p>Karty katalogowe, certyfikaty i materiały do postępowań — wszystko w jednym miejscu.
Jeśli brakuje dokumentu, którego potrzebujesz, napisz: {EMAIL}.</p></div></div>
<section><div class="wrap" style="max-width:900px">
  <h2>Karty katalogowe produktów</h2>
  {items}
  <h2 style="margin-top:44px">Certyfikaty i dokumenty</h2>
  <div class="dl"><div><strong>Certyfikat TÜV — manekiny Standard / RKO / bariatryczny</strong><div class="meta">PDF · [do uzupełnienia]</div></div><a class="btn" href="#">Pobierz</a></div>
  <div class="dl"><div><strong>Wyniki testów ogniowych EN ISO 6941 / FAR 25.853b</strong><div class="meta">PDF · [do uzupełnienia]</div></div><a class="btn" href="#">Pobierz</a></div>
  <div class="dl"><div><strong>Wykaz numerów NSN / kod NCAGE producenta</strong><div class="meta">PDF · [do uzupełnienia]</div></div><a class="btn" href="#">Pobierz</a></div>
  <div class="dl"><div><strong>Instrukcja konserwacji i przechowywania manekinów</strong><div class="meta">PDF · [do uzupełnienia]</div></div><a class="btn" href="#">Pobierz</a></div>
  <h2 style="margin-top:44px">Dla zamawiających (Pzp)</h2>
  <div class="dl"><div><strong>Przykładowe opisy przedmiotu zamówienia (OPZ)</strong><div class="meta">DOCX · udostępniamy na życzenie</div></div><a class="btn" href="zapytanie-ofertowe.html">Napisz do nas</a></div>
</div></section>
"""
    return head("Karty katalogowe i certyfikaty") + body + footer()

def page_faq():
    items = "\n".join(f'<details class="faq"><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q, a in FAQS)
    faq_ld = json.dumps({
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS],
    }, ensure_ascii=False)
    body = f"""
<script type="application/ld+json">{faq_ld}</script>
<div class="page-head"><div class="wrap"><h1>Pytania i odpowiedzi</h1>
<p>Wszystko, o co najczęściej pytają jednostki i firmy przed zakupem. Nie znalazłeś odpowiedzi?
Zadzwoń: {PHONE}.</p></div></div>
<section><div class="wrap" style="max-width:860px">{items}
<div style="margin-top:30px">{btn("kontakt.html", "Zadaj własne pytanie")}</div>
</div></section>
"""
    return head("Zakup manekinów — pytania i odpowiedzi") + body + footer()

ARTICLE_IMGS = {
    "jak-wybrac-manekin-ratowniczy": "produkty-01.jpg",
    "scenariusze-cwiczen-z-manekinem": "home-06.jpg",
    "kontrola-krwotokow-stop-the-bleed": "symulatory-ran",
}

def page_articles_index():
    cards = "\n".join(
        f'<div class="card">{pic(ARTICLE_IMGS.get(a["slug"]), a["title"], depth=1, thumb=True)}<div class="body"><h3>{esc(a["title"])}</h3>'
        f'<p>{esc(a["lead"])}</p>{btn(a["slug"] + ".html", "Czytaj artykuł")}</div></div>'
        for a in ARTICLES
    )
    body = f"""
<div class="page-head"><div class="wrap"><h1>Strefa wiedzy</h1>
<p>Praktyczne poradniki dla instruktorów, dowódców i osób odpowiedzialnych za szkolenia —
jak dobierać sprzęt, projektować ćwiczenia i budować kompetencje zespołu.</p></div></div>
<section><div class="wrap grid3">{cards}</div></section>
<section class="gray"><div class="wrap">
  <h2>Chcesz dostawać takie materiały?</h2>
  <p class="lead">Nowe poradniki, terminy szkoleń otwartych i informacje o produktach —
  maksymalnie raz w miesiącu.</p>
  <form {form_attrs} style="display:flex;flex-wrap:wrap;gap:12px;max-width:560px;margin-top:18px">
    <input type="email" name="email" placeholder="Twój adres e-mail" required>
    <button class="btn solid" type="submit">Zapisz się</button>
  <input type="hidden" name="typ" value="newsletter">
  <label class="consent"><input type="checkbox" name="zgoda_marketing" required> <span>Chcę otrzymywać materiały i informacje o produktach oraz szkoleniach na podany adres e-mail. Zgodę mogę wycofać w każdej chwili, a jej brak nie wpływa na możliwość kontaktu z nami. <a href="/polityka-prywatnosci.html">Informacja o przetwarzaniu danych</a>.</span></label>
  </form>
</div></section>
"""
    return head("Dobór sprzętu i scenariusze ćwiczeń", 1) + body + footer(1)

def page_article(a):
    body = f"""
<div class="wrap crumbs"><a href="../index.html">Start</a> / <a href="index.html">Strefa wiedzy</a> / {esc(a["title"])}</div>
<section style="padding-top:16px"><div class="wrap" style="max-width:860px">
  <h1 class="disp" style="font-size:clamp(30px,4vw,44px)">{esc(a["title"])}</h1>
  <p class="lead" style="margin:16px 0 18px">{esc(a["lead"])}</p>
  {pic(ARTICLE_IMGS.get(a["slug"]), a["title"], "ph wide", depth=1)}
  <div class="article-body" style="margin-top:22px">{a["body"]}</div>
  <div class="usebox" style="margin-top:36px"><strong>Potrzebujesz doradztwa?</strong> Opisz nam swoje
  scenariusze ćwiczeń — bezpłatnie doradzimy konfigurację i przygotujemy wycenę.
  <a href="../zapytanie-ofertowe.html"><strong>Wyślij zapytanie →</strong></a></div>
</div></section>
"""
    return head(a.get("seo_title", a["title"]), 1, a.get("desc", a["lead"])) + body + footer(1)

def page_privacy():
    body = f"""
<div class="page-head"><div class="wrap"><h1>Polityka prywatności</h1>
<p>Szkic do weryfikacji prawnej — [uzupełnij dane administratora przed publikacją docelową].</p></div></div>
<section><div class="wrap" style="max-width:860px">
  <h3>1. Administrator danych</h3>
  <p>Administratorem Twoich danych osobowych jest:</p>
  <p style="margin-top:8px"><strong>{NAZWA_PELNA}</strong><br>{ADRES_ULICA}<br>{ADRES_MIASTO}<br>
  NIP {NIP} &nbsp;·&nbsp; KRS {KRS} &nbsp;·&nbsp; REGON {REGON}</p>
  <p style="margin-top:8px">Kontakt w sprawach danych osobowych: <a href="mailto:{EMAIL}">{EMAIL}</a>,
  telefon {PHONE}. Spółka prowadzi sprzedaż produktów SRP w Polsce pod marką {BRAND}.</p>
  <h3 style="margin-top:26px">2. Jakie dane przetwarzamy i po co</h3>
  <p>Przetwarzamy wyłącznie dane przekazane dobrowolnie w formularzach: imię i nazwisko, nazwę
  organizacji, adres e-mail, numer telefonu, NIP oraz treść wiadomości — w celu obsługi zapytania
  ofertowego lub kontaktowego (art. 6 ust. 1 lit. b i f RODO), a po zapisie na materiały — w celu ich
  wysyłki (art. 6 ust. 1 lit. a RODO, zgoda).</p>
  <h3 style="margin-top:26px">3. Okres przechowywania</h3>
  <p>Dane z zapytań przechowujemy przez okres prowadzenia korespondencji i wymagany przepisami
  (np. podatkowymi przy zawarciu umowy). Dane newslettera — do wycofania zgody.</p>
  <h3 style="margin-top:26px">4. Odbiorcy danych</h3>
  <p>Dane mogą być powierzane podmiotom obsługującym naszą pocztę, hosting i formularze
  [wymień dostawców po podpięciu, np. operator formularzy] — wyłącznie w zakresie niezbędnym
  do świadczenia tych usług.</p>
  <h3 style="margin-top:26px">5. Twoje prawa</h3>
  <p>Masz prawo dostępu do danych, ich sprostowania, usunięcia, ograniczenia przetwarzania,
  przenoszenia, sprzeciwu oraz wniesienia skargi do Prezesa UODO. Wycofanie zgody nie wpływa
  na zgodność z prawem wcześniejszego przetwarzania.</p>
  <h3 style="margin-top:26px">6. Pliki cookies</h3>
  <p>Strona nie używa własnych plików cookies ani narzędzi śledzących. Czcionki ładowane są
  z Google Fonts (Google LLC może rejestrować adres IP przy pobraniu czcionki). [Zaktualizuj
  po dodaniu analityki.]</p>
</div></section>
"""
    return head("Polityka prywatności") + body + footer()


def page_404():
    """Serwer podaje ten plik pod dowolnym brakującym adresem, więc wszystkie
    odnośniki muszą być bezwzględne — inaczej style i nawigacja się rozjadą."""
    body = f"""
<div class="page-head"><div class="wrap"><h1>Nie ma takiej strony</h1>
<p>Adres jest nieaktualny albo zawiera literówkę. Poniżej najczęściej szukane miejsca.</p></div></div>
<section><div class="wrap">
  <div class="grid3">
    <div class="card"><div class="body"><h3>Produkty</h3>
      <p>Manekiny ratownicze, symulatory ran i trenażery medyczne — pełny katalog z danymi technicznymi.</p>
      {btn("/produkty/index.html", "Zobacz katalog")}</div></div>
    <div class="card"><div class="body"><h3>Porównanie modeli</h3>
      <p>Wszystkie manekiny lądowe w jednej tabeli — od ewakuacji po medycynę taktyczną.</p>
      {btn("/porownanie-manekinow.html", "Porównaj")}</div></div>
    <div class="card"><div class="body"><h3>Kontakt</h3>
      <p>Zadzwoń: {PHONE} lub napisz na {EMAIL} — odpowiadamy w ciągu dnia roboczego.</p>
      {btn("/kontakt.html", "Napisz do nas")}</div></div>
  </div>
</div></section>
"""
    html_out = head("Nie ma takiej strony") + body + footer()
    # zamiana ścieżek względnych na bezwzględne
    import re as _r
    html_out = _r.sub(r'(href|src)="(?!/|https?:|mailto:|tel:|#|data:)', r'\1="/', html_out)
    return html_out

def write_seo_files():
    pages = (["index.html", "produkty/index.html"]
             + [f"produkty/{p['slug']}.html" for p in PRODUCTS]
             + ["dla-kogo.html", "porownanie-manekinow.html", "zamowienia-publiczne.html",
                "do-pobrania.html", "faq.html", "wiedza/index.html"]
             + [f"wiedza/{a['slug']}.html" for a in ARTICLES]
             + ["szkolenia.html", "warunki-zakupu.html", "zapytanie-ofertowe.html",
                "o-nas.html", "aktualnosci.html", "kontakt.html", "polityka-prywatnosci.html"])
    base = BASE_URL
    urls = "\n".join(f"  <url><loc>{base}/{u}</loc></url>" for u in pages)
    write("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n')
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {base}/sitemap.xml\n")

    # CNAME jest potrzebny wyłącznie przy hostingu na GitHub Pages
    cname_path = os.path.join(ROOT, "CNAME")
    if DOMAIN_ACTIVE and HOSTING == "pages":
        write("CNAME", DOMAIN + "\n")
    elif os.path.exists(cname_path):
        os.remove(cname_path)
        print("✓ usunięto CNAME (hosting: %s)" % HOSTING)

# ---------------------------------------------------------------- build
def main():
    write("css/style.css", CSS)
    write("index.html", page_home())
    write("produkty/index.html", page_products_index())
    for p in PRODUCTS:
        write(f"produkty/{p['slug']}.html", page_product(p))
    write("szkolenia.html", page_trainings())
    write("warunki-zakupu.html", page_terms())
    write("zapytanie-ofertowe.html", page_quote())
    write("o-nas.html", page_about())
    write("aktualnosci.html", page_news())
    write("kontakt.html", page_contact())
    write("dla-kogo.html", page_segments())
    write("porownanie-manekinow.html", page_compare())
    write("zamowienia-publiczne.html", page_tenders())
    write("do-pobrania.html", page_downloads())
    write("faq.html", page_faq())
    write("polityka-prywatnosci.html", page_privacy())
    write("404.html", page_404())
    write("wiedza/index.html", page_articles_index())
    for a in ARTICLES:
        write(f"wiedza/{a['slug']}.html", page_article(a))
    write_seo_files()
    print("\nGotowe — otwórz index.html")

if __name__ == "__main__":
    main()
