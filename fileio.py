
def writedata(filename,data):
    """Writes list of results to a file"""
    f = open(filename,'w')

    for datum in data:
        f.write(str(datum) + '\n')

    f.close()

def readdata(filename):
    """Reads contents of file into list"""
    f = open(filename)

    lines = f.readlines()

    return [eval(line[:-1]) for line in lines]
