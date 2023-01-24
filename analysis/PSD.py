import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
'''
PSD.py
--> The Power Spectral Density PSD is defined by :
P = |x̂(f)|² with x̂ the Fourier Transform of the Signal

PSD(signal) return the Power Spectral Density of a signal

plotPSD(X,Y,signal,ax) plot the Power Spectral Density on a 3D axis

'''
def PSD(signal:list) -> np.array:
    signal=np.asarray(signal)
    signal_hat=np.fft.fft(signal)
    return np.abs(signal_hat)**2

def plotPSD(X:list, Y:list, signal:list, ax:matplotlib.axes) -> None:
    psd=PSD(signal)
    signal=np.asarray(signal)
    ax=fig.add_subplot(1,2,2,projection='3d')
    cmap=mpl.colormaps['plasma']
    ax.plot_surface(X,Y,psd,cmap=cmap)