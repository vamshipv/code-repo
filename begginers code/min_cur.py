n = [i for i in range(1000,10001,1000)]
m = int(input())
for i in n:
    if i > m or i == m:
        a = i - m
        break
print(a)