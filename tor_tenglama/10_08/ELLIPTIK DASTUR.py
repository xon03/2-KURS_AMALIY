import numpy as np
import matplotlib.pyplot as plt
# parametrlar
N = 20
M = 20

u01 = 100
u02 = 450
u03 = 200
u04 = 600
u00 = 100

omega = 1.25

Hx = 1.0 / N
Hy = 1.0 / M

# massivlar
u = np.zeros((N+1, M+1))
u0 = np.zeros((N+1, M+1))

X = np.zeros(N+1)
Y = np.zeros(M+1)

# chegaraviy shartlar
for i in range(1, N):
    u[i,0] = u01
    u[i,M] = u03

for j in range(1, M):
    u[0,j] = u04
    u[N,j] = u02

# boshlang'ich yaqinlashish
for i in range(1, N):
    for j in range(1, M):
        u[i,j] = u00

# koordinata setkasi
for i in range(N+1):
    X[i] = i * Hx

for j in range(M+1):
    Y[j] = j * Hy

# koeffitsiyentlar
Alfa = 0.5 / (1.0 + (Hx/Hy)**2)
Betta = 0.5 / (1.0 + (Hy/Hx)**2)

N_iter = 0

while True:

    # oldingi iteratsiya
    u0[:,:] = u[:,:]

    # yangi qiymatlar
    for j in range(1, M):
        for i in range(1, N):
            u[i,j] = ((u[i+1,j] + u[i-1,j]) * Alfa +
                      (u[i,j+1] + u[i,j-1]) * Betta) * omega \
                      + u0[i,j] * (1 - omega)

    # kriteriy
    Delta = 0

    for j in range(1, M):
        for i in range(1, N):
            Delta += abs(u[i,j] - u0[i,j])

    Delta = Delta / ((M-1)*(N-1))

    N_iter += 1
    print(" Iteratsiya =", N_iter, "Delta =", Delta)

    if Delta < 1e-3:
        break

print("Omega =", omega, " Iteratsiya =", N_iter)

# natijalarni faylga yozish
with open("result.txt", "w") as f:
    for j in range(M+1):
        for i in range(N+1):
            f.write(f"{X[i]:5.2f} {Y[j]:7.4f} {u[i,j]:7.4f}\n")

with open("matrix.txt", "w") as f1:
    for j in range(M+1):
        for i in range(N+1):
            f1.write(f"{u[i,j]:7.4f} ")
        f1.write("\n")
#plt.imshow(u, cmap='viridis') # rangli sxema
#plt.colorbar() # 
#plt.title("Matrisa vizualizatsiyasi")
#plt.show()
x = np.linspace(1, 21, 21)
y = np.linspace(1, 21, 21)
X, Y = np.meshgrid(x, y)
contour = plt.contourf(X/40, Y/40, u, cmap='viridis') # 
plt.clabel(contour, inline=True, fontsize=10) # 
plt.colorbar(contour) # 
plt.title("Konturli grafik")
plt.show()