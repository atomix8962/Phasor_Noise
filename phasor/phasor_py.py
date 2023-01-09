'''
phasor_py.py
--> Formule de phasor avec python
'''
import math
"""
    Attention j'ai pas encore test/ Code temporaire.
"""

def gaussian(vector:list, bandwidth:float):
    x = vector[0]
    y = vector[1]
    return math.exp(-math.pi*(bandwidth**2)*((x**2)+(y**2)))


def dot(vector1: list, vector2: list):
    return vector1[0]*vector2[0]+vector1[1]*vector2[1]


def vector_subtraction(vector1: list, vector2: list):
    return [vector1[0]-vector2[0], vector1[1]-vector2[1]]


def polar_coordinates_coefficients(vector: list, u: list, kernel_array: list, bandwidth: float, frequency: int):
    return [gaussian(vector_subtraction(vector, kernel), bandwidth) * math.sin(-dot(kernel, u) * frequency) for kernel in kernel_array],\
           [gaussian(vector_subtraction(vector, kernel), bandwidth) * math.cos(-dot(kernel, u) * frequency) for kernel in kernel_array]


def intensity(vector: list, u: list, kernel_array: list, bandwidth: float, frequency: float):
    l1, l2 = polar_coordinates_coefficients(vector, u, kernel_array, bandwidth, frequency)
    return math.sqrt(sum(l1)**2+sum(l2)**2)


def phase_func(vector: list, u: list, kernel_array: list, bandwidth: float, frequency: float):
    l1, l2 = polar_coordinates_coefficients(vector, u, kernel_array, bandwidth, frequency)
    return math.atan2(sum(l1), sum(l2))


def sine_wave(vector: list, u: list, frequency: float, kernel_array: list, bandwidth: float):
    return math.sin(frequency*dot(vector, u)+phase_func(vector, u, kernel_array, bandwidth, frequency))


def phasor_noise(vector: list, u: list, kernel_array: list, bandwidth: float, frequency: float):
    return intensity(vector, u, kernel_array, bandwidth, frequency)*sine_wave(vector, u, frequency, kernel_array, bandwidth)


def phasor_generator(ptsArray: list, dataArray: list, kernelArray: list, size: list, bandwidth: float) -> list:
    noiseArray = list()
    for x in range(size[0]):
        line = list()
        for y in range(size[1]):
            line.append(0)
        noiseArray.append(line)

    for pt in dataArray:
        num = pt[0]
        direction_x = pt[1][0]
        direction_y = pt[1][1]
        frequency = pt[2]*2*math.pi
        phase = pt[3]
        x = ptsArray[num][1][0]
        y = ptsArray[num][1][1]
        
        intens = intensity([x,y],direction_x,direction_y,ptsArray, kernelArray, bandwidth, frequency)
        phase_f = phase_func([x,y],direction_x,direction_y,ptsArray, kernelArray, bandwidth, frequency)
        sin_w = sine_wave([x,y], direction_x, direction_y, frequency, phase_f)

        phasorNoise = intens*sin_w
        noiseArray[x][y] = phasorNoise
    
    return noiseArray