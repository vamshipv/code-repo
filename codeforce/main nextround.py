n, m = map(int, input().split())
count = 0

x = list(map(int, input().split()))

for i in x:
    if x[i] >= m:
        count += 1
print(count)
