# WeightMaxKclique

Using PuLP (Python) to get a LP solution for maximizing a weighted clique with a limit k of edges, that could be added.

### ILP max clique

- Jeder Knoten v in der Clique, die ich Suche bekommt eine Variable x_v.
- x_v ist binär und bekommt den Wert 1, sollte der Knoten in der Clique sein
- Ich suche das Maximum aus der Summe über all x_v (möglichst viele Knoten)
- Ich muss berücksichtigen, das nicht jeder Knoten mit einem anderen Knoten in der Lösung
  auftauchen kann, da nicht alle Knoten mit Kanten verbunden sind. Da ich eine Lösung
  haben will, wo jedes x_v (oder x_u) mit einer Kante (v,u) verbunden ist
  (eine Clique), kann ich in der Lösung die im Graphen fehlenden Kanten
  auch für die Lösung ausschließen:

    x_u + x_v <= 1 für alle Kanten (u,v), die in G gegenüber eines vollständigen Graphen von G fehlen würde.

### ILP max weighted clique

Wie oben, allerdings werden die Gewichte w je Knoten v zu jedem x_v dazu multipliziert:

    Summe über alle Knoten v ( w_v * x_v)

### ILP max weighted k-clique

Bei einer k-(quasi) Clique, dürfen k Kanten in der Clique fehlen. Es muss also nicht
jeder jeden kennen, sondern k viele dürfen einander unbekannt sein. Um das im ILP
zu berücksichtigen, füge ich in den Ungleichungen für die fehlenden Kanten (u,v) einen
binären Modifikationsfaktor m_uv ein, der auf 1 geht, sollte die Kante (u,v)
doch erlaubt sein:

    x_u + x_v - m_uv <= 1

Eine weitere Ungleichung muss nun noch hinzugefügt werden, so dass max. k viele
Kanten hinzugefügt werden können:

    Summe über alle m_uv Variablen <= k
