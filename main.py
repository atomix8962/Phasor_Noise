from rsc.impr_img import *
from rsc.random_pts import *
from phasor.phasor_py import *
from analysis.histogrm import *

ptsArray = new_pts([150,150])
dataArray = create_rdm_data(ptsArray)
input(len(ptsArray))
kernelArray = [22499]

noiseArray = phasor_generator(ptsArray,dataArray, kernelArray, [150,150], 0.5)

impr_img(noiseArray)