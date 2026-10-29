import matplotlib.pyplot as plt
import math
p0=1000
p1=850
H=15
g=9.8
v=10
for k in range(4):
    L=v*(p1*H/(g*(p0-p1)))**(1/2)
    n=int(L/0.1)
    h = [0.0 for j in range(n)]
    l = [0.0 for j in range(n)]
    for i in range(n):
        l[i] = i*0.1
    for i in range(n):
        h[i] = g*(p0-p1)/(p1*v**2)*l[i]**2
    if k==1:
        h1 = h
        l1 = l
        v=20
    if k==2:
        h2 = h
        l2 = l
        v=30
    if k==3:
        h3 = h
        l3 = l
print(f"L={L}, {n} ta qadamda bajarildi.")
plt.plot(l1,h1, '-',l2,h2,'.-',l3,h3,'--')
plt.title("Suv osti kemasi", fontsize=15)
plt.grid(True)
plt.xlabel("l", fontsize=12)
plt.ylabel('h', fontsize=12)
plt.legend(("v=10",'v=20','v=30'))
plt.show()
