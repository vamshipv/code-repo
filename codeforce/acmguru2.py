n = int(input())
n1 = 1
n2 = 1
for i in range(n):
    series = n1 + n2
    n1 = n2
    n2 = series
print(series-1)