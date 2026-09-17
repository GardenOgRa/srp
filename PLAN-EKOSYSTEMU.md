# Ekosystem automatyzacji SRP Polska — plan rozbudowy

Wersja: 2026-07-18. Strategia: **małe, niezależne klocki spięte przez n8n** — żaden element
nie jest wpisany na stałe w kod strony, więc każdy da się wymienić bez przebudowy całości.
Rynek (przetargi, kanały social, ceny narzędzi AI) zmienia się szybko — architektura ma to
przetrwać.

---

## Zasady architektury (dlaczego tak, a nie inaczej)

1. **Strona = front, nie system.** Statyczne HTML na GitHub Pages: zero serwera do
   utrzymania, zero kosztów, brak powierzchni ataku. Cała logika żyje w n8n.
2. **n8n = kręgosłup i Wasza własność.** Integracje wchodzą i wychodzą (HubSpot dziś,
   coś innego za rok) — przepływy zostają.
3. **Dane oddzielone od kodu** (`data/site.json`): automat może zmienić treść strony
   (np. dopisać meldunek) bez dotykania szablonów.
4. **Buduj tylko to, co Was wyróżnia** (konfigurator doboru, meldunek, baza wiedzy).
   CRM, mailing, agregator przetargów — wynajmować, nie pisać.
5. **Człowiek domyka sprzedaż.** Automat dowozi ciepłe leady i nie gubi żadnego;
   pokazu i rozmowy z komendantem nie automatyzujemy.
6. **Każdy automat ma bramkę akceptacji** tam, gdzie publikuje w imieniu firmy
   (posty, maile, artykuły) — patrz „Zasady bezpieczeństwa marki".

---

## ETAP 0 — MVP (to budujemy teraz, bez dostępów zewnętrznych)

| # | Element | Status |
|---|---------|--------|
| 0.1 | GitHub Actions: auto-build i deploy po każdej zmianie | ✅ w tym commicie |
| 0.2 | Dane strony w `data/site.json` (meldunek, kontakt, opinie) | ✅ w tym commicie |
| 0.3 | Formularze gotowe pod webhook (jeden przełącznik `FORM_ENDPOINT`) | ✅ w tym commicie |
| 0.4 | Endpoint dla automatu: dopisanie meldunku = edycja JSON → strona sama się przebuduje | ✅ w tym commicie |

Efekt: n8n (albo Ty z telefonu) zmienia jeden plik JSON w repo → strona publikuje się sama.

---

## ETAP 1 — Lead nie ginie (tydzień 1)

- **1.1 Formularze → n8n → CRM.** Kontakt, zapytanie ofertowe, newsletter, konfigurator.
  n8n: walidacja → scoring (przetarg/pokaz = wysoki) → CRM + powiadomienie push/Slack.
- **1.2 Autoresponder < 5 min** z katalogiem PDF i linkiem do kalendarza.
- **1.3 Samoobsługowe umawianie pokazów** (cal.com) zamiast „oddzwonimy".
- **1.4 CRM.** Start: HubSpot Free lub ClickUp (już używany). Spinany przez n8n, nie wprost.

**Potrzebne od Was:** adres e-mail na leady, instancja n8n, decyzja CRM.

---

## ETAP 2 — Popyt sam się zgłasza (tydzień 1–2)

- **2.1 Monitoring przetargów (własny, ~0 zł):** n8n odpytuje ezamowienia.gov.pl i TED
  po frazach: manekin ratowniczy, fantom, symulator ran, pozoracja, szkolenie RKO,
  Stop the Bleed, sprzęt do ćwiczeń ratowniczych → codzienny alert + wpis do CRM.
- **2.2 Test agregatora komercyjnego** (1 miesiąc, ~150–300 zł): łapie zapytania poniżej
  progów z platform zakupowych, których BZP nie pokazuje. **Decyzja po liczbach:**
  ile ogłoszeń ponad to, co złapał własny robot.
- **2.3 Konfigurator doboru manekina** na stronie (quiz → rekomendacja + lead).
- **2.4 Gated content:** wzory OPZ i karty katalogowe za e-mail.

---

## ETAP 3 — Research i obecność w społecznościach (tydzień 2–4)

> Cel: wiedzieć, o czym mówi rynek, i być tam, gdzie zapadają decyzje — **bez spamu**.

- **3.1 Nasłuch (w pełni automatyczny, bezpieczny):**
  - RSS/API: portale pożarnicze i ratownicze, komunikaty PSP/KG PSP, MON, NFZ,
    branżowe newsy o szkoleniach i symulacji medycznej;
  - Reddit API (r/ems, r/firefighting, r/tacticalmedicine), YouTube, publiczne fora
    branżowe — pobieranie tylko tego, co udostępniają API/RSS i regulamin serwisu;
  - Google Alerts + Search Console: o co ludzie realnie pytają w wyszukiwarce.
  - Wyjście: **cotygodniowy briefing tematyczny** (co boli rynek, jakie pytania wracają,
    jakie przetargi/wydarzenia na horyzoncie) → wsad do artykułów i newslettera.
