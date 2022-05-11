import math
a,b,h,m = map(int,input().split())
angle = int(abs(11 /2 * m - 30 * h))
c = ((a**2) + (b**2))  - ((math.cos(angle))*(2*a*b))
print(math.sqrt(c))
print(angle)