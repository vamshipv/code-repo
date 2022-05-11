s = 'abacabdad'
lst = list(s)
# print(lst[1:])
for i in range(len(lst)):
    # print(i)
    if lst[i] not in lst[(i)+1:]:
        print(lst[i],end= '')

