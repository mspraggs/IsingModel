import lattice
import fileio
import os

Temps = [0.5*x for x in range(10)]

for T in Temps:
    L = lattice.Lattice(n = 100,T=T,state=0)
    averages = []
    for i in xrange(100):
        print("Temperature: %f Step: %d" % (T,i))
        L.step()
        averages.append(L.spinaverage())

    fileio.writedata("results/%s.txt" % L.config(),averages)
    os.system("git add *.txt")
    os.system("git commit -am 'Added results for %s'" % L.config())
    os.system("git push origin master")
