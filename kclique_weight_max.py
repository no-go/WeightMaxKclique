import pulp

k=1

# Knoten
V = ['a', 'b', 'c', 'd', 'e']
# Gewichte, Dachspitze hat hohes Gewicht
w = {'a':1.0, 'b':1.1, 'c':1.3, 'd':1.0, 'e':1.8}

# Kanten (Haus vom Nicolaus)
#E = [('a','b'),('b','c'),('c','d'),('a','d'),('d','e'),('c','e'),('a','c'),('d','b')]

# Kanten (Haus vom Nicolaus aber statt X ein /)
E = [('a','b'),('b','c'),('c','d'),('a','d'),('d','e'),('c','e'),('a','c')]


def notE(V, E):
    nots = []
    for u in V:
        for v in V:
            if u ==v: continue
            if not ((u,v) in E or (v,u) in E) and not((u,v) in E or (v,u) in nots):
                nots.append((u,v))
    return nots

print("k...................:", k)
print("Vertices und Gewicht:", w)
print("Edges...............:", E)
print("Missing edges.......:", notE(V, E))

model = pulp.LpProblem("max weighted clique", pulp.LpMaximize)

xv = {}
m_uv = {}

for v in V:
    xv[v] = pulp.LpVariable(v, lowBound=0, cat='Binary')

model += pulp.lpSum([w[v] * xv[v] for v in V]), "max me"

nonEdges = notE(V,E)
for noe in nonEdges:
    m_uv[noe] = pulp.LpVariable(''.join(noe), lowBound=0, cat='Binary')
    model += xv[noe[0]] + xv[noe[1]] - m_uv[noe] <= 1

model += pulp.lpSum([m_uv[m] for m in m_uv]) <= k, "for k quasi clique"

model.solve()
pulp.LpStatus[model.status]

for v in V:
    if xv[v].varValue > 0:
        print(v,'ist drin mit w =', w[v])

for m in m_uv:
    if m_uv[m].varValue > 0:
        print('Neue Kante', m)

print('Gesamt Summe dieser Clique:', pulp.value(model.objective))
