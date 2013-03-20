import numpy as np

def writedata(filename,Es,Ss):
    """Writes list of results to a file"""
    f = open(filename,'w')

    for i in xrange(len(Es)):
        f.write("%f,%f\n" % (Es[i],Ss[i]))

    f.close()

def readdata(filename):
    """Reads contents of file into list"""
    f = open(filename)

    lines = f.readlines()

    f.close()

    Es = [eval(line.split(",")[0]) for line in lines]
    Ss = [eval(line.split(",")[1][:-1]) for line in lines]
    return (Es,Ss)

def parsefilename(filename):
    """Parses file names to extract variables"""
    parameters = filename[:-4].split(",")
    filterchars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_="
    return [eval(parameter.strip(filterchars)) for parameter in parameters]

def checkparameters(prange,parameters):
    """Checks to see if parameters are in range, and returns True if so."""
    result = True
    for i in xrange(len(parameters)):
        if np.round(parameters[i],3) not in prange[i]:
            result = False

    return result