- **3.2 Wykrywanie okazji:** alert, gdy w monitorowanych źródłach pada pytanie
  o dobór fantomów/scenariusze ćwiczeń → trafia do kolejki „warto odpowiedzieć”.
- **3.3 Odpowiedzi na forach/grupach — PÓŁautomat (świadoma decyzja):**
  automat przygotowuje szkic merytorycznej odpowiedzi + link do naszego poradnika,
  **człowiek publikuje z własnego, imiennego konta.** Uzasadnienie w sekcji
  „Zasady bezpieczeństwa marki”.
- **3.4 LinkedIn (firmowy):** publikacja przez oficjalne API, z akceptacją jednym
  kliknięciem. Źródła postów: nowy artykuł, nowy meldunek, nowe szkolenie.

---

## ETAP 4 — Treść, która pisze się sama (tydzień 3–6)

- **4.1 Redakcja artykułów (AI + akceptacja):** briefing z etapu 3 → szkic artykułu
  do strefy wiedzy (struktura, SEO, CTA) → **Twoja akceptacja** → publikacja
  (commit do repo → auto-deploy) → post na LinkedIn → wzmianka w newsletterze.
  Kadencja startowa: 1 artykuł/tydzień.
- **4.2 Newsletter (AI redaguje, człowiek zatwierdza):** miesięczny numer składany
  automatycznie z: nowych artykułów, meldunków, terminów szkoleń, jednej porady
  praktycznej. Narzędzie: MailerLite/Brevo (darmowe do ~1000 kontaktów).
- **4.3 Sekwencja powitalna (raz napisana, działa latami):** 5–7 maili
  segmentowanych po typie organizacji z formularza (straż ≠ szpital ≠ wojsko).
- **4.4 Repurposing:** artykuł → karuzela na LinkedIn → skrypt na short → grafika.

---

## ETAP 5 — Sprzedaż bez przepisywania danych (miesiąc 2)

- **5.1 Generator ofert PDF** z konfiguracji klienta (n8n + szablon).
- **5.2 E-podpis** (Autenti) na umowach i protokołach odbioru.
- **5.3 Fakturowanie** (Fakturownia/inFakt) + automatyczne monity o płatność.
- **5.4 Pipeline w CRM** z automatycznymi follow-upami (3/7/21 dni po ofercie).

---

## ETAP 6 — Przychód powtarzalny (miesiąc 2–3) ⭐ największy potencjał

- **6.1 Rejestracja sprzętu** na stronie (nr seryjny) → automatyczne: przegląd po 12 mies.,
  koniec gwarancji, instrukcje konserwacji.
- **6.2 Cykliczne uzupełnianie eksploatacji** (krew symulacyjna, gaza, części) —
  model „maszynka i żyletki”: mail w cyklu do każdego posiadacza fantomu.
- **6.3 Mini-sklep na akcesoria** (linki płatności Stripe/Przelewy24 — działa
  ze statycznej strony, bez backendu). Fantomy sprzedaje pokaz; akcesoria mają
  sprzedawać się same.
- **6.4 Certyfikaty szkoleń PDF** + automatyczne przypomnienie o recertyfikacji
  (szkolenie staje się przychodem cyklicznym).
- **6.5 Automat opinii:** 2 tyg. po dostawie ankieta → zgoda na cytat → sekcja opinii.

---

## ETAP 7 — Koło zamachowe i pomiar (ciągłe)

- **7.1 Pętla:** dostawa w CRM → wpis do meldunku na stronie → post → ruch → leady → pokaz
  → dostawa. Bez ręcznej publikacji.
- **7.2 Analityka:** Plausible (bez bannera cookies) + Search Console; miesięczny raport
  automatyczny: ruch, źródła, leady, pokazy, koszt leada.
- **7.3 AI-czat na stronie** (na treściach serwisu): odpowiada 24/7, kwalifikuje, umawia pokaz.
- **7.4 Monitoring dostępności** strony + backup leadów.

---

## Zasady bezpieczeństwa marki (nienegocjowalne)

1. **Żadnych automatycznych postów na forach i grupach z kont firmowych.**
   Regulaminy Facebooka, LinkedIna i większości forów branżowych zakazują automatycznego
   publikowania i masowych wiadomości — realne ryzyko to blokada konta i (gorzej)
   spalenie reputacji w środowisku, które jest małe i pamiętliwe. Strażacy i ratownicy
   wyczuwają automat natychmiast. Dlatego: **automat researchuje i pisze szkic,
   człowiek publikuje.**
