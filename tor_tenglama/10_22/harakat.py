import matplotlib.pyplot as plt
import math
x = [0.0 for j in range(51)]
t = [0.0 for j in range(51)]
for i in range(51):
    t[i] =i*0.1
m=2
f=10
v0=3
x0=0
for i in range(51):
    x[i] = x0+v0*t[i]+f*t[i]*t[i]/(2*m)
print(x)
plt.plot(t,x, '.-')
plt.title("Harakat", fontsize=15)
plt.grid(True)
plt.xlabel("t", fontsize=12)
plt.ylabel('x', fontsize=12)
plt.show()
