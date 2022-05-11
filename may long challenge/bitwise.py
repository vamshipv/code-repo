n = int(input())
lst1 = []
for i in range(n):
    q,w,e,r = map(int,input().split())
    lst = {}
    for i in range(e,r):
        y = (q&i)*(w&i)
        lst[i] = y
    keymax = max(lst,key= lambda key:lst[key])
    lst1.append(keymax)
    n = n-1
for j in lst1:
    print(j)

