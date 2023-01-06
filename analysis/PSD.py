import numpy as np
import matplotlib.pyplot as plt
'''
PSD.py
--> The Power Spectral Density PSD is defined by :
P = |x̂(f)|² with x̂ the Fourier Transform of the Signal
'''
def PSD(signal):
    signal_hat=np.fft.fft(signal)
    psd=np.abs(signal_hat)**2
    return psd

def testSignal(x,y):
    f1=1
    f2=2
    return np.sin(f1*2*np.pi*x)+np.sin(f2*2*np.pi*y)

X,Y=np.arange(0,5,0.01),np.arange(0,10,0.02)
signal=testSignal(X,Y)
psd=PSD(signal)
fig, (ax1,ax2,ax3)=plt.subplots(3,1)
ax1.plot(X,signal)
ax2.plot(Y,signal)
ax3.plot(X,psd)
plt.show()