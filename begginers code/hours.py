h1 , m1 , h2 , m2 , k = map(int, input().split())
a1 = abs(h2-h1)*60
a2 = abs(m1-m2)
a  = a1 - a2
if a == k:
    print(0)
else:
    b = a - k
    print(b)