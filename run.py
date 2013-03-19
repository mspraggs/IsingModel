import lattice
import fileio
import os

Ts = [0.25*x for x in range(100)]
ns = [100]
states = [0]
Js = [1]
params = [(n,T,state,J) for n in ns for T in Ts for state in states for J in Js]

for param in params:
    L = lattice.Lattice(n = param[0],T=param[1],state=param[2],J=param[3])
    averages = []
    for i in xrange(10000):
        print("Temperature: %f Step: %d" % (T,i))
        L.step()
        averages.append(L.spinaverage())

    fileio.writedata("results/%s.txt" % L.config(),averages)
    os.system("git add *.txt")
    os.system("git commit -am 'Added results for %s'" % L.config())
    os.system("git push origin master")
