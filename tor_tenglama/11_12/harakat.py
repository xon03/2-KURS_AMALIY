import numpy as np
import matplotlib.pyplot as plt
import math
#u = [[0.0 for j in range(10)] for i in range(10)]
u0=[0.0 for j in range(11)]
u1=[0.0 for j in range(11)]
u2=[0.0 for j in range(11)]
u3=[0.0 for j in range(11)]
t1=[0.0 for j in range(11)]
t2=[0.0 for j in range(11)]
t3=[0.0 for j in range(11)]
z1=[0.0 for j in range(11)]
z2=[0.0 for j in range(11)]
z3=[0.0 for j in range(11)]
u4=[0.0 for j in range(11)]
u5=[0.0 for j in range(11)]
v0=[0.0 for j in range(11)]
v1=[0.0 for j in range(11)]
x=[0.0 for j in range(11)]
# boshlang'ich va chegaraviy shart
n=10
u1[n]=1
u0[n]=1
hx=0.0005
hy=0.00055
Re=20000
for j in range(1, n):
    u0[j] = 1
for j in range(n):
    print(f"{u0[j]:5.2f}", end=" ")
for k in range(10):    
    print(f"\n {k}")
    for j in range(1,n-1):
        u1[j]=u0[j]+hx/u0[j]*(1/Re * (u0[j+1]-2*u0[j]+u0[j-1])/hy/hy-v0[j]*(u0[j]-u0[j-1])/hy)
        v1[j]=v1[j-1]-hy/hx*(u1[j]-u0[j])
    if k==2:
        for i in range(n):
            t1[i]=u1[i]
            z1[i]=v1[i]
    if k==5:
        for i in range(n):
            t2[i]=u1[i]
            z2[i]=v1[i]
    if k==9:
        for i in range(n):
            t3[i]=u1[i]
            z3[i]=v1[i]
    for j in range(n):
        print(f"{u1[j]:5.2f}", end=" ")
    print()
    for j in range(n):
        print(f"{v0[j]:5.2f}", end=" ")
    u0=u1
    v0=v1
for i in range(n):
    x[i]=i
plt.plot(x,t1,'-',x,t2,'-.',x,t3,'.')
plt.title("Laminar oqim", fontsize=15)
plt.grid(True)
plt.xlabel("x", fontsize=12)
plt.ylabel('Temperature', fontsize=12)
plt.legend(('2-qatlam', '5-qatlam', '9-qatlam'))
plt.show()