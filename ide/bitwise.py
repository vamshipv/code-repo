a = 0
b = 100
lst = []
for i in range(a,b+1):
    if i == (b):
        break
    else:
        ls = i|i+1
        lst.append(ls)
    print(ls,end=',')