2. **Zero fikcji w treściach:** opinie, referencje, meldunki — wyłącznie prawdziwe
   (dyrektywa Omnibus, kary UOKiK, a przede wszystkim wiarygodność wobec instytucji).
3. **Artykuły i newsletter przed publikacją akceptuje człowiek** — AI myli się
   w szczegółach technicznych (wymiary, normy, procedury medyczne), a tu błąd
   merytoryczny kosztuje zaufanie klienta, którego zdobycie zajęło miesiące.
4. **RODO:** zgody marketingowe zbierane osobno, polityka prywatności aktualizowana
   przy każdej nowej integracji, dane leadów tylko w CRM (nie w repo).
5. **Prawa do materiałów SRP** (zdjęcia, filmy, logo) — potwierdzenie od producenta.

---

## Odporność na zmienność rynku

- **Wymienne klocki:** CRM, mailing, agregator przetargów i model AI da się wymienić
  w godzinę (zmiana węzła w n8n), bo nic z tego nie jest wpisane w kod strony.
- **Dane u Was:** kontakty w CRM z regularnym eksportem, treści w repo (Git = historia),
  przepływy w n8n (self-hosted) — żaden dostawca nie trzyma Was zakładnikiem.
- **Start na darmowych planach**, płatne dopiero, gdy licznik pokaże zwrot.
- **Kwartalny przegląd:** co działa, co wyłączamy, gdzie rynek się przesunął.

---

## Kolejność wdrożenia (rekomendacja)

1. **ETAP 0** (teraz) — fundament, bez niego nic dalej nie zadziała.
2. **ETAP 1 + 2** — leady i przetargi = najkrótsza droga do gotówki.
3. **ETAP 3 + 4** — research, artykuły, newsletter = budowa pozycji eksperta.
4. **ETAP 6** — przychód powtarzalny.
5. **ETAP 5 + 7** — usprawnienia i pomiar.

## Stack (potwierdzony 2026-07-18)

| Warstwa | Narzędzie | Status |
|---------|-----------|--------|
| Automatyzacja | **n8n** (własna instancja) | ✅ jest |
| CRM / marketing | **HubSpot** | ✅ jest |
| Zadania / projekty | **ClickUp** | ✅ jest |
| Hosting, domeny, poczta | **cyber_Folks** | ✅ jest |
| Strona WWW | GitHub Pages + auto-build (Actions) | ✅ działa |
| Domena | **srp-polska.pl** (jedna, bez dodatkowych) | do rejestracji |

Podział ról: HubSpot = kontakty, deale, maile marketingowe. ClickUp = realizacja
(dostawy, szkolenia, serwis). n8n = spina wszystko i aktualizuje stronę.
cyber_Folks = domena i poczta firmowa (biuro@srp-polska.pl), strona zostaje na Pages.

## Blokery po stronie klienta (bez tego stoimy)

- [ ] rejestracja domeny srp-polska.pl w cyber_Folks + DNS (instrukcja w README)
- [ ] zgoda producenta na użycie znaku „SRP" w domenie (mail wystarczy)
- [ ] adres e-mail na leady i alerty
- [ ] URL webhooka n8n do `data/site.json`
- [ ] dane firmy: pełna nazwa, telefon, adres, NIP
- [ ] prawdziwe dostawy do meldunku
- [ ] logotypy certyfikatów (STB / ERC / TECC)

## Aktualizacja 2026-09-08 — badanie odbiorców instytucjonalnych w Polsce

Zlecone przez użytkownika: przygotowanie briefu i promptu do Perplexity dla jednostek szkoleniowych, ośrodków szkolenia straży pożarnej i Policji oraz odpowiednich instytucji szkoleniowych. Cel: weryfikacja potencjału SRP poprzez mapę podmiotów, potwierdzonych zastosowań szkoleniowych i oficjalnych kontaktów. Jest to rozszerzenie etapu 3.1, powiązane z 2.1 i 7.2, a nie osobny plan.

Status: brief i gotowy prompt przygotowane; badanie nieuruchomione. Artefakt: /Users/ogr/Documents/Codex/2026-09-07/jeste-osobnym-koordynatorem-grupy-srp-utworzonym/outputs/SRP-brief-i-prompt-Perplexity.md.

