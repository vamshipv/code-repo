# x,y = map(int,input().split())
# lst = list(map(int,input().split()))
# i = 0
# while i < y:
#     p,q,r = map(int,input().split())
#     sum = 0
#     if p == 1:
#         lst[q] = r
#     else:
#         for j in range(q,r+1):
#             sum = sum + lst[j]
#         print(sum)
#     i = i + 1

# n = list(map(int,input().split()))
# lst = []
# lst1 = []
# for i in n:
#     if i in n[i:]:
#         break
#     else:
#         lst.append(i)

# print(lst)
n = [1,2,3,4,1,2,5,7,8]
lst = []
for i in n:
    if n.count(i) == 1:
        lst.append(i)
print(lst)