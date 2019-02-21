import numpy as np
import matplotlib.pyplot as plt
from periodic_lattice import Periodic_Lattice
from scipy import signal
class gameoflife():
    def __init__(self,size):
        self.N = size
        p=0.9
        initialArray = np.random.choice(a=[-1,1], size=(self.N, self.N), p=[p, 1-p])#np.array((self.N,self.N))
        initialArray = -1*np.ones((self.N,self.N))
        initialArray[1,4]=1
        initialArray[2,4]=1
        initialArray[3,4]=1
        self.lattice = Periodic_Lattice(initialArray)

        # plt.imshow(self.lattice)
        # plt.show()

    def simulate(self,steps):
        for i in range(0,steps):
            plt.imshow(self.lattice)
            updated = self.update(self.lattice)
            self.lattice = updated
            plt.pause(0.1)
        plt.show()

    def update(self,lattice):
        updated = np.zeros((self.N,self.N))
        counts = self.NebCounts(self.lattice)
        print(counts)
        for i in range(0,self.N):
            for j in range(0,self.N):
                if self.lattice[i,j]==1:
                    if (counts[i,j]>3) or (counts[i,j]<2):
                        updated[i,j] = -1
                elif self.lattice[i,j]==-1:
                    if counts[i,j]==3:
                        updated[i,j] = -1
                # neighbs = self.getNeighbs(lattice,i,j)
                # update = self.rules(i,j, neighbs)
                # updated[i,j] = update#update*lattice[i,j]



        return updated

    def getNeighbs(self,lattice, i,j):
        values = np.array(8)

        values = lattice[i-1:i+2,j-1:j+2].flatten()
        ADJACENTS = {(-1, 1), (0, 1), (1, 1), (-1, 0),
             (1, 0), (-1, -1), (0,-1), (1,-1)}
        #values = np.array(lattic
        if values.size!=8:
            print(values)
            raise ValueError("Wrong number of nebs")
        return values

    def NebCounts(self,lattice):
        kernel = np.ones((3,3), dtype=int)
        kernel[1,1]=0
        return signal.convolve2d(lattice, kernel, mode="same")
    def rules(self,i,j,neighbs):
        counts = np.where(neighbs==1)[0].size
        if counts>0:
            print(counts)
        current = self.lattice[i,j]
        newVal = current

        if current==1:
            if (counts>3) or (counts<2):
                newVal = -1
        else:
            if counts==3:
                newVal = 1
        return newVal
def main():
    G = gameoflife(100)
    G.simulate(1)
main()
