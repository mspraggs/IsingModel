import lattice
import fileio
import os

Temps = [0.5*x for x in range(10)]

for T in Temps:
    L = lattice.Lattice(n = 100,T=T)
    averages = []
    for i in xrange(1000):
        L.step()
        averages.append(L.spinaverage())

    fileio.writedata("results/Temperature="+str(T)+".txt",averages)
    os.system("git add *.txt")
    os.system("git commit -am 'Added results for T="+T+"'")
    os.system("git push origin master")
