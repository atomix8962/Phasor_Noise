'''
phasor_numpy.py
--> Formule de phasor avec numpy
'''
import numpy


def numpy_gaussian(vector, bandwidth:float):
    return numpy.exp(-numpy.pi*(bandwidth**2)*(numpy.linalg.norm(vector)**2))

