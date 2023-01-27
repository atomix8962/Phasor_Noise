from matplotlib import pyplot as plt
import numpy as np
import phasor.phasor_py as generator
from rsc.const import *


#Interactive noise but with the vecor, freq and bandwidth fixed (+ of kernels adds + time to refresh and recalculate)

size = 100
kernels = []
def onclick(event):
    kernels.append([[event.xdata, event.ydata], [1,-1], 1, 0.1])
    img = plt.contourf(X, Y, np.array(apply_function(X, Y)), cmap="Greys")
    fig.canvas.draw_idle()

X = np.arange(0, size, 1)
Y = np.arange(0, size, 1)
X, Y = np.meshgrid(X, Y)

def apply_function(X, Y):
    Z = []
    for i in range(len(X)):
        Z.insert(i, [])
        for j in range(len(Y)):
            vector = X[i][j], Y[i][j]
            Z[i].insert(j, generator.phasor_noise(vector, kernels))
    return Z

fig = plt.figure("Interactive Phasor Noise Generator")   
img = plt.contourf(X, Y, np.array(apply_function(X, Y)), cmap="Greys")
    
plt.colorbar(img)
cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()

