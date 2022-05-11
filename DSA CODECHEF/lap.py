n = int(input())
for i in range(n):
    m = input()
    op = int(len(m)//2)
    lst = list(m[:op])
    lst1 = list(m[-op:])
    lst.sort()
    lst1.sort()
    if (lst == lst1):
        print("YES")
    else:
        print("NO")    
