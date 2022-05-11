# def rec(n):
#     if n==0:
#         return 
#     else:
#         print(n)
#         rec(n-1)

# print(rec(5))

# def rec(n):
#     if n <= 0 :
#         return
#     else:
#         rec(n-1)
#         print(n)

# print(rec(5))

#Josephus problem from start index 0

def jose(n,k):
    if n == 0:
        return n
    return (jose(n-1,k)+k-1)%n+1

print(jose(7,3))