import numpy as np


def gaussian(entry:list,bandwidth:int=255) -> tuple:
    return np.histogram(entry,bins=bandwidth/100) 