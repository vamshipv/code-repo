n = int(input())
m = list(map(str,input()))
if len(m) > n:
    a = m[:n]
    print(''.join(a)+'...')
else:
    for i in m:
        print(i,end='')