| Etap | Właściciel | Zależności | Wynik i warunek odbioru | Status |
|---|---|---|---|---|
| 3.1a Przygotowanie badania | Koordynator SRP | Karta projektu, istniejący plan, katalog zastosowań | Brief i samodzielny prompt: Polska, segmenty, kwalifikacja, oficjalne kontakty ze źródłami i datami, deduplikacja, oddzielenie faktów od hipotez | Wykonane; do odbioru przez asystenta głównego |
| 3.1b Badanie odbiorców | Wykonawca badania: Perplexity, uruchomienie przez użytkownika/asystenta głównego po osobnym zleceniu | Zlecenie uruchomienia; bieżący etap nie autoryzuje płatnego researchu | Tabela instytucji, kontakty bez zgadywania, źródła działalności i kontaktu, zakres pokrycia Polski, kolejka niepewności i rejestr duplikatów | Przygotowane do zlecenia, nieuruchomione |
| 3.1c Kontrola wyników i wybór segmentów | Koordynator SRP; decyzje biznesowe: użytkownik | Wynik 3.1b | Kontrola wszystkich rekordów A i minimum 10 pozostałych lub wszystkich przy mniejszej liczbie; udokumentowane luki; maksymalnie 3 rekomendowane segmenty z oddzieleniem rekomendacji od decyzji | Propozycja kolejnego kroku |

Najbliższe priorytety koordynacji (maksymalnie trzy):
1. Przekazać i odebrać brief badania 3.1a zgodnie z bieżącym zleceniem.
2. Zachować otwartą kontrolę trwałego zapisu kontaktów i zgód w etapie 1.1 — aktualny dowód HubSpot pozostaje nieuzyskany; brak dostępu do integracji nie blokuje przygotowania briefu.
3. Po osobnym uruchomieniu badania sprawdzić jego wynik i zaproponować segmenty do dalszej weryfikacji potencjału, bez automatycznego kontaktowania się z podmiotami.

Publiczny kontakt nie jest zgodą marketingową. Lista badawcza nie jest potwierdzeniem popytu ani listą do automatycznej wysyłki. Przygotowanie nie obejmuje wiadomości do instytucji, importu do CRM, publikacji ani uruchamiania automatyzacji. Nie zmienia decyzji dotyczących zdjęć i SEO. Wcześniejsze historyczne statusy planu nie stają się przez ten wpis zweryfikowanymi wynikami.

## Sterowanie przepływem i zamknięcie dnia — 2026-09-08

Ta sekcja wraz z aktualizacją badania powyżej określa bieżący przepływ. Lipcowe tygodnie, koszty i oznaczenia „teraz” są historyczne; nie są nowymi zobowiązaniami. Cel bieżący: zweryfikować potencjał SRP i doprowadzić uzasadniony zakres do mierzalnego procesu pozyskania i obsługi zapytań. Dalsze moduły ekosystemu pozostają w tym samym planie, lecz ich realizacja zależy od wyników i decyzji użytkownika.

### Obecny etap i dowody

Obecny etap: kontrola fundamentu (0/1.1) i przygotowanie badania odbiorców (3.1a). Wykonawca „Kopia strony SRP dla rynku polskiego”, ID 01a07b42-5b11-7c83-a14f-7b7482a3f87a, zakończył zleconą kontrolę; stan zadania idle sprawdzony 8 września. Koordynator odebrał raport i wykonał niezależną kontrolę lokalną.

| Wynik | Status na koniec dnia | Dowód / ograniczenie |
|---|---|---|
| Newsletter: zgoda w formularzu, required, endpoint | Zweryfikowane lokalnie | Parser HTML index.html i wiedza/index.html, 2026-09-08; nie jest to nowy test produkcyjny |
| Podpisy filmów PRO ELITE oraz pobieranie | Zweryfikowane lokalnie | HEAD fb95b87; oba podpisy bez uwagi roboczej; 0 href="#" na do-pobrania.html |
| Materiały PDF | Zablokowane brakiem materiałów | 0 PDF w pliki/; tabela braków pliki/README.md; przekazanie od producenta niepotwierdzone |
| Dane firmy, domena, webhook, konfiguracja publikacji | Zweryfikowana konfiguracja lokalna | data/site.json, CNAME, .github/workflows/build-deploy.yml; dawne blokery konfiguracji częściowo nieaktualne, działanie usług wymaga aktualnego dowodu |
| Produkcyjny newsletter i powiadomienia | Historyczny raport wykonawcy | Wykonania n8n #21123 i #21124; brak nowej kontroli aktywnej wersji |
| Trwały zapis kontaktów/zgód HubSpot | Niezweryfikowane, kontrola zablokowana dostępem | Brak aktualnej sesji n8n i dowodu utworzenia kontaktu; 1.1 nieodebrane |
| Brief i prompt Perplexity | Wykonane, badanie nieuruchomione | Artefakt wskazany w sekcji 3.1a; nie ma jeszcze wyników rynku |
| Aktualizacja jednego planu | Wykonane po zapisie tej sekcji | PLAN-EKOSYSTEMU.md; bez publikacji, push i zmian kodu |

