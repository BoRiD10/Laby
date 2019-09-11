from control.matlab import *
from numpy import *
import matplotlib.pyplot as mp

inerless = "1. Безинерционное"
aperiodic = "2. Апериодическое"
integr = "3. Интегрирующее"
realDiff = "4. Идеальное дифференцирующее"
perfDiff = "5. Реальное дифференцирующее"

print("Выберите звено: " "\n\t" + inerless +"\n\t"+ aperiodic +"\n\t"+ integr +"\n\t"+ realDiff +"\n\t"+ perfDiff)
zveno = input('Номер звена: ')

if zveno == "1":
    k = float(input("Введите К: "))
    #T = float(input("Введите T: "))
    num = [k]
    den= [1e-10, 1.]
    w= tf(num, den)
    print(w)
    print("Выберите снимаемую характеристику:\n\t1. Переходная \n\t2. Импульсная \n\t3. АЧХ и ФЧХ")
    Har = input("Номер характеристики: ")
    if Har == "1":
        y, x = step(w)
        mp.plot(x, y)
        mp.title('Переходная Характеристика')
        mp.ylabel('Амплитуда')
        mp.xlabel('Время(с)')
        mp.grid(True)
        mp.show()
    if Har == "2":
        y, x = impulse(w)
        mp.plot(x, y)
        mp.title('Импульсная Характеристика')
        mp.ylabel('Амплитуда')
        mp.xlabel('Время(с)')
        mp.grid(True)
        mp.show()
    if Har == "3":
        amp, phase, freq = bode(w, dB=False)
        mp.plot()
        mp.show()

if zveno == "2":
    k = float(input("Введите К: "))
    T = float(input("Введите T: "))
    num = [k]
    den= [T, 1.]
    w= tf(num, den)
    print(w)
    print("Выберите снимаемую характеристику:\n\t1. Переходная \n\t2. Импульсная \n\t3. АЧХ и ФЧХ")
    Har = input("Номер характеристики: ")
    if Har == "1":
        y, x = step(w)
        mp.plot(x, y)
        mp.title('Переходная характеристика')
        mp.ylabel('Амплитуда')
        mp.xlabel('Время(с)')
        mp.grid(True)
        mp.show()
    if Har == "2":
        y, x = impulse(w)
        mp.plot(x, y)
        mp.title('Импульсная характеристика')
        mp.ylabel('Амплитуда')
        mp.xlabel('Время(с)')
        mp.grid(True)
        mp.show()
    if Har == "3":
        amp, phase, freq = bode(w, dB=False)
        mp.plot()
        mp.show()

if zveno == "3":
    #k = float(input("Введите К: "))
    T = float(input("Введите T: "))
    num = [1]
    den= [T, 0.]
    w= tf(num, den)
    print(w)
    print("Выберите снимаемую характеристику:\n\t1. Переходная \n\t2. Импульсная \n\t3. АЧХ и ФЧХ")
    Har = input("Номер характеристики: ")
    if Har == "1":
        y, x = step(w)
        mp.plot(x, y)
        mp.title('Переходная характеристика')
        mp.ylabel('Амплитуда')
        mp.xlabel('Время(с)')
        mp.grid(True)
        mp.show()
    if Har == "2":
        y, x = impulse(w)
        mp.plot(x, y)
        mp.title('Импульсная характеристика')
        mp.ylabel('Амплитуда')
        mp.xlabel('Время(с)')
        mp.grid(True)
        mp.show()
    if Har == "3":
        amp, phase, freq = bode(w, dB=False)
        mp.plot()
        mp.show()

if zveno == "4":
    k = float(input("Введите К: "))
    #T = float(input("Введите T: "))
    num = [k]
    den= [1e-10, 1.]
    w= tf(num, den)
    print(w)
    print("Выберите снимаемую характеристику:\n\t1. Переходная \n\t2. Импульсная \n\t3. АЧХ и ФЧХ")
    Har = input("Номер характеристики: ")
    if Har == "1":
        y, x = step(w)
        mp.plot(x, y)
        mp.title('Переходная характеристика')
        mp.ylabel('Амплитуда')
        mp.xlabel('Время(с)')
        mp.grid(True)
        mp.show()
    if Har == "2":
        y, x = impulse(w)
        mp.plot(x, y)
        mp.title('Импульсная характеристика')
        mp.ylabel('Амплитуда')
        mp.xlabel('Время(с)')
        mp.grid(True)
        mp.show()
    if Har == "3":
        amp, phase, freq = bode(w, dB = False)
        mp.plot()
        mp.show()

if zveno == "5":
    k = float(input("Введите К: "))
    T = float(input("Введите T: "))
    num = [k, 0.]
    den= [T, 1.]
    w= tf(num, den)
    print(w)
    print("Выберите снимаемую характеристику:\n\t1. Переходная \n\t2. Импульсная \n\t3. АЧХ и ФЧХ")
    Har = input("Номер характеристики: ")
    if Har == "1":
        y, x = step(w)
        mp.plot(x, y)
        mp.title('Переходная характеристика')
        mp.ylabel('Амплитуда')
        mp.xlabel('Время(с)')
        mp.grid(True)
        mp.show()
    if Har == "2":
        y, x = impulse(w)
        mp.plot(x, y)
        mp.title('Импульсная характеристика')
        mp.ylabel('Амплитуда')
        mp.xlabel('Время(с)')
        mp.grid(True)
        mp.show()
    if Har == "3":
        amp, phase, freq = bode(w, dB=False)
        mp.plot()
        mp.show()




# num= [4.]
# den= [5., 1.]
# w= tf(num, den)
# print(w)
# y,x=step(w)
# #y,x=impulse(w)
# #amp, phase, freq = bode(w)
# mp.plot(x,y)
# #mp.plot()
# mp.title('Характеристика')
# mp.ylabel('Амплитуда')
# mp.xlabel('Время(с)')
# mp.grid(True)
# mp.show()