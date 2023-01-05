import math

def gaussian(vector:list, bandwidth:float):
    x = vector[0]
    y = vector[1]
    return math.exp(-math.pi*(bandwidth**2)*((x**2)+(y**2)))

def intensity(vector:list):
    pass

def phase_func(vector:list):
    pass

def sine_wave(vector:list, direction_x:int, direction_y:int, frequency:float, phase:float):
    pass

def phasor_generator(ptsArray:list,dataArray:list, size:list) -> list:
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
        frequency = pt[2]
        phase = pt[3]
        x = ptsArray[num][0]
        y = ptsArray[num][1]
        
        phasorNoise = intensity([x,y])*sine_wave([x,y], direction_x, direction_y, frequency, phase)

