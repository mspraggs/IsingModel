import pylab as pl
import fileio
from os import listdir
from os.path import isfile, join

def parsefilename(filename):
    """Parses file names to extract variables"
    parameters = filename[:-4].split(",")
    filterchars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_="
    return [eval(parameter.strip(filterchars)) for parameter in parameters]

files = [f for f in listdir("results") if isfile(join("results",f)) and f[-4:] == ".txt"]

for f in files:
    parameters = parsefilename(f)
    #This is where results could be filtered according to parameters if necessary
    if True:
        
