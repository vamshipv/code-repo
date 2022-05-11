# n = int(input())
# count = 0
# for i in range(20,101):
#     pod = 1
#     a = list(map(int,str(i)))
#     if 1 not in a:
#         for j in a:
#             pod = pod * j
#         if pod == n:
#             count += 1
# if n < 9:
#     print(count + 1)
# else:   
#     print(count)
# n = int(input())
# count = 0
# for i in range(2,n//2+1):
#     if n%i == 0:
#         # if 1 not in list(map(int,str(i))):
#         count += 1
# print(count)

# n = int(input())
# count = 0
def fact_(n):
    prd = 1
    while (n!=0):
        rem = n%10
        if rem == 1:
            return 0
        else:
            prd *= rem
            n = int(n/10)
    return int(prd)

n = int(input())
count = 0
for i in range(2,10000):
    if fact_(i) == n:
        count +=1
print(count)
