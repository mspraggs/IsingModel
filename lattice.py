"""Class for lattice object. Contains spin states etc."""

import pylab as pl

class Lattice:

    def __init__(self,n=10,state=0):
        """Constructor..."""
        self.n = n

        self.spins = -1 * pl.ones(1,(n,n))

        for i in xrange(n):
            for j in xrange(n):
                if pl.random() > (1 + state) / 2:
                    self.spins[i,j] = 1

        
