# # n = int(input())
# # o , p = map(int,input().split())
# lst = [1,2,3,4,5,6,7,8,9,10]
# p = 3
# for i in lst:
#     if (i%p == 0):
#         print(i)
#         while i>=1:
#             if (i == 1) or (i == 2):
#                 lst.append(i)
#             else:
#                 i//p           
#     else:
#         lst.append(i)
        
# print(lst)
import re
from collections import Counter
def dic(a):
    b = dict(Counter(a))
    ab = { key for key,values in b.items() if values == 1 }
    c = re.sub('{|}',"",str(ab))
    return c
    if c == None:
        return -1

a = [1,2,1,4,4]
print(dic(a))