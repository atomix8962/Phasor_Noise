import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
'''
PSD.py
--> The Power Spectral Density PSD is defined by :
P = |x̂(f)|² with x̂ the Fourier Transform of the Signal
'''
def PSD(signal:list) -> list:
    signal=np.asarray(signal)
    signal_hat=np.fft.fft(signal)
    return np.abs(signal_hat)**2

def testSignal(x,y):
    f1=5
    f2=4
    return np.exp(-y)*np.sin(f1*2*np.pi*x)+np.sin(f2*2*np.pi*y)


def showSignalPSD(X:list,Y:list,signal:list):
    psd=PSD(signal)
    signal=np.asarray(signal)
    psd=np.asarray(psd)
    fig = plt.figure()
    fig.set_size_inches(10,7)
    ax_signal=fig.add_subplot(1,2,1,projection='3d')
    ax_psd=fig.add_subplot(1,2,2,projection='3d')
    cmap=mpl.colormaps['plasma']
    ax_signal.plot_surface(X,Y,signal,cmap=cmap)
    ax_psd.plot_surface(X,Y,psd,cmap=cmap)
    plt.show()

n_x,n_y=100,100
X,Y=np.linspace(0,3,n_x),np.linspace(0,3,n_y)
X,Y=np.meshgrid(X,Y)
signal=testSignal(X,Y)
showSignalPSD(X,Y,signal)