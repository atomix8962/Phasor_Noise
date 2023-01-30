import numpy as np
import os, math
import random as rd
from rsc.const import *
import phasor.phasor_jax as generator
from matplotlib import pyplot as plt
from alive_progress import alive_bar
        

def custom_kernel(size:int, kernels):
    plt.figure("Custom Phasor Noise")
    X = np.arange(0, size, 1)
    Y = np.arange(0, size, 1)
    X, Y = np.meshgrid(X, Y)

    def apply_function(X, Y):
        Z = []
        with alive_bar(len(X)*len(Y)) as bar: 
            for i in range(len(X)):
                Z.insert(i, [])
                for j in range(len(Y)):
                    vector = X[i][j], Y[i][j]
                    Z[i].insert(j, generator.phasor_noise(vector, kernels))
                    bar()
        return Z
    

    img = plt.contourf(X, Y, np.array(apply_function(X, Y)), cmap="Greys")
    
    plt.colorbar(img)

    plt.show()
    

def setting(error:str=None) -> list:
    try:
        os.system("cls|clear")
        for f in head:
            print(f)
        if error != None:
            print(error)
        size = int(input("Size of the picture: "))
        nb_ker = int(input("Number of kernels: "))
        minFreq = float(input("Minimum of frequency: "))
        maxFreq = float(input("Maximum of frequency: "))
        minAng = float(input("Minum angle of the vector: "))
        maxAng = float(input("Maximum angle of the vector: "))
        minBandwidth= float(input("Gaussian minimum bandwidth: "))
        maxBandwidth= float(input("Gaussian maximum bandwidth: "))
        if minFreq == maxFreq and minBandwidth == maxBandwidth:
            return [size, [[[rd.randint(0,size),rd.randint(0,size)], [math.cos(rd.uniform(minAng,maxAng)),math.sin(rd.uniform(minAng,maxAng))], minFreq, minBandwidth] for i in range(nb_ker)]]
        elif minFreq == maxFreq:
            return [size, [[[rd.randint(0,size),rd.randint(0,size)], [math.cos(rd.uniform(minAng,maxAng)),math.sin(rd.uniform(minAng,maxAng))], minFreq, rd.uniform(minBandwidth,maxBandwidth)] for i in range(nb_ker)]]
        elif minBandwidth == maxBandwidth:
            return [size, [[[rd.randint(0,size),rd.randint(0,size)], [math.cos(rd.uniform(minAng,maxAng)),math.sin(rd.uniform(minAng,maxAng))], rd.uniform(minFreq, maxFreq), minBandwidth] for i in range(nb_ker)]]
        else:
            return [size, [[[rd.randint(0,size),rd.randint(0,size)], [math.cos(rd.uniform(minAng,maxAng)),math.sin(rd.uniform(minAng,maxAng))], rd.uniform(minFreq, maxFreq), rd.uniform(minBandwidth,maxBandwidth)] for i in range(nb_ker)]]
    except:
        return setting(bcolors.FAIL +"An error occured..." + bcolors.ENDC)

sett = setting()
os.system("cls|clear")
print(bcolors.OKGREEN + "Processing ..." + bcolors.ENDC)
print()
custom_kernel(sett[0], sett[1])
print()
print(bcolors.OKGREEN + "Done §" + bcolors.ENDC)
        
