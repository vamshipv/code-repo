testcase = int(input())
while testcase:
    testcase -= 1
    N,Z = map(int,input().split())
    lst = list(map(int,input().split()))
    count = 0
    while Z>0:
        # mx = max(lst)
        lst.sort(reverse=True)
        mx = lst[0]
        # ind = lst.index(mx)
        if mx >= Z:
            print(count+1)
            break
        else:
            Z = Z - mx
            mx = mx // 2
            lst.insert(0,mx)
            count += 1
    print('Evacuate')