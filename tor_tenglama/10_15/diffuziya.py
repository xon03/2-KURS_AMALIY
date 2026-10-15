import numpy as np
import matplotlib.pyplot as plt
import math
#u = [[0.0 for j in range(10)] for i in range(10)]
u0=[0.0 for j in range(11)]
u1=[0.0 for j in range(11)]
u2=[0.0 for j in range(11)]
u3=[0.0 for j in range(11)]
u4=[0.0 for j in range(11)]
u5=[0.0 for j in range(11)]

# boshlang'ich va chegaraviy shart
n=11
for j in range(0, n-1):
    u0[j] = 1
for j in range(n):
    print(f"{u0[j]:5.2f}", end=" ")
input("davom ettirish uchun enterni bosing")