import numpy as np
import matplotlib.pyplot as plt
from periodic_lattice import Periodic_Lattice
from scipy import signal
import matplotlib.animation as animation
from scipy import ndimage
import sys
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
p=0.5

class gameoflife():
    def __init__(self,size,starter,pos=[0,0]):
        self.N = size
        initialArray = np.zeros((self.N,self.N),dtype=int)
        initialArray[pos[0]:pos[0]+starter.shape[0],pos[1]:pos[1]+starter.shape[1]] = starter
        self.lattice = Periodic_Lattice(initialArray)
        self.kernel = np.zeros((3,3),dtype=int)
        self.kernel[1,0]=1
        self.kernel[0,1]=1
        self.kernel[2,1]=1
        self.kernel[1,2]=1
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

def main(args):
    print(args)
    if len(args)==3:
        if int(args[1]) == 0:
            print("random")
            G= gameoflife(100,np.random.choice(a=[0,1], size=(100, 100), p=[p, 1-p]))
        elif  int(args[1]) == 1:
            bee_hive = np.array([[0,1,0],[1,0,1],[1,0,1],[0,1,0]])
            G = gameoflife(50,bee_hive,[10,10])
        elif  int(args[1]) == 2:
            oscillator = np.array([[1],[1],[1]])
            G = gameoflife(50,oscillator,[10,10])
        elif  int(args[1]) == 3:
            glider = np.array([[0,1,0],[0,0,1],[1,1,1]])
            G = gameoflife(50,glider,[25,25])
        if int(args[2]) == 0:
            print("animate")
            ani = animation.FuncAnimation(fig, G.animate)
            plt.show()
        elif int(args[2]) == 1:
            G.simulate(1000)

            CoMs = np.array(G.CoMs)
            CoMs = np.sqrt(np.power(CoMs[:,0],2)+np.power(CoMs[:,1],2))
            print(np.nanmean(np.gradient(CoMs)))
            plt.plot(CoMs)
            plt.show()
    else:
        print("[0:random,1:bee hive,2:oscillator,3:glider],[0:animate,1:calculate velocity]")


main(sys.argv)
