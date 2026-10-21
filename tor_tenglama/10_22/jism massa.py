import matplotlib.pyplot as plt
import math
M = [i * 0.1 for i in range(3, 11)]
v = [0.0 for j in range(8)]
m = 0.001
g = 9.8
l = 1
a = math.pi / 3
for i in range(8):
    v[i] = math.sqrt(2 * (m + M[i]) * g * l * (1 - math.cos(a))) / m
plt.plot(M, v, 'o-')
plt.title("O'q tezligi", fontsize=14)
plt.grid(True)
plt.xlabel("Jism massasi", fontsize=12)
plt.ylabel('Tezlik', fontsize=12)
plt.show()
