n = int(input())
lt = []
for i in range(n):
    m = int(input())
    a = ((m)*(m-1)) + 1
    lt.append(a)

for i in lt:
    print(i)