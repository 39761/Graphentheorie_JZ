# Grundlegendes rekursives Fortbewegen in einem Graph

# importiere graph_minimal
from graphen import graph_minimal

print(f"So sieht der Graph aus: {graph_minimal}")
STATIONEN_getestet = []

def tiefensuche(start, end, STATIONEN_getestet):
    print("▶ Aufruf:", start, "→", end, "| bisher:", STATIONEN_getestet)

    if start == end:
        print("✓ Ziel erreicht:", start)
        return STATIONEN_getestet

    else:
        NACHBARN = graph_minimal[start]
        print("  Nachbarn von", start, ":", NACHBARN)

        start = NACHBARN[0]
        print("  Nächster Schritt →", start)

        STATIONEN_getestet.append(start)
        print(f"  Nachbarn {start} zu der Liste {STATIONEN_getestet} hinzugefügt")

        print("  Rückkehr aus rekursivem Aufruf")
        return tiefensuche(start, end, STATIONEN_getestet)

# Rufe die Funktion auf und teste sie auf dem eifnachen Graphen

tiefensuche()