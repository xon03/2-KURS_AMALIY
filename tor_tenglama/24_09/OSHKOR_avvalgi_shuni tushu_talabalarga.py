import numpy as np
import matplotlib.pyplot as plt
import math
u = [[0.0 for j in range(10)] for i in range(10)]
T1=[0.0 for j in range(10)]
T2=[0.0 for j in range(10)]
T3=[0.0 for j in range(10)]
T4=[0.0 for j in range(10)]
x=[0 for j in range(10)]
# boshlang'ich shart
for i in range(1, 9):
    u[i][0] = 10
# chegaraviy shartlar
for j in range(10):
    u[0][j] = 50
    u[9][j] = 30
print("Boshlang'ich qiymatlar:\n")
# massivni chiqarish
for i in range(10):
    for j in range(10):
        print(f"{u[i][j]:5.2f}", end=" ")
    print()
input()    
lamda = 0.5
print("\nHisoblangan natija:\n")
# hisoblash
for j in range(9):
    for i in range(1, 9):
        u[i][j+1] = (1 - 2*lamda) * u[i][j] + lamda * (u[i-1][j] + u[i+1][j])

for i1 in range(10):
            T1[i1]=u[i1][0]
            T2[i1]=u[i1][4]
            T3[i1]=u[i1][5]
# natijani chiqarish
for i in range(10):
    for j in range(10):
        print(f"{u[i][j]:5.2f}", end=" ")
    print()
input()
for i in range(10):
    x[i]=i
plt.plot(x, T1,'-',x,T2,'-.',x,T3,'--')
plt.title("sterjenda temperatura o'zgarishi", fontsize=15)
plt.grid(True)
plt.xlabel('x',fontsize=12)
plt.ylabel('Temperatura',fontsize=12)
plt.legend(('3-qatlam','5-qatlam','7-qatlam'))
plt.show()
