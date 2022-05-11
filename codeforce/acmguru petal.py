from itertools import cycle, islice
n, m = map(int, input().split())
val = []
for j in range(m):
    k = str(input())
    val.append(k)
x = list(islice(cycle(val), n))
# dif = abs(n - m)
# for i in range(0, dif):
#     val.append(val[i])
# print(val[-1])
print(x[-1])
