import numpy as np
import matplotlib.pyplot as plt
'''
PSD.py
--> The Power Spectral Density PSD of a bi-dimensional signal using the DFT
Input : A numpy array of dimension NxM
'''
def PSD_2D(signalArray:np.array) -> np.array:
    n_x,n_y=signalArray.shape
    psd=np.zeros((n_x,n_y))
    for y in range(n_y):
        #Applying the Discrete Fourier Transform
        dft=np.fft.fft(signalArray[:,y])
        dft_amp=np.abs(dft)
        psd[:,y]=dft_amp**2/(2*np.pi)
    return psd