from collections import Counter
cou = 0
n = int(input())
for i in range(n):
    lst = list(map(int,input().split()))
    y = [item for item ,count in Counter(lst).items() if item == 1 and count >=2 ]
    if y[0] == 1:
        cou = cou +1
print(cou)