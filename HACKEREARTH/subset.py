# # # n = int(input())
# # m = input()
# # a = 0
# # lst = []
# # lst1 = {'a','e','i','o','u','A','E','I','O','U'}
# # for i in range(0,len(m)):
# #     for j in range(i,len(m)):
# #         lst.append(m[i:(j+1)])

# # b =set(lst)
# # print(b)
# # # for i in lst:
# # #     if i in lst1:
# # #         a = a + 1
# # for i in b:
# #     if b.issubset(lst1):
# #         a = a + 1
# #     print(a)

# # def maxSumWithoutAdjacents(a):
# lst = []
# a = [6, 13, 100, 100, 4]
# for i in range(0,len(a)-1):
#         # b = 0
#     b = a[i] + a[i+1]
#     lst.append(b)
        
# print(max(lst))

n,m = map(int,input().split())
n = list(str(n))
for i in range(m):
    n[i] = '9'
print(''.join(n))
