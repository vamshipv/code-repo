test = int(input())
while test != 0:
    test -= 1
    n = int(input())
    lst = list(map(int,input().split()))
    count = 0
    for i in range(len(lst) - 1):
        if lst[i] > lst[i+1]:
            count += 1
    if count == 0:
        print(str(1) + " " + str(1))
    else:
        if count == len(lst) - 1:
            print(str(count+ 1) + " " + str(count+1))
        else:
            print(str(1) + " " + str(count + 1))
