import pylab as pl
import fileio
from os import listdir
from os.path import isfile, join

files = [f for f in listdir("results") if isfile(join("results",f)) and f[-4:] == ".txt"]

files.sort()

pl.ion()

chi = []
Cv = []

for f in files:
    n,state,J,T = fileio.parsefilename(f)
    Ts = [0.25*x for x in range(41)]
    ns = [100]
    Js = [1]
    states = [0]
    #This is where results could be filtered according to parameters if necessary
    if fileio.checkparameters([ns,states,Js,Ts],[n,state,J,T]):
        Etotals,Stotals = fileio.readdata(join("results",f))
        Eaverages = pl.array(Etotals) / n**2
        Saverages = pl.array(Stotals) / n**2

        chi.append(1/T*(pl.mean(Saverages**2) - pl.mean(Saverages)**2))
        Cv.append(1/T**2*(pl.mean(Eaverages**2) - pl.mean(Saverages)**2))
        
pl.legend()
pl.show()
