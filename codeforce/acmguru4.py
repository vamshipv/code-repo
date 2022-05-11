n = int(input())
lst = []
for i in range(n+1):
    if i%2 != 0:
        lst.append(i)
print(len(lst))
print(lst)