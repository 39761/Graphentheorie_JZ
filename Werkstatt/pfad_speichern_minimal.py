# Die Ausgabe gibt wider erwarten nicht den kompletten Pfad:
# beim Aufrufen der Funktion mit tiefensuche(graph_kompakt, "Start", "C", [], [])
# erhaltene Ausgabe: [['Start', 'A']]
# erwartete Ausgabe: ['Start', 'A', 'C']

# liegt das Problem hier?
# result.append(path)
# path.pop()

# These: die Listen "Pfad" und "result" sind nicht getrennt, deshalb gibt es die ungewollte Ausgabe


# Testgraph in dem der Issue entdeckt wurde
graph_kompakt = {
    "Start": ["A", "B"],          # Fork
    "A": ["Start", "C", "D", "E"], # Fork + Teil eines Zyklus
    "B": ["Start", "D"],           # MultiParent D
    "C": ["A", "E"],               # Teil-Zyklus C-E-A
    "D": ["A", "B", "F"],          # MultiParent D + Dead-End F
    "E": ["C", "A"],               # Zyklus C-E-A
    "F": ["D"],                    # Dead-End / Blatt
    "SelfLoop": ["SelfLoop"],      # Self-Loop isoliert
    "Isolated": [],                # Isolierte Node
}

# Stand der Funktion mit dem der Fehler aufgerufen wurde
def tiefensuche(graph, node, goal, path, result, tiefe=0):
    einrueckung = "   " * tiefe  # Einrückung je Rekursionstiefe
    print(f"{einrueckung}Wir sind gerade hier: {node} | Aktueller Pfad: {path + [node]}")
    path.append(node)

    if node == goal:
        print(f"{einrueckung}Ziel erreicht: {goal} | Pfad speichern: {path}")
        # vermutete Fehlerquelle
        result.append(path)
        path.pop()
        print(f"{einrueckung}Nach dem Erreichen des Ziels {node} wieder aus Pfad entfernen | Pfad jetzt: {path}")
        return result

    for child in graph[node]:
        if child not in path:
            print(f"{einrueckung}Wir fahren von {node} zu {child}")
            return tiefensuche(graph, child, goal, path, result, tiefe + 1)

    path.pop()
    print(f"{einrueckung}Pfad zu Ende: {node} aus Pfad entfernen | Pfad jetzt: {path}")

print(tiefensuche(graph_kompakt, "Start", "C", [], []))