Niedomknięte: odbiór produkcji, kontrola HubSpot, pozyskanie PDF, rozstrzygnięcie galerii i dokumentów producenta. Nie deklarujemy ich wykonania na podstawie dawnych opisów.

### Droga do wdrożenia i dalszego rozwoju

Terminy poniżej są propozycją kolejności i założeniami, nie zaakceptowanym terminem ukończenia. D = dzień spełnienia zależności i zlecenia danego etapu. Właściciel techniczny oznacza istniejące zadanie „Kopia strony SRP dla rynku polskiego”; koordynacja i odbiór dowodów — koordynator SRP. Nie tworzymy nowych wykonawców.

| Etap istniejącego planu | Rezultat | Właściciel | Zależności | Termin / założenie | Warunek odbioru |
|---|---|---|---|---|---|
| 0 — fundament | Wiarygodny stan wdrożonej strony | Właściciel techniczny; odbiór koordynator | Odczyt produkcji i historii wdrożeń | 9.09: kontrola, jeśli dostępna | Aktualny commit wdrożenia i odczyt obu formularzy, linków oraz strony kontaktowej; rozdzielenie lokalne/produkcyjne |
| 3.1a–c — rozpoznanie rynku | Mapa kwalifikowanych instytucji i wybór segmentów | Brief/QA: koordynator; badanie: Perplexity po zleceniu; wybór: Radek | Gotowy brief, zlecenie uruchomienia | 9.09: przekazanie; wynik zależny od uruchomienia; QA do D+2 dni roboczych | Podmioty z oficjalnymi źródłami, deduplikacją, faktami i hipotezami; kontrola rekordów wg briefu |
| 1 — lead i obsługa | Trwały kontakt, rozróżniony newsletter, odpowiedź i odpowiedzialność za lead | Właściciel techniczny; odbiór biznesowy Radek | Dostęp n8n/HubSpot, ustalenie mapowania i sposobu obsługi | 9–10.09: kontrola; wdrożenie po odblokowaniu, szacunek po przeglądzie | Dowód zapisu bez duplikatów, zgoda/źródło/czas, obsługa błędów; test izolowany; produkcja i wysyłki tylko w uprawnionym zakresie |
| 7.2 — pomiar bazowy | Mierzalna droga źródło → zapytanie → pokaz → oferta → sprzedaż | Właściciel techniczny; definicje i decyzje Radek | Dostęp Search Console i danych CRM, potwierdzenie 1.1 | Definicje równolegle z 1; pomiar po działającym zapisie | Dostęp do usługi, uzgodnione wskaźniki i źródła, raport bazowy z jawnymi brakami; liczba instytucji nie jest popytem |
| 2 — pozyskanie popytu | Trafne przetargi, kwalifikacja zainteresowania, materiały | Właściciel techniczny; ocena trafności Radek | Segmenty z badania, odbiór 1, dokumenty producenta; decyzja o ewentualnym wydatku | Po odbiorze 1 i wynikach badania; propozycja pilotażu 2 tygodnie | Próbka ogłoszeń z terminami/źródłami i deduplikacją; ocena trafności; brak fikcyjnych PDF i obietnic |
| 3–4 — treści i kanały | Treści oparte na potrzebach rynku i mierzalny ruch | Właściciel techniczny; akceptacja treści Radek | Wyniki badania, poprawny pomiar, materiały i osobne zatwierdzenie publikacji | Po pilotażu 2; propozycja przeglądu po 4 tygodniach | Zatwierdzone treści, źródła, pomiar wejść i zapytań; publikacja przez człowieka tam, gdzie wymaga tego plan |
| 5 — obsługa sprzedaży | Oferta i realizacja bez utraty informacji | Właściciel techniczny; proces i odbiór Radek | Zweryfikowany CRM, rzeczywiste oferty, ustalone narzędzia i dane | Po pierwszych rzeczywistych okazjach; estymacja po wyborze zakresu | Przejście przykładowej sprawy od zapytania do oferty i realizacji, poprawność danych, kontrola wysyłek i błędów |
| 6 — obsługa po sprzedaży | Serwis, eksploatacja i szkolenia powtarzalne | Właściciel techniczny; zasady handlowe Radek | Rzeczywiste dostawy, numery sprzętu, warunki serwisu, decyzja o module | Po odbiorze procesu sprzedaży; termin po uzyskaniu danych | Zweryfikowany cykl dla rzeczywistego lub izolowanego testowego przypadku; brak nieuzgodnionych płatności i wiadomości |
| 7 — eksploatacja i optymalizacja | Stabilny system, backup i decyzje o rozwoju | Właściciel techniczny; priorytety Radek i koordynator | Odebrane wdrożenia, dostęp do pomiaru | Po odbiorze podstawowego przepływu; propozycja przeglądu co miesiąc | Odtwarzalny backup, widoczne błędy, wskaźniki lejka; każda zmiana ma właściciela, wynik i dowód |

