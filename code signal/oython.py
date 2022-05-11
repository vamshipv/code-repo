lst = [24,85,0]
lst.reverse()
lst1 = []
for i in lst:
    a = format(i,'04b')
    lst1.append(a)

# a = ''.join(str(n) for n in lst1)
# print(a)
print(lst1)