import numpy as np
import matplotlib.pyplot as plt
import math
#u = [[0.0 for j in range(10)] for i in range(10)]
u0=[0.0 for j in range(11)]
u1=[0.0 for j in range(11)]
t0=[0.0 for j in range(11)]
t1=[0.0 for j in range(11)]
t2=[0.0 for j in range(11)]
t3=[0.0 for j in range(11)]
x=[0.0 for j in range(11)]
# boshlang'ich va chegaraviy shart
n=11
for j in range(0, n-1):
    u0[j] = 1
u0[n-1]=0.1
u1[n-1]=0.1
for j in range(n):
    print(f"{u0[j]:5.2f}", end=" ")
input("davom ettirish uchun enterni bosing")
for k in range(20):
    u1[0]=u0[0]+2*0.5*(u0[1]-u0[0])
    for j in range(1,n-1):
        u1[j]=u0[j]+0.5*(u0[j+1]-2*u0[j]+u0[j-1])
    for j in range(n):
        print(f"{u1[j]:5.2f}", end=" ")
    if k==4:
        for i in range(n):
            t0[i]=u1[i]
    if k==8:
        for i in range(n):
            t1[i]=u1[i]
    if k==12:
        for i in range(n):
            t2[i]=u1[i]
    if k==16:
        for i in range(n):
            t3[i]=u1[i]
    u0=u1
    print("")
for i in range(11):
    x[i]=i
plt.plot(x,t0,'-',x,t1,'-.',x,t2,'--',x,t3,'.')
plt.title("Sterjenda temperatura o'zgarishi", fontsize=15)
plt.grid(True)
plt.xlabel("x", fontsize=12)
plt.ylabel('Temperature', fontsize=12)
plt.legend(('5-qatlam', '9-qatlam', '13-qatlam','17-qatlam'))
plt.show()




















