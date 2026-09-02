# Product Backlog – Boghandel

Userstories fra opgavebeskrivelsen (afsnittet "Brugerhistorier", side 4–6).

| # | Userstory | Status |
|---|-----------|--------|
| 1 | Større vindue, så alle søjler kan ses | Todo |
| 2 | Ekstra kolonne "id" i bog-tabellen | Todo |
| 3 | Vis alle oplysninger om den valgte bog | Todo |
| 4 | Årstal vises som helt tal | Todo |
| 5 | Vis bogens forside ved valg | Todo |
| 6 | Vis lagerbeholdning | Todo |
| 7 | Bekræftelsesdialog ved "Slet bog" | Todo |
| 8 | "Søg"-knap til søgning på forfatter | Todo |
| 9 | "Tilføj til kurv" og bon-område | Todo |
| 10 | Gem køb til regnskab | Todo |

---

## 1. Større vindue, så alle søjler kan ses

Når brugeren ser på skærmen, vil brugeren gerne kunne se alle søjlerne i bog-tabellen fra start (`Book_gui.py`). Dvs. gør vinduet større, f.eks. 1200x600.

## 2. Ekstra kolonne "id" i bog-tabellen

Brugeren vil gerne have en søjle mere i bog-tabellen, dvs. en kolonne 5 med "id", til højre for de fire andre kolonner.

## 3. Vis alle oplysninger om den valgte bog

Når man markerer en bog, er det kun Titel og Forfatter, der skrives ovenover listen. Brugeren ønsker alle oplysningerne fra bog-tabellen vist.

**Fra:**

- Titel: The Hobbit
- Forfatter: J.R.R. Tolkien

**Til:**

- Titel: The Hobbit
- Forfatter: J.R.R. Tolkien
- Årstal: 1937.0
- Rating: 4.245552526414449
- Id: 7

## 4. Årstal vises som helt tal

Brugeren vil gerne have årstallet ændret, så man kun ser et helt årstal og ikke et decimaltal. Dvs. ikke `1937.0`, men blot `1937`.

Gælder både i tabellen (kolonnen Årstal) og i teksten over tabellen, når en bog er valgt.

## 5. Vis bogens forside ved valg

Brugeren ønsker at kunne se forsiden af bogen, når en bog på listen er markeret. Dvs. når der vælges en bog på listen, vises et billede af forsiden af bogen til højre for teksten.

Tip: Brug `image_url` (kolonne i `data/books.csv`).

## 6. Vis lagerbeholdning

Når brugeren skal sælge en bog, ønskes det at kunne se, hvor mange eksemplarer af bogen der er på lageret. Det kan enten være som en ekstra søjle i bog-tabellen eller i teksten over, når en bog er valgt.

## 7. Bekræftelsesdialog ved "Slet bog"

Når man trykker på "Slet bog", skal man få en dialogboks op med beskeden:

> "Vil du slette bogen?"

Samt to knapper: "Fortryd" og "Bekræft".

## 8. "Søg"-knap til søgning på forfatter

Lav en "Søg"-knap, så man kan lede efter bøger af en bestemt forfatter.

## 9. "Tilføj til kurv" og bon-område

Lav en knap "Tilføj til kurv", som simulerer at en kunde vil købe et eksemplar af den valgte bog.

- a. I et nyt bon-område vises en tabel med bogens titel og pris (som pris kan bruges Rating · 50 kr.)
- b. Det skal være muligt at tilføje flere bøger til listen
- c. Samt en samlet pris
- d. Tilføj en "Køb"-knap, som opdaterer lagerets status og bon-området tømmes

## 10. Gem køb til regnskab

Gem et køb, så man kan lave et regnskab for salget i boghandlen. Skal som minimum indeholde dato og tid for hvert køb, samt beløbet.

---

## Noter fra opgaven

- For at udnytte tiden kan det være nødvendigt at lave egne userstories eller opdele disse userstories i flere userstories i Sprint Backlog, for at få tiden til at passe med afslutning indenfor et Sprint.
- Man kan også tænke i helt nye udvidelser som medarbejdere, der skal have udbetalt løn. Det vil kræve registrering af medarbejdere og deres lønniveau. Måske login af medarbejdere så deres salg kan gemmes.
