from pylab import *
import IPython
import fileio
from os import listdir
from os.path import isfile, join

def subplots(label):
    """Draws four subplots of each of the variables"""
    data = [M,E,chi,Cv]
    labels = ["$\overline{M}$","$\overline{E}$","$\overline{\chi}$","$\overline{C}_V$"]

    for j in xrange(len(labels)):
        subplot(2,2,j+1)
        plot(T,data[j])
        xlabel("$T$")
        ylabel(labels[j])

    fig = gcf()
    fig.suptitle(label)
    savefig("plots/%s.png" % files[i])

files = [f for f in listdir("results") if isfile(join("results",f)) and f[:7] == "results"]

files.sort()
ion()

if len(files) > 0:
    print("Available data:")
    for i in xrange(len(files)):
        print("(%d) %s" % (i,files[i]))

    file_num = input("File: ")
    filename = "results/%s" % files[file_num]

    T,E,M,Mtheory,Cv,chi = fileio.readdata(filename)
    
    IPython.embed()

else:
    print("No data available yet! Use postprocess.py to generate some.")
