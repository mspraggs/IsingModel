import pylab as pl
import fileio
from os import listdir
from os.path import isfile, join

files = [f for f in listdir("results") if isfile(join("results",f)) and f[-4:] == ".txt"]

for f in files:
    parameters = parsefilename(f)
    #This is where results could be filtered according to parameters if necessary
    if True:
        averages = fileio.readdata(f)
        iterations = range(len(averages))
        label = "T=%f" % parameters[3]
        pl.plot(iterations,averages,label=label)
        
