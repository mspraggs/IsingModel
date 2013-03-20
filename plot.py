import pylab as pl
import fileio
from os import listdir
from os.path import isfile, join

files = [f for f in listdir("results") if isfile(join("results",f)) and f[-4:] == ".txt"]

files.sort()

pl.ion()

for f in files:
    parameters = fileio.parsefilename(f)
    Ts = [0.25]#[0,0.25,0.5,0.75]
    ns = [100,200,300]
    Js = [1]
    inits = [0]
    #This is where results could be filtered according to parameters if necessary
    if fileio.checkparameters([ns,inits,Js,Ts],parameters):
        averages = fileio.readdata(join("results",f))
        iterations = range(len(averages))
        label = "n=%f" % parameters[0]
        pl.plot(iterations,averages,label=label)
        
pl.legend()
pl.show()
