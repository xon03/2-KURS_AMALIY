import numpy as np
import matplotlib.pyplot as plt
import math
T1 = [[0.0 for j in range(10)] for i in range(10)]
T2 = [[0.0 for j in range(10)] for i in range(10)]
input()
for i in range(10):
    T1[i][9]=50
for J in range(10):
    T1[9][J]=30
    
# massivni chiqarish
for i in range(10):
    for j in range(10):
        print(f"{T1[i][j]:5.2f}", end=" ")
    print()
input()
T2=T1
for J in range(1,9):
    for I in range(1, 9):
        T2[I][J]=T1[I][J]+0.25*(T1[I][J+1]+T1[I][J-1]+T1[I-1][J]+T1[I+1][J]-4*T1[I][J])
for i in range(10):
    for j in range(10):
        print(f"{T2[i][j]:5.2f}", end=" ")
    print()
x = np.linspace(0, 10, 10)
y = np.linspace(0, 10, 10)
X, Y = np.meshgrid(x, y)
contour = plt.contourf(X, Y, T2, cmap='viridis') # 
plt.clabel(contour, inline=True, fontsize=10) # 
plt.colorbar(contour) # 
plt.title("Konturli grafik")
plt.show()

#input()    
