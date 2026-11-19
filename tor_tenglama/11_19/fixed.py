import matplotlib.pyplot as plt
import math
import numpy as np

# Grid va parametrlar
n = 10
hx = 0.0005
hy = 0.00055
Re = 2000
Pr = 0.7

# Massivlarni e'lon qilish
u1 = [0.0 for j in range(n + 1)]
u2 = [0.0 for j in range(n + 1)]
v1 = [0.0 for j in range(n + 1)]
v2 = [0.0 for j in range(n + 1)]
t1 = [0.0 for j in range(n + 1)]
t2 = [0.0 for j in range(n + 1)]

# Grafik uchun saqlanadigan qatlamlar (3, 5, 7-qatlamlar)
t_layer3 = [0.0 for j in range(n + 1)]
t_layer5 = [0.0 for j in range(n + 1)]
t_layer7 = [0.0 for j in range(n + 1)]
x = [float(i) for i in range(n + 1)]

# Boshlang'ich va chegaraviy shartlar (k = 0)
u1[0] = 0.0
v1[0] = 0.0
t1[0] = 0.25

for j in range(1, n + 1):
    u1[j] = 1.0
    v1[j] = 0.0
    t1[j] = 1.0

print("Boshlang'ich u1:")
for j in range(n + 1):
    print(f"{u1[j]:5.2f}", end=" ")

# Asosiy hisoblash sikli (x yo'nalishi bo'yicha 10 ta qadam)
for k in range(10):
    print(f"\n\n--- {k}-qatlam ---")
    
    # Chegaraviy shartlarni yangi qatlam uchun saqlash
    u2[0] = 0.0
    u2[n] = 1.0
    v2[0] = 0.0
    t2[0] = 0.25
    t2[n] = 1.0

    # Ichki tugunlar uchun chekli ayirmalar usuli (j = 1 dan n-1 gacha)
    for j in range(1, n):
        # Tezlik (u) tenglamasi
        u2[j] = u1[j] + (hx / u1[j]) * (
            (1.0 / Re) * (u1[j + 1] - 2 * u1[j] + u1[j - 1]) / (hy * hy)
            - v1[j] * (u1[j] - u1[j - 1]) / hy
        )
        
        # Uzluksizlik (v) tenglamasi
        v2[j] = v2[j - 1] - (hy / hx) * (u2[j] - u1[j])
        
        # Temperatura (t) tenglamasi (Prandtl soni bilan)
        t2[j] = t1[j] + (hx / u1[j]) * (
            (1.0 / (Re * Pr)) * (t1[j + 1] - 2 * t1[j] + t1[j - 1]) / (hy * hy)
            - v1[j] * (t1[j] - t1[j - 1]) / hy
        )

    # 3, 5 va 7-qatlamlar uchun temperatura qiymatlarini saqlab olish
    if k == 3:
        t_layer3 = t2.copy()
    elif k == 5:
        t_layer5 = t2.copy()
    elif k == 7:
        t_layer7 = t2.copy()

    # Natijalarni chop etish
    print("u:", end=" ")
    for j in range(n + 1):
        print(f"{u2[j]:5.2f}", end=" ")
        
    print("\nv:", end=" ")
    for j in range(n + 1):
        print(f"{v2[j]:5.2f}", end=" ")
        
    print("\nt:", end=" ")
    for j in range(n + 1):
        print(f"{t2[j]:5.2f}", end=" ")

    # Keyingi qadam uchun qiymatlarni nusxalash (.copy() xotira xatosini oldini oladi)
    u1 = u2.copy()
    v1 = v2.copy()
    t1 = t2.copy()

# Grafik chizish
plt.plot(x, t_layer3, '-', label='3-qatlam')
plt.plot(x, t_layer5, '-.', label='5-qatlam')
plt.plot(x, t_layer7, '--', label='7-qatlam')

plt.title("Laminar oqimda temperatura o'zgarishi", fontsize=15)
plt.grid(True)
plt.xlabel('y (qatlam tugunlari)', fontsize=12)
plt.ylabel('Temperatura (T)', fontsize=12)
plt.legend()
plt.show()
