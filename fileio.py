import numpy as np

def writedata(filename,dataset):
    """Writes list of results to a file"""
    f = open(filename,'w')

    for i in xrange(len(dataset[0])):
        row = [dataset[j][i] for j in xrange(len(dataset))]
        for i in xrange(len(row)):
            f.write("%f" % row[i])
            if i < len(row) - 1: f.write(",")

        f.write("\n")
        
    f.close()

def readdata(filename):
    """Reads contents of file into list"""
    f = open(filename)

    lines = [line.strip("\n") for line in f.readlines()]

    f.close()

    dataset = [[] for item in lines[0].split(",")]

    for line in lines:
        items = line.split(",")
        for j in xrange(len(items)):
            dataset[j].append(eval(items[j]))
            
    return dataset

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
