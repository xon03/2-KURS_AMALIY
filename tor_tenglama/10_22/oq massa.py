import matplotlib.pyplot as plt
import math
v = [0.0 for j in range(11)]
m = [0.0 for j in range(11)]
for i in range(1, 11):
    m[i] = i * 0.001
M = 0.5
g = 9.8
l = 1
a = math.pi / 3
for i in range(1, 11):
    v[i] = math.sqrt(2 * (m[i] + M) * g * l * (1 - math.cos(a))) / m[i]
print(v[1:])
plt.plot(m[1:], v[1:], 'o-')
plt.title("O'q tezligining uning massasiga bog'liqligi", fontsize=15)
plt.grid(True)
plt.xlabel("O'q massasi", fontsize=12)
plt.ylabel('Tezlik', fontsize=12)
plt.show()
