import numpy as np
import matplotlib.pyplot as plt
from periodic_lattice import Periodic_Lattice
from scipy import signal
class gameoflife():
    def __init__(self,size,initialArray):
        self.N = size

        # initialArray = 0*np.ones((self.N,self.N),dtype=int)
        # initialArray[-1,0]=1
        # initialArray[0,0]=1
        # initialArray[1,0]=1
        self.lattice = Periodic_Lattice(initialArray)
        self.kernel = np.ones((3,3),dtype=int)
        self.kernel[1,1]=0

    def simulate(self,steps):
        for i in range(0,steps):
            plt.imshow(self.lattice)
            self.lattice = self.update(self.lattice)
            plt.pause(0.01)
        plt.show()

    def update(self,lattice):
        counts = self.NebCounts(self.lattice)
        updated = ((counts==3)*(self.lattice==0) + (((counts == 2)+ (counts ==3))* self.lattice==1)).astype(int)
        return updated

    def NebCounts(self,lattice):
        return signal.convolve2d(lattice, self.kernel, mode="same",boundary = "wrap")

    @classmethod
    def startRandom(cls,size, steps=100,p=0.5):
        print(p)
        initialArray = np.random.choice(a=[0,1], size=(size, size), p=[p, 1-p])
        I = cls(size,initialArray)
        I.simulate(steps)

def main():
    # G = gameoflife(100)
    # G.simulate(100)
    gameoflife.startRandom(100,100)
main()
