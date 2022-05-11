n = int(input())
# for i in range(n):
#     m = int(input())
#     k = k*m
op = 1
p = list(map(int,input().split()))
p.sort()
for i in p:
    op = op*i

    if op > 10**18:
        print(-1)
        exit(0)

print(op)