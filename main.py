import numpy as np
import matplotlib.pyplot as plt
from periodic_lattice import Periodic_Lattice
from scipy import signal
import matplotlib.animation as animation
from matplotlib import style

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

class gameoflife():
    def __init__(self,size,starter,pos=[0,0]):
        self.N = size
        initialArray = np.zeros((self.N,self.N),dtype=int)
        initialArray[pos[0]:pos[0]+starter.shape[0],pos[1]:pos[1]+starter.shape[1]] = starter
        self.lattice = Periodic_Lattice(initialArray)
        self.kernel = np.ones((3,3),dtype=int)
        self.kernel[1,1]=0
        #style.use('fivethirtyeight')



    def simulate(self,steps):
        for i in range(0,steps):
            plt.imshow(self.lattice)
            self.lattice = self.update(self.lattice)
            plt.pause(0.01)
        plt.show()

    def update(self):
        counts = self.NebCounts(self.lattice)
        updated = ((counts==3)*(self.lattice==0) + (((counts == 2)+ (counts ==3))* self.lattice==1)).astype(int)
        self.lattice=updated
        return updated

    def NebCounts(self,lattice):
        return signal.convolve2d(lattice, self.kernel, mode="same",boundary = "wrap")

    @classmethod
    def startRandom(cls,size, p=0.5):
        print(p)
        initialArray = np.random.choice(a=[0,1], size=(size, size), p=[p, 1-p])
        I = cls(size,initialArray)
        return I

    def animate(self,i):
        data = self.update()
        print(data)
        ax1.clear()
        ax1.imshow(data)

def main():
    # G = gameoflife(100)
    # G.simulate(100)
    # R = gameoflife.startRandom(100)
    #R.simulate(100)
    Garray = np.zeros((3,3),dtype=int)
    Garray[2,:] = 1
    Garray[1,2] = 1
    Garray[0,1] = 1

    G = gameoflife(20,Garray,[10,10])

    ani = animation.FuncAnimation(fig, G.animate)
    plt.show()
main()
