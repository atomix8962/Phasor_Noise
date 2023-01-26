"""
-Name:  kernel_isolated.py 
-Description:   Create 4 kernels isolated and display the vector and the kernel in 1 image
-Date: 26/01/23
"""
#   Import section
import numpy as np
import phasor.phasor_py as generator
from matplotlib import pyplot as plt

plt.figure('4 kernels isolated')
kernels = [[[25, 25], [1, 1], .75, 0.1], [[25, 75], [1, 0], .75, 0.1], [[75, 25], [0, 1], .75, 0.1], [[75, 75], [-1, 1], .75, 0.1]]

X, Y = np.meshgrid(np.arange(0, 100, 1), np.arange(0, 100, 1))

def apply_noise(X:int, Y:int) -> list:
    Z = []
    for i in range(len(X)):
        Z.insert(i, [])
        for j in range(len(Y)):
            vector = X[i][j], Y[i][j]
            Z[i].insert(j, generator.phasor_noise(vector, kernels))

    return Z


img = plt.contourf(X, Y, np.array(apply_noise(X, Y)), cmap="Greys")
plt.colorbar(img)

for kernel in kernels:
    plt.plot(kernel[0][0],kernel[0][1], color="green", marker="o")
    plt.arrow(kernel[0][0],kernel[0][1], kernel[1][0]*15,kernel[1][1]*15 , width= 1,head_width=4, head_length=4, color="red")

plt.show()