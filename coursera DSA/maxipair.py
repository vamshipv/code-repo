# # n = int(input())
# # m1 = list(map(int,input().split()))
# # m1.sort()
# # max_ = 0
# # m = len(m1)
# # for i in range(0,m-1):
# #     for j in range(1,m):
# #         max_ = max(max_,m1[i]*m1[j])
# # print(max_)
# # take max value and less than max and pair it 

# # we reduced from n^2 to n in time complexity
# while True:
#     import random
#     n = random.randint(100,200)
#     print(n)
#     lst = []
#     for i in range(n):
#         lst.append(random.randint(100,200))
#     print(lst)
#     max_ = -1
#     for i in range(0,len(lst)):
#         if max_ == -1 or lst[i] > lst[max_]:
#             max_= i
#     max1_ = -1

#     for j in range(0,len(lst)):
#         if (max_ != j) and (max1_ == -1 or lst[max1_] <= lst[j]):
#             max1_ = j
#     print(lst[max1_]*lst[max_])

#     omax_ = 0
#     for i in range(0,n):
#         for j in range(i+1,n):
#             omax_ = max(omax_,lst[i]*lst[j])
#     print(omax_)
#     if (omax_ == (lst[max_]*lst[max1_])):
#         print("Yes")
#     else:
#         print("No")
#         break

# n = int(input())
# lst = list(map(int,input().split()))
# max_ = -1
# for i in range(0,len(lst)):
#     if max_ == -1 or lst[i] > lst[max_]:
#         max_= i
# max1_ = -1

# for j in range(0,len(lst)):
#     if (max_ != j) and (max1_ == -1 or lst[max1_] <= lst[j]):
#         max1_ = j
# print(lst[max_]*lst[max1_])

a = 467889
lst = list(str(a))
# for i in range(2):
ab = [int(a) for a in lst]
print(sum(ab))
