n = int(input())
while n > 0:
    m = int(input())
    h1=1
    t1=2
    while m > 0:
        i,o,p = map(int,input().split())
        if (o%2 == 0 or i == p):
            print(int(o/2))
        else:
            print(int((o/2)+1))
        m = m -1
    n = n - 1 
