import lattice
import fileio
import os
import pylab as pl

Ts = [0.01*(x+1) for x in xrange(0,500)]
ns = [20]
states = [1]
Js = [1.]
params = [(n,state,J,T) for n in ns for state in states for J in Js for T in Ts ]

Saverage = []

for param in params:
    L = lattice.Lattice(n = param[0],T=param[3],state=param[1],J=param[2])
    Saverage.append(L.spinaverage())
    for i in xrange(500000):
        print("Run:%s Equilibrating: %d" % (L.config(),i))

    Etotals = []
    Stotals = []
    Etotal = L.H()
    Stotal = L.spintotal()
    Etotals.append(Etotal)
    Stotals.append(Stotal)
    
    for i in xrange(250000):
        print("Run:%s Calculating: %d" % (L.config(),i))
        Ediff,Sdiff = L.step()
        Etotal += Ediff
        Stotal += Sdiff
        Etotals.append(Etotal)
        Stotals.append(Stotal)

    fileio.writedata("results/%s.txt" % L.config(),[Etotals,Stotals])
