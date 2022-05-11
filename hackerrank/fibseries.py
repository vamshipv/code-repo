# m = int(input())
# while(m>0):
#     n = int(input())
#     n1 = 1
#     n2 = 2
#     for i in  range(1,n):
#         nth = 4*n2 + n1
#         n1 = n2
#         n2 = nth
#         series = n2 + nth
#     print(series)
#     m = m -1
# # for a in lst:
# #     if a<n and a%2==0:
# #         series = series + a

# n = int(input())
# n1 = 0
# n2 = 2
# n3 = 2
# series = 0
# while (series<n):
#     nth = 4*(n2) + n1
#     n1 = n2
#     n2 = nth
#     series = n3 + nth 
# print(nth)  
# print(series)

t = int(input())
for a0 in range(t):
    n = int(input())
    a=2
    b=8
    c=0
    total=a+b
    while c<n:
        c=4*b+a
        a=b
        b=c
        total=total+c
    print(total-c)