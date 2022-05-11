# # # a,b = map(int,input().split())
# # # lst = []
# # # for i in range(a,b+1):

# # l = ((7,9),(3,2))
# # ll = l[0][0]|l[0][1]
# # print(ll)
# x for x in range(a,b+1)
# print(9|8)


# a = 0
# b = 100
# lst = []
# for i in range(a,b+1):
#     if i == (b):
#         break
#     else:
#         ls = i|i+1
#         lst.append(ls)
#     print(ls,end=',')
# print(len(set(lst))+len(range(a,b)))

# print(9|10)

# def printSubsets(a,b):
#     i=b
#     while(i != 0):
#         print(i,end=" ")
#         i=(i - 1) | b
#     print("0")

# print(printSubsets(7,9))

l = '1'*1024
r = '1'*1024
a = 7
b = 9
print(list(map(lambda x: x[0] & x[1], [
      (int(l[i:i+64], 2), int(r[i:i+64], 2)) for i in range(a, b,1)])))
