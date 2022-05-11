
m = int(input())
lst = []
while (m>0):
    n = int(input())
    
    if (n == 1) or (n==2) :
        lst.append('NO')
    elif (n%2 == 1):
        for i in range(2,n//2):
            if (n%i) != 0:
                lst.append('NO')
    else:
        lst.append("YES")
    m = m -1
for i in lst:
    print(i)
