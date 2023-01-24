import numpy as np


def gaussian(entry:list,bandwidth=255:int) -> tuple(list,list):
    return np.histogram(entry,bins=bandwidth/100) 