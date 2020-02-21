import cmath
import keyboard
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

m = 0.5
r = 0.01
k = 8.5
dt = 0.0001
q = 100
N = 100
pi = 3.1415
w = 20
p = 0
ksi = np.zeros(N+1, complex)
eta = np.zeros(N, complex)
E = np.zeros(N, complex)
t = 0

while True:
    t += dt
    Sum_E = 0
    p += 1
    i = 2
    for i in range (N-1):
        ksi[N] = 100
        test = E[i]
        Sum_E += test
        if w * t < pi:
            ksi[1] = 1 * cmath.sin(w * t)
        else:
            ksi[1] = 0
        F = q *(ksi[i-1] - ksi[i]) + q * (ksi[i+1] - ksi[i])
        teta = (F - r * eta[i] - k * ksi[i]) / m
        ksi[i] = ksi[i] + eta[i] * dt + teta * dt * dt / 2
        eta[i] = eta[i] + teta * dt
        E[i] = q * cmath.sqrt(ksi[i-1]-ksi[i])/2 + k * ksi[i] * ksi[i] / 2 + m * eta[i] * eta[i] / 2
    if p % 20 == 20:
        p = 0
        i = 2
        for i in range (N-1):
            plt.figure()
            currentAxis = plt.gca()
            currentAxis.add_path(Rectangle(6*i, 400, 5*i+2, 400 - round(Sum_E), fill=None))

    if keyboard.is_pressed:
        break
plt.show()
