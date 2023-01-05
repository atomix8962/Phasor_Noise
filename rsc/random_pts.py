import random,math

def new_pts(size:list=[255,255]) -> list:
    ptsArray = list()
    incr = 0
    for x in range(size[0]):
        for y in range(size[1]):
            ptsArray.append([incr,[x,y]])
            incr += 1
    return ptsArray


def create_rdm_data(ptsArray:list) -> list:
    dataArray = list()
    for pt in ptsArray:
        numPt = pt[0]
        xd = random.choice([-1,1])
        yd = random.choice([-math.sqrt(1-xd**2), math.sqrt(1-xd**2)])
        direction = [xd,yd]
        frequency = random.uniform(0, 100000000) #R+
        phase = random.uniform(-math.pi,math.pi)
        dataArray.append([numPt,direction,frequency,phase])
    return dataArray


