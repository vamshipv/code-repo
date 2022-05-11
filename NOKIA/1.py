from collections import Counter
n = int(input())
x = list(map(int,input().split()))
y = sum([item for item,count in Counter(x).items() if count%2 ==0])
print(y)
