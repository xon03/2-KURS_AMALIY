import matplotlib.pyplot as plt
import math
u = [0.0 for j in range(21)]
y = [0.0 for j in range(21)]
for i in range(21):
    y[i] =-1.0+ i*0.1
myu=0.01
dpx = 5
b = 1
for i in range(21):
    u[i] = 1/(2*myu)*dpx*(b*b-y[i]*y[i])
print(u)
plt.plot(u,y, 'o-')
plt.title("Oqim", fontsize=15)
plt.grid(True)
plt.xlabel("U", fontsize=12)
plt.ylabel('y', fontsize=12)
plt.show()
