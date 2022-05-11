lst = []
lst1 = []
a = [2, 1, 3, 5, 3, 2]
for i in range(len(a)):
    if a[i] not in lst:
        lst.append(a[i])
    else:
        lst1.append(i)
    
if len(lst1) == 0:
    print('-1')
        
else:
    lst1.sort()
    print(a[lst1[0]])
