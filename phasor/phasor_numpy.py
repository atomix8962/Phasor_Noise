'''
phasor_numpy.py
--> Formule de phasor avec numpy
'''
import numpy
"""
Version Numpy provisoire de la fonction gaussian
"""
def numpy_gaussian(vector, bandwidth:float):
    return numpy.exp(-numpy.pi*(bandwidth**2)*(numpy.linalg.norm(vector)**2))

def intensity(vector:list):
    pass