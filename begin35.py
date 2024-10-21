import math
v1=int(input("v1 ni kiriting"))
v2=int(input("v2 ni kiriting"))
t1=int(input("t1 ni kiriting"))
t2=int(input("t2 ni kiriting"))

s1=(v1+v2)*t1
s2=math.fabs(v1-v2)*t2

print(s1,s2)