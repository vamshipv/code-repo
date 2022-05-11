n = int(input())
while n > 0:
    m = int(input())
    lst = []
    st = list(map(int, input().split()))
    for i in range(len(st) - 1):
        a = 0
        if st[i] < st[i + 1]:
            a += abs((st[i] + 1) - st[i + 1])
            lst.append(a)
        else:
            a += abs((st[i] - 1) - st[i + 1])
            lst.append(a)
    print(sum(lst))
    n = n - 1
