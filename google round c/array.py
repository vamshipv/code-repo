n = int(input())
lst = []
while n > 0:
    m , b = map(int,input().split())
    op = list(map(int,input().split()))
    for i in op:
        if op[i] > op[i+1]:
            lst.append(op[i])
            if lst[-1] == 1:
                break
    n = n -1
for i in lst:
    print('case #1:'+ str (i))
