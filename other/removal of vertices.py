import math
t=int(input())
for test in range(t):
    n,k=[int(x) for x in input().split()]
    i=(k+1)*2
    i=i%n
    if i==0:
        i=n

    #print('i= ',i)
    lg=math.floor(math.log2(n))
    num=n-pow(2,lg)
    num=2*num+1
    print((num+i-1-1)%n)