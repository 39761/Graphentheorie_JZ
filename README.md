# Graphentheorie

Dieses Repo dient dazu, Graphen praktisch zu erkunden!

## Lernziele
1. **Graphentheorie** verstehen (Knoten, Kanten, Pfade).  
2. **Tiefensuche implementieren** im U-Bahn-Kontext.  
3. evtl. **Breitensuche** nachschieben
4. **GitHub-Workflow**: Fork → lokal bearbeiten → Commit → Push → Pull Request.  
5. **GitHub Issues** verwenden: Probleme dokumentieren, Fragen stellen.

## Repo
```
graphentheorie/
│
├── /docs/ # Unterlagen & Skripte zu Graphentheorie und GitHub-Workflow
│ └── GitHub_cheat_sheet.md # Begriffe und Flows zu GitHub, mit herzlichen Dank an Johannes und Markus 
│ └── graph_komplex_kompakt.png # Visualisierung eines kompakten ungerichteten Testgraphen mit verschiedenen Fallstricken zum testen der DFS
│ └── graphentheorie_von_chatgpt.md # etwas Theorie zu Graphen in der Informatik
│ └── tiefensuche.md # das wichtigeste zu DFS auf einen Blick
│
├── /Werkstatt/ # Experimentierbereich & Übungsfälle
│ └── kurzesten_pfad_finden_minimal.py # hier wird versucht die kürzeste Liste aus einer Liste von Listen zu ermitteln
│ └── laufen_lernen.py # Beispiel: rekursives Durchlaufen eines Graphen
│ └── pfad_speichern_minimal.py # Vorlage mit Erklärung des Issues zum Herausarbeiten des (minimal) Problems
│
├── .gitignore # hier steht, was von git ignoriert werden soll!!!!!
├── graphen.py # Verschiedene Graphen
├── main.py # Ausgangscode für die Übung (fehlerhafte DFS)
├── README.md # Überblick & Anleitungen
```

## Wie wir arbeiten
siehe [wie GitHub funktioniert](docs/GitHub_cheat_sheet.md)

1. **Repo forken**  
2. **Projekt klonen** und lokal öffnen  
3. **Branch** erstellen und bearbeiten
4. **Pull-Request** senden