import math
m=float(input("m="))
M=0.5
g=9.8
l=1
a=math.pi/3
v=math.sqrt(2*(m+M)*g*l*(1-math.cos(a))/m)
print(v)