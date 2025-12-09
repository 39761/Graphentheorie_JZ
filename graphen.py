graph_minimal = {"A":"B",
                 "B":["C", "Z"],
                 "C":"D",
                 "D":""
                 }



# komplexer Pfad (ungerichtet)
graph_komplex_kompakt = {
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