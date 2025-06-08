# AC-Point-Matija 🏎️

Ein Punkte- und Rangsystem für deinen Assetto Corsa Server mit Discord-Bot Integration.

## 🔧 Features
- Zählt Überholungen live im Rennen
- Speichert Punkte in einer SQLite-Datenbank
- Discord-Bot sendet das aktuelle Ranking in deinen Server

## 🖥️ Setup

### 1. Server-Plugin
1. Kopiere `ScoreTrackerPlugin.dll` in dein Assetto Corsa Server Plugin-Verzeichnis.
2. Aktiviere es in der `extra_cfg.yml`.

### 2. Datenbank
Die SQLite-Datenbank wird automatisch erstellt unter `database/ac_points.db`.

### 3. Discord-Bot starten
1. Erstelle einen Bot auf [discord.com/developers](https://discord.com/developers)
2. Trage deinen Bot-Token und Channel-ID in `config.json` ein.
3. Installiere Abhängigkeiten:
   ```bash
   pip install -r requirements.txt
