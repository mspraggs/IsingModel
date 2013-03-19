"""Class for lattice object. Contains spin states etc."""

import pylab as pl
import copy

class Lattice:

    k = 1#.38e-23

    def __init__(self,n=100,state=0.5,J=1,T=2):
        """Constructor..."""
        self.n = n
        self.spins = -1 * pl.ones((n,n))
        self.J = J
        self.T=T
        self.init = state

        for i in xrange(n):
            for j in xrange(n):
                if pl.random() < (1 + state) / 2.:
                    self.spins[i,j] = 1

    def config(self):
        """Outputs information about the lattice configuration"""
        return "n=%d,init=%f,J=%f,T=%f" % (self.n,self.init,self.J,self.T)

    def Hij(self,(i,j)):
        """Calculates the energy of a given lattice site"""
        neighbour_sum = self.spins[i%(self.n-1),(j-1)%(self.n-1)] + \
                        self.spins[i%(self.n-1),(j+1)%(self.n-1)] + \
                        self.spins[(i-1)%(self.n-1),j%(self.n-1)] + \
                        self.spins[(i+1)%(self.n-1),j%(self.n-1)]
        return - self.J * self.spins[i,j] * neighbour_sum

    def H(self):
        """Calculates the total energy of the lattice"""
        E = 0

        for i in xrange(self.n):
            for j in xrange(self.n):
                E += self.Hij((i,j))

        return E/2

    def beta(self):
        """Calculates the value of beta for the given lattice temperature"""
        return 1/(self.k * self.T) if self.T > 0 else float("inf")

    def getsite(self):
        """Returns tuple to random point on the lattice
        (Selection probability)"""
        return (pl.randint(0,self.n),pl.randint(0,self.n))

    def spinflip(self,(i,j)):
        """Flips the spin at site i,j"""
        self.spins[i,j] = 1 if self.spins[i,j] == -1 else -1

    def probaccept(self,Ediff):
        """Calculates the probability of acceptance of a configuration that
        has energy difference Ediff from current configuration"""
        if self.T == 0: return 0
        else: return 1 if Ediff < 0 else pl.exp(-self.beta()*Ediff)
        
    def step(self):
        """Run one step of the Metropolis algorithm"""
        site = self.getsite()
        #Copy the lattice and flip a particular site
        newLattice = copy.deepcopy(self)
        newLattice.spinflip(site)
        
        #Now need to work out the energy difference between the lattices.
        #This is used to determine the probability that we'll keep the
        #new configuration.
        Ediff = newLattice.Hij(site) - self.Hij(site)
        AP = self.probaccept(Ediff)

        if AP > pl.random():
            self.spins = copy.copy(newLattice.spins)

    def spinaverage(self):
        """Calculate the average spin of the lattice"""
        return pl.mean(self.spins)
