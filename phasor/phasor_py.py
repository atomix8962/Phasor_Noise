'''
phasor_py.py
--> Formule de phasor avec python
'''
import math

def gaussian(vector:list, bandwidth:float):
    x = vector[0]
    y = vector[1]
    return math.exp(-math.pi*(bandwidth**2)*((x**2)+(y**2)))


def intensity(vector:list, dx:float, dy:float, ptsArray:list, kernelArray:list, bandwidth:float, f:float):
    res1 = 0
    res2 = 0
    for ker in kernelArray:
        new_x = vector[0] - ptsArray[ker][1][0]
        new_y = vector[1] - ptsArray[ker][1][1]
        res1 = res1 + (gaussian([new_x,new_y], bandwidth)*math.sin(-(new_x*dx+new_y*dy)*f))
        res2 = res2 + (gaussian([new_x,new_y], bandwidth)*math.cos(-(new_x*dx+new_y*dy)*f))
    return math.sqrt(res1**2 + res2**2)

def phase_func(vector:list, dx:float, dy:float, ptsArray:list, kernelArray:list, bandwidth:float, f:float):
    res1 = 0
    res2 = 0
    for ker in kernelArray:
        new_x = vector[0] - ptsArray[ker][1][0]
        new_y =vector[1] - ptsArray[ker][1][1]
        res1 = res1 + (gaussian([new_x,new_y], bandwidth)*math.sin(-(new_x*dx+new_y*dy)*f))
        res2 = res2 + (gaussian([new_x,new_y], bandwidth)*math.cos(-(new_x*dx+new_y*dy)*f))
    return math.atan2(res1,res2)

def sine_wave(vector:list, direction_x:int, direction_y:int, frequency:float, phase_f:float):
    return math.sin((direction_x*vector[0]+ direction_y*vector[1])*frequency + phase_f)

def phasor_generator(ptsArray:list,dataArray:list, kernelArray:list, size:list, bandwidth:float) -> list:
    noiseArray = list()
    for x in range(size[0]):
        line = list()
        for y in range(size[1]):
            line.append(0)
        noiseArray.append(line)

    for pt in dataArray:
        num = pt[0]
        direction_x  = pt[1][0]
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