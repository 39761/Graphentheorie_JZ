# Graphentheorie in der Informatik

**1. Definition:**

- Ein **Graph** G=(V,E)
- G=(V,E) besteht aus:
    - V: Menge der **Knoten** (Vertices)
    - E: Menge der **Kanten** (Edges), die Knoten verbinden
- **Gerichteter Graph**: Kanten haben Richtung (z.B. nur u→v nicht gleichtzeitig v→u)
- **Ungerichteter Graph**: Kanten ohne Richtung

--> Gerichtete Graphen haben mehr Besonderheiten, z.B. Einbahnstraßen, als ungerichtete.

**2. Arten von Graphen:**

- **Gewichtet**: Kanten haben Werte (z. B. Kosten, Distanzen)
- **Ungewichtet**: Alle Kanten gleichwertig
- **zyklisch/azyklisch**: Enthält oder enthält keine Kreise
- **Bäume**: Zusammenhängende, azyklische Graphen

**3. Darstellung in der Informatik:**

- **Adjazenzmatrix** n×nn \times nn×n, 1 wenn Kante existiert, 0 sonst
- **Adjazenzliste**, pro Knoten Liste der Nachbarn (platzsparender bei dünnen Graphen)

**4. Wichtige Begriffe:**

- **Grad** eines Knotens: Anzahl der Kanten, die ihn verbinden
- **Pfad**: Sequenz von Knoten entlang der Kanten
- **Konnektivität**: Zusammenhang zwischen Knoten

**5. Wichtige Algorithmen:**

- **Durchsuchung**:
    - BFS (Breitensuche) → kürzester Weg in ungewichteten Graphen
    - DFS (Tiefensuche) → Zyklen, Topologische Sortierung
- **Kürzeste Wege**:
    - Dijkstra (nicht-negative Gewichte)
    - Bellman-Ford (auch negative Gewichte)
    - Floyd-Warshall (alle Paar kürzesten Wege)
- **Minimaler Spannbaum**:
    - Prim, Kruskal
- **Flussalgorithmen**: Maximaler Fluss (Ford-Fulkerson)

**6. Anwendungen:**
- Netzwerke (Internet, Strom, Straßen)
- Routenplanung / GPS
- Soziale Netzwerke / Empfehlungen
- Compiler (Abhängigkeitsgraphen)