n = int(input())
n1 = 0
n2 = 1
lst = []
lst1 = []
for i in range(n):
    nth = n1 + n2
    n1 = nth
    lst.append(nth)
# print(lst)
for j in lst:
    if j%3 == 0:
        lst1.append(j)
print(len(lst1) + 1)