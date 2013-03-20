
def writedata(filename,Ediffs,Sdiffs):
    """Writes list of results to a file"""
    f = open(filename,'w')

    for i in xrange(len(Ediffs)):
        f.write("%f,%f\n" % (Ediffs[i],Sdiffs[i]))

    f.close()

def readdata(filename):
    """Reads contents of file into list"""
    f = open(filename)

    lines = f.readlines()

    f.close()

    Ediffs = [eval(line.split(",")[0]) for line in lines]
    Sdiffs = [eval(line.split(",")[1][:-1]) for line in lines]
    return (Ediffs,Sdiffs

def parsefilename(filename):
    """Parses file names to extract variables"""
    parameters = filename[:-4].split(",")
    filterchars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_="
    return [eval(parameter.strip(filterchars)) for parameter in parameters]

def checkparameters(prange,parameters):
    """Checks to see if parameters are in range, and returns True if so."""
    result = True
    for i in xrange(len(parameters)):
        if parameters[i] not in prange[i]:
            result = False

    return result
