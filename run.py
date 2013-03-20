import lattice
import fileio
import os

Ts = [0.25]#[0.25*x for x in range(21)]
ns = [100]
states = [0.5*x - 1 for x in range(5)]
Js = [1.]
params = [(n,state,J,T) for n in ns for T in Ts for state in states for J in Js]

for param in params:
    L = lattice.Lattice(n = param[0],T=param[3],state=param[1],J=param[2])
    averages = []
    for i in xrange(10000):
        print("Run:%s Step: %d" % (L.config(),i))
        L.step()
        averages.append(L.spinaverage())

    fileio.writedata("results/%s.txt" % L.config(),averages)
    os.system("git add *.txt")
    os.system("git commit -am 'Added results for %s'" % L.config())
    os.system("git push origin master")
