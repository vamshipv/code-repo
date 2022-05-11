
    # lst1 = lst[::2]
    # lst2 = lst[1::2]
    # A = 0
    # B = 0
    # N = 2*n
    # for i in range(0,N-1,2):
    #     if i == N-2:
    #         if A - B == 2:
    #             print(N-2)
    #             break
    #         if B - A == 2:
    #             print(N-2)
    #             break
    #     A = A + lst[i]
    #     B = B + lst[i+1]
    #     if A >= B or B >= A:
    #         print(N)
        
    
def footbal(lst,n):
    A = 0
    B = 0
    N = 2*n
    if n == 1:
        return 2
    for i in range(N):
        # if i == N-2:
        #     if A - B == 2:
        #         return N-2
        #     if B - A == 2:
        #         return N-2
        if i%2 == 0 and lst[i]==1:
            A = A + 1
        elif i%2 != 0 and lst[1] == 1:
            B = B = 1
        diff = A - B
        if(diff>(n-int((i+1)/2))) or (diff<(int(i+1)/2)-n):
             break
    return i + 1
    

testcase = int(input())
while testcase:
    testcase -= 1
    n = int(input())
    lst = list(map(int,input()))
    print(footbal(lst,n))