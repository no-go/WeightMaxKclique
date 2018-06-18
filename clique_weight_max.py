import pulp

# Knoten
V = ['a', 'b', 'c', 'd', 'e']
# Gewichte, Dachspitze hat hohes Gewicht
w = {'a':1.0, 'b':1.1, 'c':1.3, 'd':1.0, 'e':1.8}

# Kanten (Haus vom Nicolaus)
E = [('a','b'),('b','c'),('c','d'),('a','d'),('d','e'),('c','e'),('a','c'),('d','b')]

# Kanten (Haus vom Nicolaus aber statt X ein /)
#E = [('a','b'),('b','c'),('c','d'),('a','d'),('d','e'),('c','e'),('a','c')]


def notE(V, E):
    nots = []
    for u in V:
        for v in V:
            if u ==v: continue
            if not ((u,v) in E or (v,u) in E) and not((u,v) in E or (v,u) in nots):
                nots.append((u,v))
    return nots

print("Vertices und Gewicht:", w)
print("Edges:               ", E)
print("Missing edges:       ", notE(V, E))

model = pulp.LpProblem("max weighted clique", pulp.LpMaximize)

xv = {}

for v in V:
    xv[v] = pulp.LpVariable(v, lowBound=0, cat='Binary')

model += pulp.lpSum([w[v] * xv[v] for v in V]), "max me"

nonEdges = notE(V,E)
for noe in nonEdges:
    model += xv[noe[0]] + xv[noe[1]] <= 1

model.solve()
pulp.LpStatus[model.status]

for v in V:
    if xv[v].varValue > 0:
        print(v,'ist drin mit w =', w[v])

print('Gesamt Summe dieser Clique:', pulp.value(model.objective))
