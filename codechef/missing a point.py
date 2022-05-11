np = int(input())
while np > 0:
    n = int(input())
    set1 = set()
    set2 = set()
    for i in range(((4*n)-1)):
        x,y = map(int,input().split())
        if x in set1:
            set1.remove(x)
        else:
            set1.add(x)
        if y in set2:
            set2.remove(y)
        else:
            set2.add(y)
    print(str(set1)[1:-1],str(set2)[1:-1])
    np = np - 1

