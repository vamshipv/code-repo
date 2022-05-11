a,b,c,d = map(int,input().split())
ta = 0
aok = 0
while True:
    ta = c-b
    c = ta

    if c <=0:
        print("Yes")
        break
    aok = a - d
    a = aok
    if a <=0:
        print("No")
        break
       

    

