from matplotlib import pyplot as plt
from matplotlib.widgets import Slider
import numpy as np
import generator_phasor_noise_vPy as generator

global line

X = np.arange(-10, 10, 0.1)
Y = np.arange(-10, 10, 0.1)
X, Y = np.meshgrid(X, Y)


def apply_function(X, Y, bandwidth):
    Z = []
    for i in range(len(X)):
        Z.insert(i, [])
        for j in range(len(Y)):
            vector = X[i][j], Y[i][j]
            Z[i].insert(j, generator.gaussian(vector, bandwidth))
    return Z

fig, ax = plt.subplots(subplot_kw=dict(projection="3d"))
fig.subplots_adjust(bottom=0.25)
line = ax.plot_surface(X, Y, np.array(apply_function(X, Y, 0)))
sliderAxes = fig.add_axes([0.25, 0.1, 0.65, 0.03])
slider = Slider(ax=sliderAxes, label='BandWidth', valmin=0, valmax=3, valinit=0)


def update(val):
    global line
    line.remove()
    line = ax.plot_surface(X, Y, np.array(apply_function(X, Y, val)), color="blue")


slider.on_changed(update)
plt.show()



