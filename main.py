import numpy as np
import matplotlib.pyplot as plt
from periodic_lattice import Periodic_Lattice
from scipy import signal
import matplotlib.animation as animation
from scipy import ndimage
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
p=0.1

class gameoflife():
    def __init__(self,size,starter,pos=[0,0]):
        self.N = size
        initialArray = np.zeros((self.N,self.N),dtype=int)
        initialArray[pos[0]:pos[0]+starter.shape[0],pos[1]:pos[1]+starter.shape[1]] = starter
        self.lattice = Periodic_Lattice(initialArray)
        self.kernel = np.ones((3,3),dtype=int)
        self.kernel[1,1]=0
        self.CoMs = []

    def simulate(self,steps):
        for i in range(0,steps):
            self.lattice = self.update()
            self.CoMs.append(ndimage.measurements.center_of_mass(np.array(self.lattice)[3:self.N-4,3:self.N-4]))

    def update(self):
        counts = signal.convolve2d(self.lattice, self.kernel, mode="same",boundary = "wrap")
        updated = ((counts==3)*(self.lattice==0) + (((counts == 2) + (counts ==3))* self.lattice==1)).astype(int)
        self.lattice=updated
        return updated

    def animate(self,i):
        data = self.update()
        ax1.clear()
        ax1.imshow(data)

def main():
    #R= gameoflife(100,np.random.choice(a=[0,1], size=(100, 100), p=[p, 1-p]))
    bee_hive = np.array([[0,1,0],[1,0,1],[1,0,1],[0,1,0]])
    oscillator = np.array([[1],[1],[1]])
    glider = np.array([[0,1,0],[0,0,1],[1,1,1]]).T
    G = gameoflife(50,glider,[10,10])
    G.simulate(1000)
    #ani = animation.FuncAnimation(fig, G.animate)
    CoMs = np.array(G.CoMs)
    CoMs = np.sqrt(np.power(CoMs[:,0],2)+np.power(CoMs[:,1],2))
    print(np.nanmean(np.gradient(CoMs)))
    plt.plot(CoMs)


    #plt.plot(G.CoMs)
    #plt.plot(G.CoMs)
    plt.show()
main()
