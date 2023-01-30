'''
--> Formule de phasor avec python
'''
import math
def gaussian(vector:list, bandwidth:float):
    return math.exp(-math.pi*(bandwidth**2)*dot(vector, vector))


def dot(vector1: list, vector2: list):
    return vector1[0]*vector2[0]+vector1[1]*vector2[1]


def vector_subtraction(vector1: list, vector2: list):
    return [vector1[0]-vector2[0], vector1[1]-vector2[1]]


def polar_coordinates_coefficients(x: list, kernel_array: list):
    return [gaussian(vector_subtraction(x, kernel[0]), kernel[3]) * math.sin(-dot(vector_subtraction(x, kernel[0]), kernel[1]) * kernel[2]) for kernel in kernel_array],\
           [gaussian(vector_subtraction(x, kernel[0]), kernel[3]) * math.cos(-dot(vector_subtraction(x, kernel[0]), kernel[1]) * kernel[2]) for kernel in kernel_array]

"""
x: position in the image
kernel_array : list of
[position, direction, frequency, bandwidth]
"""
def intensity(x: list, kernel_array: list):
    l1, l2 = polar_coordinates_coefficients(x, kernel_array)
    return math.sqrt(sum(l1)**2+sum(l2)**2)

"""
x: position in the image
kernel_array : list of
[position, direction, frequency, bandwidth]
"""
def phase_func(x: list, kernel_array: list):
    l1, l2 = polar_coordinates_coefficients(x, kernel_array)
    return math.atan2(sum(l1), sum(l2))

"""
x: position in the image
kernel_array : list of
[position, direction, frequency, bandwidth]
"""
def sine_wave(x: list, kernel_array: list):
    return math.sin(phase_func(x, kernel_array))

"""
x: position in the image
kernel_array : list of
[position, direction, frequency, bandwidth]
"""
def phasor_noise(x: list, kernel_array: list):
    #return scipy.signal.sawtooth(phase_func(x, kernel_array))
    return sine_wave(x, kernel_array)