Kamień milowy podstawowego wdrożenia: potwierdzona strona, trwały zapis kontaktów, uzgodniona obsługa zapytania, pomiar i odebrany pilotaż jednego kanału pozyskania. Rozbudowa etapów 4–6 i czatu 7.3 wymaga uzasadnienia wynikami; nie startuje automatycznie. Ocena potencjału biznesowego następuje po badaniu i pilotażu: użytkownik ustala progi powodzenia przed pilotażem, a następnie podejmuje decyzję kontynuuj/zmień zakres/wstrzymaj. Nie obiecujemy daty ani wyniku sprzedaży bez danych.

### Najbliższe dni — maksymalnie trzy wyniki

1. 9 września: odbiór briefu i promptu przez asystenta głównego; ustalenie uruchomienia badania w dostępnym trybie, bez automatycznego zakupu. Właściciel: koordynator; uruchomienie: asystent główny/użytkownik.
2. 9–10 września, jeśli dostęp zostanie zapewniony: dowód aktualnej produkcji i trwałego zapisu HubSpot albo konkretna lista braków. Właściciel: istniejący wykonawca techniczny. Dostęp i decyzje konta: Radek. Nie powtarzać bezcelowo prób przy niezmienionej blokadzie.
3. Od 10 września lub do 2 dni roboczych od dostarczenia wyników: kontrola badania i propozycja maksymalnie 3 segmentów do pilotażu z miernikami odbioru. Właściciel: koordynator; wybór segmentów i progów powodzenia: Radek. Jeśli wyników nie ma, status oczekuje, bez wymyślania danych.

### Otwarte decyzje i odpowiedzialność

- Uruchomienie badania: gotowe do przekazania; bieżące zlecenie obejmowało przygotowanie. Właściciel: asystent główny/Radek. Płatny tryb lub zakup wymaga osobnego zlecenia.
- Dostęp do właściwych usług n8n/HubSpot oraz Search Console: Radek; wykonawca określa brak po odczycie, bez ujawniania sekretów. Historyczna blokada DNS nie jest nowym dowodem stanu konta.
- Materiały PDF i uprawnienia do ich wykorzystania: Radek/producent; brak nowych potwierdzeń. Nie wysłano prośby do producenta w tym zakresie.
- Galeria wodna: wskazanie zdjęcia 03, 05 albo obu pozostaje otwarte wg ostatniego raportu; nie usunięto materiałów. SEO 8711041: brak nowej decyzji o cofnięciu; nie cofnięto.
- Progi pilotażu, wybór segmentów i dalsze wydatki: Radek po odebraniu danych, bez domyślnej zgody wynikającej z obecności w planie.

Start dnia: sprawdzić obecny etap, do 3 wyników, właścicieli i zależności; zamknięcie: dowody, status niewykonanych punktów i następny krok. Raport zbiera asystent główny. Nie utworzono żadnego harmonogramu ani nowej sesji.


## Przekazanie aktywnej realizacji do Claude — 2026-09-08

Radek zlecił eksport kontekstu i wznowienie istniejącej sesji Claude. Źródło przekazania: HANDOFF-CLAUDE.md w tym repo. Wykonawca Codex zakończył kontrolę; nie uruchamiamy równoległej implementacji. Wznowienie Claude Desktop podlega potwierdzeniu odpowiedzi w UI.

Nowo odczytane źródło biznesowe: istniejąca sesja Claude „SRP Polska handoff” zawiera polecenie Radka rozpoczęcia 10.09 i limitu 2 h/dzień; historyczny raport wykonawcy: 31 zadań ClickUp, 10.09–27.10, 2 h/dzień/osoba. To źródło uzgadniamy z tym planem, bez duplikowania zadań. Wcześniejsze proponowane terminy techniczne 9–10.09 nie zmieniają harmonogramu ludzi. Aktualnego stanu ClickUp nie sprawdzono. Claude ma powiązać istniejące zakresy biznesowy i techniczny oraz dopisać dowody i raport zwrotny do tego planu.

## Decyzje i kierunek — 2026-09-17 (Radek, sesja „Kopia strony SRP dla rynku polskiego")

