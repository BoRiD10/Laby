from control.matlab import *
import matplotlib.pyplot as mp

def Function ( num, den, num1, den1):
    w = tf( num, den)
    W = tf( num1, den1)
    y, x = step(w)
    y1,x1 = step(W)
    lines = [w, W]
    lines[0],lines[1] = mp.plot(y,"r",y1,"b")
    mp.legend(lines, ['w', 'W'])
    mp.title('Переходная Характеристика')
    mp.ylabel('Амплитуда')
    mp.xlabel('Время(с)')
    mp.grid(True)
    mp.show()

    y,x = impulse(w)
    y1,x1 = impulse(W)
    lines = [w, W]
    lines[0], lines[1] = mp.plot(y,"r",y1,"b")
    mp.title('Импульсная Характеристика')
    mp.ylabel('Амплитуда')
    mp.xlabel('Время(с)')
    mp.grid(True)
    mp.show()

    mp.figure()
    amp, phase, freq = bode(w, dB=False)
    amp, phase, freq = bode(W, dB=False)
    mp.plot()
    mp.show()

    return W
    return w

inerless = Function([4.],[1e-10, 1],[8.],[1e-10, 1])
aperiodic = Function([4.],[5.,1.],[8.],[2.5,1.])
integr = Function([1.],[1.,0.],[1.],[0.5,0.])
realDiff = Function([3.,0.],[1e-10, 1.],[6.,0.],[1e-10, 1.])
perfDiff = Function([4.,0.],[5.,1.],[8.,0.],[2.5,1.])