import math 
U=1
L=70*(10**-3)
C=10**-7
R=100
f=2500
w=2*math.pi*f
I=U/((R**2)+(w*L-1/(w*C))**2)**0.5
UR=I*R
UL=I*w*L
UC=I*1/(w*C)
F=math.degrees(math.atan((w*L-1/(w*C))/R))

print(f"tok kuchi={I}")
print(f"UR={UR}")
print(f"UL={UL}")
print(f"UC={UC}")
print(f"F={F}")
