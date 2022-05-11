# n = int(input())
# m = int(input())
# lst = []
# while(m>0):
#     l,b = map(int, input().split())
#     if l*b == n*n:
#         lst.append("ACCEPTED")
#     elif l<n or b<n:
#         lst.append("UPLOAD ANOTHER")
#     else:
#         lst.append("CROP IT")
#     m = m-1
# for i in lst:
#     print(i)
# lst = []
# for i in range(12):
#     a, b = list(map(int, input().split()))
#     su = a+b
#     if su == 0:
#         break
#     lst.append(su)
# for i in lst:
#     print(i)
# lst =[]
# while True:
#     a,b = map(int,input().split())
#     if (a !=0 and b!=0):
#         c = a+b
#         lst.append(c)
#     else:
#         break
# for i in lst:
#     print(i)    
# lst =[]
# for i in range(12):
#     a,b = map(int,input().split())
#     if (a !=0 and b!=0):
#         s = a+b
#         lst.append(s)
#     else:
#         exit
# print(lst)




# import sys
# input = sys.stdin.read()
# data = list(map(int, input.split()))
# si = len(data)
# first,second = list((data[0:si:2]),list(data[1:si:2]))
# print(first)
# print(second)

# import sys
# input = sys.stdin.read()
# data = list(map(int, input.split()))
# si = len(data)
# first,second = list(data[0:si:2]),list(data[1:si:2])
# ans = []
# for i in range(si//2):
#     ans.append(first[i]+second[i])
# for i in ans:
#     print(i)

data = [2,3]
si = len(data)
first,second = list(data[0:si:2]),list(data[1:si:2])
print(first)