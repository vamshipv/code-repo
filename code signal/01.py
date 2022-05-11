a = [2,3,4,5,6,7]
lst = []
for i in a:
    b = bin(i).replace('0b','0')
    lst.append(b)
# a = ''.join(str(n) for n in lst)
# count = 0
# for i in a:
#     if i == '1':
#         count = count + 1
print(lst)