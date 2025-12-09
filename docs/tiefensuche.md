# Tiefensuche DFS

## Was ist Depth-First Search?

Die Tiefensuche (**Depth-first search**, DFS) ist ein Algorithmus, der verwendet wird, um eine Datenstruktur, wie z. B. einen Graphen oder einen Baum, zu durchlaufen oder zu durchsuchen. 
Die **Grundidee** des DFS ist, dass es **einen Zweig des Graphen oder Baums so weit wie möglich erkundet**, bevor es zurückgeht, um alternative Zweige zu erkunden. Dieser Ansatz steht im **Gegensatz zur Breadth-First-Suche**, bei der alle Knoten auf der aktuellen Tiefenstufe untersucht werden, bevor die nächste Stufe erreicht wird. Du kannst HIER über die Breadth-First-Suche lesen.

## Hauptmerkmale der Depth-First-Suche in Python

Bei der Depth-First-Suche werden die Knoten systematisch erkundet und nur bei Bedarf ein Backtracking durchgeführt. Werfen wir einen Blick auf einige seiner wichtigsten Eigenschaften.

### Rekursive Natur

Im Kern arbeitet die DFS rekursiv, das heißt, sie löst das Problem, indem sie sich selbst wiederholt aufruft, während sie tiefer in die Struktur vordringt. Wenn die DFS in einen Zweig eintaucht, erforscht sie ihn so tief wie möglich, bevor sie wieder hochkommt, um andere Zweige zu erforschen. 

### Backtracking

**Backtracking** ist für die DFS unerlässlich. **Wenn der Algorithmus einen Knoten erreicht, der keine unbesuchten Nachbarn hat, geht er seine Schritte zum vorherigen Knoten zurück und prüft, ob es dort weitere unbesuchte Nachbarn gibt.**
Wenn es welche gibt, werden diese erkundet; wenn nicht, wird der Weg zurückverfolgt. Dieser Zyklus von tiefer eintauchen und zurückverfolgen wird fortgesetzt, bis alle möglichen Pfade abgedeckt sind oder eine Ausstiegsbedingung erfüllt ist.

### Handhabungszyklen

Graphen können **Zyklen** enthalten, **also Pfade, die sich selbst wiederholen**. Ohne entsprechende Vorkehrungen könnte DFS die Knotenpunkte in diesen Zyklen endlos wieder besuchen. Indem jeder Knoten beim ersten Mal als besucht markiert wird, kann das DFS vermeiden, seine Schritte unnötig zurückzuverfolgen. Auf diese Weise bleibt das DFS auch in zyklischen Graphen effizient und vermeidet Endlosschleifen.

### Umfassende Erkundung

Eines der Markenzeichen der DFS ist die Fähigkeit, eine Struktur vollständig zu erkunden. Der Algorithmus wird so lange fortgesetzt, bis jeder Knotenpunkt besucht worden ist. Das ist besonders nützlich, wenn du sicherstellen musst, dass keine potenzielle Lösung übersehen wird, z. B. beim Lösen von Rätseln, beim Erkunden von Entscheidungsbäumen oder beim Navigieren durch Labyrinthe.

# Recursive DFS function in Python

```python
# Define the decision tree as a dictionary
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
    'H': [], 'I': [], 'J': [], 'K': [],
    'L': [], 'M': [], 'N': [], 'O': []
}
```
Ist das ein **gerichteter** Graph?
Ich kann von "C" nicht zu "A" oder?
```python
def dfs_recursive(tree, node, visited=None):
    if visited is None:
        visited = set()  # Initialize the visited set
    visited.add(node)    # Mark the node as visited
    print(node)          # Print the current node (for illustration)
    for child in tree[node]:  # Recursively visit children
        if child not in visited:
            dfs_recursive(tree, child, visited)
```

#  Merken

> **Immer, wenn du einen veränderlichen Container (Liste) rekursiv speicherst, speichere eine Kopie, nicht die Liste selbst.**

⭐ **"Beim Reinlaufen anhängen, beim Rauslaufen entfernen."**

⭐ **Rekursive Funktionen müssen die Rückgabe explizit weiterreichen**, sonst „verliert“ sich der Wert nach unten.