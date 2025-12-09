# Wie bekommen wir die Liste ausgegeben, die die kurzeste Länge hat?
# 1. wie bekommen wir die kurzeste Liste ausgegebebn?
# funktioniert die Idee mit "min" überhaupt?
# --> erst "zu fuß", dann komplizierter

# 2. was machen wir bei mehreren gleich langen "strecken"?
# --> Festlegung: alle ausgeben


# Eine Liste, in der Listen gespeichert sind:
liste_liste = [[1,2,3],[2,3,4,5], [1]]

# über die Liste mit den Listen mit zugewiesenem Index iterieren
for index, liste in enumerate(liste_liste):
    print(f"index: {index}, liste: {liste}")


# Idee mit "min" schlägt (erstmal) fehl:
kuerzeste_liste = min(list(len(liste) for liste in liste_liste))

print(kuerzeste_liste)
# erwartete Ausgabe:
# kuerzeste_liste: list := [Start, Station, ..., Ziel]

# erhaltene Ausgabe:
# kuerzeste_liste: int := [1]