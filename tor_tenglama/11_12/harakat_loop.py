import numpy as np
import matplotlib.pyplot as plt
import math

#u = [[0.0 for j in range(10)] for i in range(10)]
u0=[0.0 for j in range(11)]
u1=[0.0 for j in range(11)]
v0=[0.0 for j in range(11)]
v1=[0.0 for j in range(11)]
t0=[0.0 for j in range(11)]
t1=[0.0 for j in range(11)]
t2=[0.0 for j in range(11)]
t3=[0.0 for j in range(11)]
x=[0.0 for j in range(11)]

# boshlang'ich va chegaraviy shart
n=11
hx=0.0005
hy=0.00055
Re=20000

u1[n-1]=1
u0[n-1]=1
for j in range(1, n-1):
    u0[j] = 1

for j in range(n):
    print(f"{u0[j]:5.2f}", end=" ")
print("")
input("davom ettirish uchun enterni bosing")

for k in range(20):
    for j in range(1, n-1):
        # 0 ga bo'lish xatosini oldini olish
        u_val = 1e-6 if u0[j] == 0 else u0[j]
        # (1/Re*(...)) qismida tushib qolgan ko'paytirish belgisi qo'yildi
        u1[j]=u0[j]+hx/u_val*(1/Re*(u0[j+1]-2*u0[j]+u0[j-1])/hy/hy-v0[j]*(u0[j]-u0[j-1])/hy)
        
    v1[0]=0.0
    for j in range(1, n):
        v1[j]=v1[j-1]-hy/hx*(u1[j]-u0[j])
        
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
            
    # Keyingi qadamda xatolik yig'ilmasligi uchun nusxa olish kerak
    u0=u1.copy()
    v0=v1.copy()
    print("")

for i in range(11):
    x[i]=i * hy # y masofasini to'g'ri ko'rsatish uchun

plt.plot(t0,x,'-',t1,x,'-.',t2,x,'--',t3,x,'.')
plt.title("Chegaraviy qatlamda tezlik o'zgarishi", fontsize=15)
plt.grid(True)
plt.xlabel("u tezlik", fontsize=12)
plt.ylabel('y masofa', fontsize=12)
plt.legend(('5-qatlam', '9-qatlam', '13-qatlam','17-qatlam'))
plt.show()