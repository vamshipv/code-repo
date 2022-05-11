# def fact(base):
#     return 1 if (n == 1 or n ==0 ) else n * fact(n-1)
# number , n = map(int,input().split())
# qw = (x**fact(n))%10
# print(po)

# import numpy as np
# x , n = map(int,input().split())
# a = np.math.factorial(n)
# if n >=2:
#     print(pow(x,a/2,10))
# else:
#     print(pow(x,a,10))

# def boost(n,x):
#     result = 1
#     while x > 0:
#         if x %2 == 1:
#             result *= ((n**(x-1))*n)
#         result *= ((n*n)**(x//2))
                    
#     return result
# print(boost(2,2))




# def fast_power(base, power):
#     """
#     Returns the result of a^b i.e. a**b
#     We assume that a >= 1 and b >= 0

#     Remember two things!
#      - Divide power by 2 and multiply base to itself (if the power is even)
#      - Decrement power by 1 to make it even and then follow the first step
#     """

# def fast_power(base, power):
#     result = 1
#     while power > 0:
#         if power % 2 == 0:
#             power = power // 2
#             base = base * base
#         else:
#             power = power - 1
#             result = result * base
#             power = power // 2
#             base = base * base
#     return result


# import numpy as np
# x , n = map(int,input().split())
# mod = np.math.factorial(n)%10
# po = (x**mod)%10
# print(po)
# print(24%10)

number, base = map(int,input().split())
if base == 0 or base == 1:
    power = 1
elif base == 2:
    power = 2
elif base == 3:
    power = 6
elif base == 4:
    power = 4
else:
    power = 0
print(pow(number,power)%10)