import pylab as pl

import fileio
from os import listdir
from os.path import isfile, join

files = [f for f in listdir("results") if isfile(join("results",f)) and f[-4:] == ".txt"]

files.sort()

pl.ion()

chi = []
Cv = []
Smean = []
Emean = []
Ts = []

for f in files:
    n,state,J,T = fileio.parsefilename(f)
    Ts = [pl.around(0.01*(x+1),3) for x in xrange(0,500)]
    ns = [20]
    Js = [1]
    states = [1]
    #This is where results could be filtered according to parameters if necessary
    if fileio.checkparameters([ns,states,Js,Ts],[n,state,J,T]):
        Etotals,Stotals = fileio.readdata(join("results",f))
        Eaverages = pl.array(Etotals) / n**2
        Saverages = pl.array(Stotals) / n**2

        chi.append(1/T*pl.var(Saverages))
        Cv.append(1/T**2*pl.var(Eaverages))
        Smean.append(pl.absolute(pl.mean(Saverages)))

pl.plot(Ts,Smean,'x')
pl.show()
