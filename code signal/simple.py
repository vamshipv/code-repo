# inputArray = ["abacaba", 
#  "abacab", 
#  "abac", 
#  "xxxxxx"]
# lst = []
# for i in inputArray:
#     lst.append(len(i))
# print(lst)

# s1 = ['aabcc']
# s2 = 'adcaa'
# # count = 0
# # lst = []
# # for i in s1:
# #     if i in s2:
# #         count += 1
# #         lst.append(i)
# #         s2.remove(i)  
# # print(len(lst))
# print(list(s2))

# n =1234
# m = list(str(n))
# p = len(m)
# o = m[:int(p/2)]
# u = m[int(p/2):]
# po = 0
# op = 0
# lst1  = []
# lst  = []
# for i in o:
#     lst.append(int(i))
# for i in u:
#     lst1.append(int(i))    
# if sum(lst) == sum(lst1):
#     print(True)
# else:
#     print(False)

'''
same solution
'''

# def isLucky(n):
#     s = str(n)
#     pivot = len(s)//2
#     left, right = s[:pivot], s[pivot:]
#     return sum(map(int, left)) == sum(map(int, right))
# import numpy
a = [-1, 150, 190, 170, -1, -1, 160, 180]
lst = sorted(i for i in a if i != -1)
lst1 = numpy.argsort(lst)

print(lst1)