Radek zniósł zakaz edycji planu i kodu z 8.09 i zlecił: strona na światowym poziomie z widocznymi elementami AI, klient „zaopiekowany", plan realizowany i unowocześniany sukcesywnie. Decyzje zapadły w trzech rundach pytań (32 pytania); poniżej stan wiążący. Raport przejęcia z 8.09 pozostaje historią (lokalnie, poza publicznym repozytorium).

### Decyzje wiążące
| Obszar | Decyzja | Konsekwencja |
|---|---|---|
| Marka | Sub-marka producenta „SRP Polska" (żółty/czerń SRP) z sygnaturą TURBOMEDIC. Producent dał zgodę na logo, materiały, nazwę, domenę i social (wg Radka 17.09; kopia pisemna do `ogólne/srp-polska/zgody/`). | Księga znaku buduje na tożsamości SRP; mail do producenta o pisemne potwierdzenie, pliki i terytoria — gotowy do wysyłki. |
| Decyzje | Zatwierdza wyłącznie Radek; blok **poniedziałek 14:00–14:45** (w kalendarzu 21.09–26.10). Poza blokiem tylko blokery, jedno zdanie na Telegram. | Materiały do decyzji „jednym spojrzeniem" (artefakt/podgląd). |
| AI na stronie | (a) czat doradczy z katalogu, anonimowy, dane dopiero przy ofercie/rozmowie; (c) generator opisu przedmiotu zamówienia (podgląd darmowy, DOCX po e-mailu, klauzula „lub równoważny"); (d) szybka odpowiedź AI na zapytanie w minutach. Konfigurator pakietów po ustaleniu cen pakietów. Rekomendacje „podobne jednostki" dopiero z prawdziwych danych. | AI odpowiada z faktów i umawia rozmowę; cena/oferta — człowiek. Podpis „Asystent SRP Polska". |
| Ceny | **Pełny cennik sprzętu publiczny**, źródło: sklep Turbomedic (14 pozycji, `data/cennik.json`). Pozycje spoza sklepu „na zapytanie" do potwierdzenia Karoliny. Sprzęt < 10 tys. zł netto — przycisk „Zamów w sklepie"; droższy — „Zapytaj o ofertę". | Wdrożone 17.09: bloki cen na kartach, strona `cennik.html`, JSON-LD offers. |
| Główne CTA | „Umów **rozmowę o produkcie**" (30 min, Google Meet/telefon) zamiast pokazu; pokaz na żywo na zapytanie. Okna: **wtorek i czwartek 10:00–12:00** (w kalendarzu). Filmy instruktażowe producenta + własne mają zastąpić fizyczny pokaz. | Wdrożone 17.09 (teksty, formularz, krok 02). Rezerwacja online — do zbudowania. |
| CRM | Dziś pomost **Google Sheets** (poświadczenie w n8n istnieje), docelowo **HubSpot** po dodaniu poświadczenia przez Radka. | Mapowanie pól gotowe (RAPORT §4). |
| Budżet narzędzi | **300 zł/mies.** do 27.10, potem weryfikacja wobec marży. Rejestr: `ogólne/srp-polska/finanse/koszty-narzedzi.md`. | Model czatu Haiku 4.5, OPZ Sonnet 5; limit wydatków w konsoli API ustawia Radek. |
| Finanse | Marże i ceny zakupu **wyłącznie prywatnie**: `ogólne/srp-polska/finanse/` (poza gitem) + arkusz „SRP — rejestr marży" (Tor B). Stan 17.09: 25–46 % na sprzęcie średnim; PRO ELITE bez ceny zakupu (~8 % wg handoffu) — do potwierdzenia. | Repozytorium jest publiczne — nic poufnego w repo. |
| Języki | **PL + EN + DE** jako katalogi `/en`, `/de` pod srp-polska.pl; osobna domena po potwierdzeniu terytoriów przez producenta. Rynki bez dystrybutora (Europa, USA) — do zbadania. Tłumaczenie AI + kontrola krzyżowa Codex; korekta natywna przed kampanią. | Pytanie o terytoria w mailu do producenta. |
| Codex ↔ Claude | Codex: research, UX, design, grafiki, wizualna księga znaku, weryfikacja ustaleń; pliki tylko do `brand/` i `docs/`, bez commitów. Claude: kod, n8n, integracje, treści, plan, publikacja. Zlecenia jako pliki `zlecenia/*.md` (lokalne), Radek wkleja jedno zdanie w Codex. | Zlecenie nr 1: `zlecenia/CODEX-2026-09-17-research-ux-brand.md`. |
| Social | Nowe strony firmowe **SRP Polska: LinkedIn, Facebook, YouTube**; profil Radka wzmacnia. Ten sam potok redakcyjny co dział PR Ogrodowiak. Konta zakłada Radek po księdze znaku. | Etap po księdze znaku. |
| Materiały | Zdjęcia 05 usunięte z galerii wodnej (bez kasowania pliku, `site.json → galeria.wyklucz`). SEO 8711041 zostaje. Własne karty produktów PDF generowane z danych strony (dokument dystrybutora). Surowy materiał wideo od Radka do obróbki (lokalizacja do wskazania); klipy 20–60 s, napisy PL, bez muzyki i lektora AI; hosting własny + kanał YouTube. | ffmpeg do instalacji (Homebrew). |
| Miara sukcesu | Robocza, do zastąpienia OKR Radka: **8 kwalifikowanych zapytań i 3 rozmowy o produkcie do 27.10**. Pomiar: Cloudflare Web Analytics (bez ciasteczek) + Search Console (TXT po stronie Radka). | |

### Stan wykonania 17.09 (dowody)
- Strona: cennik (14 pozycji), bloki cen, `cennik.html` w sitemap i stopce, CTA „rozmowa o produkcie" w 10 miejscach, krok 02 procesu, formularz z dwoma polami (rozmowa / pokaz na żywo), pole-pułapka antyspamowa w 4 formularzach, galeria wodna bez zdjęcia 05, polityka prywatności bez tekstów roboczych (wymienieni realni odbiorcy danych). Kontrola jakości: 33 strony, 0 uwag. Publikacja: commit po tej sekcji.
- Spam: jedno wykonanie webhooka po 8.09 (#37785, 15.09) to bot; pułapka po stronie strony, filtr po stronie n8n — do dodania.
- Kalendarz Radka: blok poniedziałkowy 14:00 i okna wt/czw 10–12 wpisane.
- ClickUp (odczyt 17.09): 32 pozycje „to do", 4 po terminie (OKR, katalog/ceny, rynek/segmenty, blitz). Publikacja cennika realizuje część zadania „Katalog produktów, SKU i ceny" — Karolina weryfikuje ceny zakupu; zamknięcie zadania po jej potwierdzeniu, bez zmian dat.

### Droga do 27.10 — kolejność realizacji (właściciel: Claude, o ile nie zaznaczono)
| Tydzień | Wynik | Zależność / decyzja Radka |
|---|---|---|
| 17–21.09 | Cennik i CTA na produkcji ✔; rejestr kontaktów w Google Sheets + filtr antyspamu w n8n; mail do producenta wysłany (Radek); zlecenie do Codexa przekazane (Radek: jedno zdanie). | Radek: wysyłka maila, uruchomienie Codexa, HubSpot — poświadczenie w n8n. |
| 22–28.09 | Rezerwacja rozmowy o produkcie (Google Calendar + Meet przez n8n, potwierdzenie mailem); szybka odpowiedź AI na zapytania (SMTP kontakt@); karty produktów PDF (13) w „Do pobrania"; obróbka surowego wideo (po wskazaniu lokalizacji). Codex: research + audyt UX + księga znaku A/B. | Poniedziałek 22.09: wybór kierunku A/B księgi znaku. |
| 29.09–5.10 | Czat doradczy AI (n8n webhook + Haiku 4.5, wiedza z katalogu/FAQ/artykułów, eskalacja do rozmowy); wdrożenie księgi znaku na stronie; Cloudflare Web Analytics; aktualizacja polityki prywatności o AI i analitykę. | Poniedziałek 29.09: akceptacja treści odpowiedzi czatu; limit API w konsoli. |
| 6–12.10 | Generator OPZ (Sonnet 5, DOCX); wersje EN i DE (tłumaczenie + kontrola krzyżowa); pozycje „na zapytanie" uzupełnione po weryfikacji Karoliny. | Odpowiedź producenta o terytoriach. |
| 13–19.10 | Strony firmowe social (LinkedIn/FB/YouTube) z szablonami z księgi; pierwsze 3 materiały przez potok redakcyjny; filmy na YouTube. | Radek zakłada konta; akceptuje materiały. |
| 20–27.10 | Raport bazowy: ruch, zapytania, rozmowy, koszty vs limit; ocena vs miara robocza; propozycja zakresu na listopad (konfigurator pakietów, HubSpot pełny, Search Console). | Poniedziałek 26.10: decyzja kontynuuj / zmień zakres. |

### Nowy wątek do rozpisania (Radek, 17.09): „networki i biznes po coś"
Sieci networkingowe jako kanał i źródło treści (leady, samotność lidera, edukacja/po exicie, technikalia) oraz cel dawania (rodziny poległych żołnierzy, fundacja onkologiczna dla kobiet — gala wkrótce, „Las na zawsze"). Pytania rozpisane w sesji, odpowiedzi po jednym; wyniki wracają do tej sekcji i do księgi znaku (sekcja „Po co to robimy").
