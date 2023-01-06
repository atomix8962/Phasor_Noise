import numpy as np
import matplotlib.pyplot as plt
'''
PSD.py
--> The Power Spectral Density PSD is defined by :
P = |x̂(f)|² with x̂ the Fourier Transform of the Signal
'''
def PSD(signal:list) -> list:
    signal=np.asarray(signal)
    n_x,n_y=signal.shape
    psd=[]
    for x in range(n_x):
        signal_hat=np.fft.fft(signal[x])
        psd.append(np.abs(signal_hat)**2)
    return psd

def testSignal(x,y):
    f1=5
    f2=4
    return [np.exp(-y)*np.sin(f1*2*np.pi*x),np.sin(f2*2*np.pi*y)]


def showSignalPSD(signal:list,X:list,Y:list):
    signal=np.asarray(signal)
    fig = plt.figure()
    ax_signal=fig.add_subplot(1,2,1,projection='3d')
    fig.set_size_inches(10,7)
    psd=PSD(signal)
    psd=np.asarray(psd)
    ax_signal.plot_surface(X,Y,signal)
    ax_psd=fig.add_subplot(1,2,2,projection='3d')
    ax_psd.plot_surface(X,Y,psd)
    plt.show()

n_x,n_y=100,100
X,Y=np.linspace(0,10,n_x),np.linspace(0,10,n_y)
signal=testSignal(X,Y)
showSignalPSD(signal,X,Y)