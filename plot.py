import pylab
import IPython
import fileio
from os import listdir
from os.path import isfile, join

files = [f for f in listdir("results") if isfile(join("results",f)) and f[:7] == "results"]

if len(files) > 0:
    print("Available data:")
    for i in xrange(len(files)):
        print("(%d) %s" % (i,f))

    file_num = input("File: ")
    filename = "results/%s" % files[i]

    T,E,M,Mtheory,Cv,chi = fileio.readdata(filename)
    
    IPython.embed()

else:
    print("No data available yet! Use postprocess.py to generate some.")
