from control.matlab import *
import matplotlib.pyplot as mp
import numpy as np

def Function ( num, den, num1, den1,t):
    w = tf( num, den)
    W = tf( num1, den1)
    y, x = step(w,t)
    y1,x1 = step(W,t)
    lines = [w, W]
    lines[0],lines[1] = mp.plot(x,y,"r",x1,y1,"b")
    mp.legend(lines, ['W1', 'W2'])
    mp.title('Переходная Характеристика')
    mp.ylabel('h(t)')
    mp.xlabel('t,с')
    mp.grid(True)
    mp.show()

    y,x = impulse(w,t)
    y1,x1 = impulse(W,t)
    mp.legend(lines, ['W1', 'W2'])
    lines[0], lines[1] = mp.plot(x,y,"r",x1,y1,"b")
    mp.title('Импульсная Характеристика')
    mp.ylabel('h(t)')
    mp.xlabel('t, с')
    mp.grid(True)
    mp.show()

    mp.figure()
    amp, phase, freq = bode(w, dB=False)
    amp, phase, freq = bode(W, dB=False)
    mp.plot()
    mp.show()

    return W
    return w

t = np.linspace(0, 20, 100)
inerless = Function([4.],[1.],[8.],[1.],t)
aperiodic = Function([4.],[5.,1.],[8.],[2.5,1.],t)
integr = Function([1.],[1.,0.],[1.],[0.5,0.],t)
realDiff = Function([3.,0.],[1e-10, 1.],[6.,0.],[1e-10, 1.],t)
perfDiff = Function([4.,0.],[5.,1.],[8.,0.],[2.5,1.],t)
