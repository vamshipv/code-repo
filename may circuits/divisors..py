# n = int(input())
# lst = []
# lst1  = []
# while(n>0):
#     o , p = map(int,input().split())
#     for i in range(1,o+1):
#         if (i%p == 0):
#             s = i//p
#             lst.append(s)
#         else:
#             lst.append(i)
#     n = n-1

# lst1.append(lst)
    
    

# print(lst1)
# # for i in lst1:
# #     print(sum(i))

def oop(qw,j):
        if qw<j:
                return (qw*(qw+1))//2
        else:
                s1=(qw*(qw+1))//2
                t=qw//j
                s2=((t*(t+1))//2)*j
                return(s1-s2+oop(t,j))
sas = []
for _ in range(int(input())):
    n,j=map(int,input().split())
    sas.append(oop(n,j))
for i in sas:
    print(i)