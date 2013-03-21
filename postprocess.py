import pylab as pl
import IPython
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
J1 = 0

for f in files:
    n,state,J,T = fileio.parsefilename(f)
    J1 = J
    Ts = [pl.around(0.01*(x+1),3) for x in range(0,500)]
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
        Emean.append(pl.mean(Eaverages))

Tc = 2*float(J1)/pl.log(1.+pl.sqrt(2.))

Stheory = [(1 - (pl.sinh(pl.log(1+pl.sqrt(2.))*Tc/T))**(-4))**(1./8) for T in Ts if T < Tc]
Stheory += [0 for T in Ts if T >= Tc]

fileio.writedata(join("results","results.txt"),[Ts,Emean,Smean,Stheory,Cv,chi])
