import math

from matplotlib import pyplot as plt
from matplotlib.widgets import Slider
import numpy as np
import phasor.phasor_py as generator

global line

X = np.arange(0, 255, 1)
Y = np.arange(0, 255, 1)
X, Y = np.meshgrid(X, Y)


def apply_function(X, Y, bandwidth):
    Z = []
    for i in range(len(X)):
        Z.insert(i, [])
        for j in range(len(Y)):
            vector = X[i][j], Y[i][j]
            Z[i].insert(j, generator.phasor_noise(vector, [0, 1], [[100, 100], [105, 105]], bandwidth, 1000))
    return Z

fig, ax = plt.subplots(subplot_kw=dict(projection="3d"))
ax2 = fig.add_subplot()
fig.subplots_adjust(bottom=0.25)
#line = ax.plot_surface(X, Y, np.array(apply_function(X, Y, 0)))
img = ax2.contourf(X, Y, np.array(apply_function(X, Y, 1/4)), cmap="Greys")
sliderAxes = fig.add_axes([0.25, 0.1, 0.65, 0.03])
slider = Slider(ax=sliderAxes, label='Bandwidth', valmin=0, valmax=3, valinit=0)
fig.colorbar(img)

def update(val):
    global line
    return


###slider.on_changed(update)
plt.show()



