n,k,m = map(int,input().split())
val = list(map(int,input().split()))
lst = []
for i in range(k):
    lst.append(i%m)
print(lst)

lst1 = [a*b for a,b in zip(val,lst)]
# for i in range(len(val)-1):
#     op = 0
#     if val[i] > val[i+1]:
#         for j in lst:
#             op = op + i*j
#     lst1.append(op)
print(lst1)
print(max(lst1))