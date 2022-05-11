n =int(input())
lst = []
for i in range(n):
    m = int(input())
    lst.append(m)
lst.sort()
maxi = 0
for i in range(n):
    a = lst[i]*(n-i)
    # print(a)
    maxi = max(a,maxi)
print(maxi)