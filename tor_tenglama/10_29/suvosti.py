import matplotlib.pyplot as plt
import math
p0=1000
p1=850
v=40/(3.6)
H=15
g=9.8
L=v*(p1*H/(g*(p0-p1)))**(1/2)
n=int(L/0.1)
h = [0.0 for j in range(n)]
l = [0.0 for j in range(n)]
for i in range(n):
    l[i] = i*0.1
for i in range(n):
    h[i] = g*(p0-p1)/(p1*v**2)*l[i]**2
print(f"L={L}, {n} ta qadamda bajarildi.")
plt.plot(l,h, '.-')
plt.title("Suv osti kemasi", fontsize=15)
plt.grid(True)
plt.xlabel("l", fontsize=12)
plt.ylabel('h', fontsize=12)
plt.show()
