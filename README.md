# To-Do Lijst CLI-applicatie

## Algemene Beschrijving
Deze command-line applicatie is een eenvoudige to-do lijst waarmee gebruikers taken kunnen beheren, voltooide taken kunnen bekijken, en rapporten kunnen genereren. De applicatie gebruikt een SQLite-database voor gegevensopslag en biedt verschillende interacties via een menu in de terminal.

## Functionaliteiten
- **Taken toevoegen**: Voeg een nieuwe taak toe met een titel, beschrijving en vervaldatum.
- **Taken bekijken**: Bekijk een lijst van actieve of voltooide taken.
- **Taken voltooien**: Markeer een taak als voltooid of maak deze weer actief.
- **Exporteren**: Genereer een rapport in CSV- of Excel-formaat.
- **Grafieken**: Bekijk statistieken over actieve en voltooide taken in een grafiek.
- **Databasebeheer**: Gegevens worden opgeslagen in een SQLite-database, zodat taken behouden blijven na het afsluiten van de applicatie.

## Vereisten
- Python 3.9 of hoger
- Virtuele omgeving (`venv`) geactiveerd
- De pakketten in `requirements.txt` geïnstalleerd

## Installatie en Gebruik

### Stap 1: Clone de Repository
Clone de GitHub-repository naar je lokale machine:
```bash
git clone https://github.com/ZoeTermont/todo_list_app.git
cd todo_list_app
```

### Stap 2: Maak een Virtuele Omgeving
Maak en activeer een virtuele omgeving:

**Windows**:
```bash
python -m venv .venv
.venv\Scripts\activate
```

**Unix (Linux/MacOS)**:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Stap 3: Installeer Vereiste Pakketten
Installeer de pakketten die in `requirements.txt` staan:
```bash
pip install -r requirements.txt
```

### Stap 4: Start de Applicatie
Navigeer naar de `src`-map en start de applicatie:
```bash
cd src
python main.py
```

## Databaseconfiguratie
- De applicatie gebruikt een SQLite-database die automatisch wordt aangemaakt in de projectmap.
- Het pad naar de database wordt ingesteld in een `.env`-bestand in de map `Config/`. Zorg ervoor dat het `.env`-bestand er als volgt uitziet:
  ```plaintext
  DB_PATH="todo_list_app.db"
  ```

## Exportfunctionaliteiten
- **CSV**: Taken kunnen worden geëxporteerd naar een CSV-bestand via het exportmenu.
- **Excel**: Taken kunnen worden geëxporteerd naar een Excel-bestand via het exportmenu.

## Projectstructuur
De mappen en bestanden zijn georganiseerd als volgt:
```
todo_list_app/
├── Config/
│   ├── __init__.py
│   ├── config.py
│   ├── .env
├── database/
│   ├── __init__.py
│   ├── db_handler.py
├── src/
│   ├── __init__.py
│   ├── main.py
├── README.md
├── requirements.txt
├── .gitignore
```

## Menu-opties
### Hoofdmenu:
1. **Add Task**: Voeg een nieuwe taak toe.
2. **Show Tasks**: Bekijk alle actieve taken.
3. **Mark Task as Complete**: Markeer een taak als voltooid.
4. **Completed Tasks Menu**: Bekijk voltooide taken, herstel taken, of bekijk statistieken.
5. **Export Menu**: Genereer een CSV- of Excel-rapport.
6. **Exit**: Sluit de applicatie.

### Completed Tasks Menu:
1. **View Completed Tasks**: Bekijk alle voltooide taken.
2. **Return Completed Task to Active Tasks**: Verplaats een voltooide taak terug naar de actieve takenlijst.
3. **Graph Active vs. Completed Tasks**: Toon een grafiek met statistieken.
4. **Exit to Main Menu**: Keer terug naar het hoofdmenu.

### Export Menu:
1. **Export to CSV**: Exporteer alle taken naar een CSV-bestand.
2. **Export to Excel**: Exporteer alle taken naar een Excel-bestand.
3. **Exit Export Menu**: Keer terug naar het hoofdmenu.

## GitHub Repository
Bekijk de volledige repository hier: [todo_list_app](https://github.com/ZoeTermont/todo_list_app.git)

## Voorbeeldgebruik
1. Start de applicatie en selecteer een menu-optie.
2. Voeg taken toe via optie "1".
3. Bekijk taken via optie "2".
4. Markeer taken als voltooid via optie "3".
5. Genereer een CSV- of Excel-rapport via het exportmenu.

## Licentie
Dit project is eigendom van [ZoeTermont](https://github.com/ZoeTermont).
```