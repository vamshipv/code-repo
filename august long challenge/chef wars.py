def wars(h,p):
    if p >= h//2:
        return 1
    if h>p:
        return 0
for _ in range(int(input())):
    h,p = map(int,input().split())
    print(wars(h,p))