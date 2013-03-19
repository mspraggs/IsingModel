"""Class for lattice object. Contains spin states etc."""

import pylab as pl

class Lattice:

    def __init__(self,n=10,state=0.5,J=1):
        """Constructor..."""
        self.n = n
        self.spins = -1 * pl.ones((n,n))
        self.J = J

        for i in xrange(n):
            for j in xrange(n):
                if pl.random() > (1 + state) / 2:
                    self.spins[i,j] = 1

    def Hij(self,i,j):
        """Calculates the energy of a given lattice site"""
        neighbour_sum = self.spins[i,j-1] + self.spins[i,j+1] + self.spins[i-1,j] + self.spins[i+1,j]
        return - self.J * self.spins[i,j] * neighbour_sum

    def H(self):
        """Calculates the total energy of the lattice"""

        E = 0

        for i in xrange(0,self.n,2):
            for j in xrange(0,self.n,2):
                E += self.Hij(i,j)

        return E
