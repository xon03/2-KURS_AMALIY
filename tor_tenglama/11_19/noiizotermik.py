import numpy as np
import matplotlib.pyplot as plt
import math
#u = [[0.0 for j in range(10)] for i in range(10)]
u1=[0.0 for j in range(11)]
u2=[0.0 for j in range(11)]
t1=[0.0 for j in range(11)]
t2=[0.0 for j in range(11)]
v1=[0.0 for j in range(11)]
v2=[0.0 for j in range(11)]
x=[0.0 for j in range(11)]
# boshlang'ich va chegaraviy shart
n=10
u1[0]=0
u1[n]=1
v1[0]=0
v1[n]=0
t1[0]=0.25
t2[0]=0.25
hx=0.0005
hy=0.00055
Re=2000
Pr=0.7
for j in range(1, n):
    u1[j] = 1
    t1[j]=1
    t2[j]=1
    v1[j]=0
print("\nu1")
for j in range(n):
    print(f"{u1[j]:5.2f}", end=" ")
print("\nv1")
for j in range(n):
    print(f"{v1[j]:5.2f}", end=" ")
print("\nt1")
for j in range(n):
    print(f"{t1[j]:5.2f}", end=" ")
print("\nu2")
for j in range(1,n-1):
    u2[j]=u1[j]+hx/hy*(1/Re/hy*(u1[j+1]-2*u1[j]+u1[j-1])+v1[j]*(u1[j]-u1[j-1]))/u1[j]
    v1[j+1]=v1[j]+hy/hx*(u1[j]-u2[j])
    t2[j]=t1[j]+hx/hy*(1/Re/Pr/hy*(t1[j+1]-2*t1[j]+t1[j-1])+v1[j]*(t1[j]-t1[j-1]))/u1[j]
for j in range(n):
    print(f"{u2[j]:5.2f}", end=" ")
print("\nv2")
for j in range(n):
    print(f"{v2[j]:5.2f}", end=" ")
print("\nt2")
for j in range(n):
    print(f"{t2[j]:5.2f}", end=" ")