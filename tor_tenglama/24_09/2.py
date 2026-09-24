import numpy as np
import matplotlib.pyplot as plt
import math
T1 = [[0.0 for j in range(10)] for i in range(10)]
T2 = [[0.0 for j in range(10)] for i in range(10)]
x=[0 for j in range(10)]
# boshlang'ich shart
for i in range(1, 9):
    T1[i][0] = 10
    T1[i][9] = 20
# chegaraviy shartlar
for j in range(10):
    T1[0][j] = 50
    T1[9][j] = 30
T2=T1
print("Boshlang'ich qiymatlar:\n")
# massivni chiqarish
for i in range(10):
    for j in range(10):
        print(f"{T1[i][j]:5.2f}", end=" ")
    print()
print("\n")
for j in range(9):
    for i in range(1,9):
        T2[i][j] = T1[i][j] +0.25*(T1[i+1][j]+T1[i-1][j]+T1[i][j+1]+T1[i][j-1]-4*T1[i][j])
for i in range(10):
    for j in range(10):
        print(f"{T2[i][j]:5.2f}", end=" ")
    print()