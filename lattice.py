"""Class for lattice object. Contains spin states etc."""

import pylab as pl
import copy

class Lattice:

    k = 1#.38e-23

    def __init__(self,n=100,state=0.5,J=1,T=2,):
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
        neighbour_sum = 0
        for site in self.getneighbours((i,j)):
            neighbour_sum += self.spins[site]
        return - self.J * self.spins[i,j] * neighbour_sum

    def getneighbours(self,(i,j)):
        """Returns sites connected to site i,j"""
        result = []
        result.append((i%self.n,(j-1)%self.n))
        result.append((i%self.n,(j+1)%self.n))
        result.append(((i-1)%self.n,j%self.n))
        result.append(((i+1)%self.n,j%self.n))
        return result

    def getneighbourhood(self,(i,j)):
        """Gets 3x3 neighbourhood around site i,j"""
        out = pl.zeros((3,3))
        r = 0
        for m in xrange(i-1,i+2):
            s = 0
            for n in xrange(j-1,j+2):
                out[r,s] = self.spins[m%(self.n-1),n%(self.n-1)]
                s+=1
            r+=1
                
        return out

    def H(self, a = False):
        """Calculates the total energy of the lattice"""
        E = 0.
        Energies = pl.zeros((self.n,self.n))

        for i in xrange(self.n):
            for j in xrange(self.n):
                E += self.Hij((i,j))
                Energies[i,j] = self.Hij((i,j))

        if a: return [E/2,Energies]
        else: return E/2

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
        if Ediff < 0: return 1
        else: return 0 if self.T == 0 else pl.exp(-self.beta()*Ediff)
        
    def step(self):
        """Run one step of the Metropolis algorithm"""
        site = self.getsite()
        #Copy the lattice and flip a particular site
        newLattice = copy.deepcopy(self)
        newLattice.spinflip(site)
        
        #Now need to work out the energy difference between the lattices.
        #This is used to determine the probability that we'll keep the
        #new configuration.
        Ediff = -2 * self.Hij(site)
        Sdiff = -2 * self.spins[site]
        AP = self.probaccept(Ediff)

        if AP > pl.random():
            self.spins = copy.copy(newLattice.spins)
        else:
            Ediff = 0.
            Sdiff = 0.
            
        return (Ediff, Sdiff)

    def spinaverage(self):
        """Calculate the average spin of the lattice"""
        return pl.mean(self.spins)

    def spintotal(self):
        """Calculate the total spin of the lattice"""
        return pl.sum(self.spins)
