import lattice

Temps = [0.5*x for x in range(10)]

for T in Temps:
    L = lattice.Lattice(n = 100,T=T)
