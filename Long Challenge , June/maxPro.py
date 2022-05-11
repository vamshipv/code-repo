# testcase = int(input())
# while testcase > 0:
#     d,x,y,z = map(int,input().split())
#     cOne = x * 7
#     remDays = 7 - d
#     cTwo = (y*d) + (z*remDays)
#     result = max(cOne,cTwo)
#     print(result)
#     testcase = testcase - 1

# testcase = int(input())
# while testcase > 0:
#     g,c = map(int,input().split())
#     result = (c*c)/(2*g)
#     print(round(result))
#     testcase = testcase - 1

testcase = int(input())
while testcase > 0:
    n,k = map(int,input().split())
    lst = list(map(int,input().split()))
    p = 0
    pin = 2**p
    while sum(lst) == 0:
        for i in lst:
            pass


    testcase = testcase - 1