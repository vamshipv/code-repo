testcase = int(input())
while testcase > 0:
    mainlst = [1,2,3,4,5,6,7]
    n = int(input())
    count = 0
    lst = list(map(int, input()))
    for i in lst:
        if i in mainlst:
            count = count + 1
            mainlst.remove(i)
            # print(mainlst)
        else:
            count = count + 1
        if len(mainlst) == 0:
            print(count)
    testcase - testcase - 1