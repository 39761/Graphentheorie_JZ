# Ausgangscode: hier ist eine Tiefensuche als Funktion codiert. Sie hat jedoch noch Fehler!

# importiere graph_minimal
from graphen import graph_minimal, graph_komplex_kompakt

STATIONEN_getestet = []

# Tiefensuche-Funktion
def tiefensuche(graph, node, goal, path, result, tiefe=0):
    einrueckung = "   " * tiefe  # Einrückung je Rekursionstiefe
    print(f"{einrueckung}Wir sind gerade hier: {node} | Aktueller Pfad: {path + [node]}")
    path.append(node)

    if node == goal:
        print(f"{einrueckung}Ziel erreicht: {goal} | Pfad speichern: {path}")
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


## Kürzesten Pfad zum Ziel finden

# Wie beim Aufrufen der Funktion durch die Prints gesehen, werden Pfade zum Ziel gefunden
# Die Pfade sollen alle in einer Liste gespeichert werden
pfade = tiefensuche(graph_komplex_kompakt, "Start", "F", [], STATIONEN_getestet)

print(f"type: {type(pfade)} inhalt: {pfade}")

kuerzester_pfad = min(list(len(pfad) for pfad in pfade))

print(f"Das ist der kürszeste Weg zum Ziel: {kuerzester_pfad}")