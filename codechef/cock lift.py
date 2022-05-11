a = int(input())

an = []
for q in range(a):
    n, q = map(int, input().split())
    lst = []
    for i in range(q):
        lst.append(list(map(int, input().split())))
    lvl = lst[0][0]
    for i in range(q):
        if i == 0:
            lvl = lvl + abs(lst[i][0]-lst[i][1])
        else:
            lvl += abs(lst[i-1][1]-lst[i][0])+abs(lst[i][0]-lst[i][1])
    an.append(lvl)
for i in an:
    print(i)
