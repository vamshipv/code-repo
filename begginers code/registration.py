lis = []
for i in range(1000001):
    try:
        v = int(input())
    except SyntaxError:
        v == None
        break
    lis.append(int(v))
lg = 42
if lg in lis:
    print(lis[:lis.index(42)])
else:
    print(list)