n = int(input())
for i in range(n):
    m = int(input())
    op = list(map(int,input().split()))
    # if len(op) ==  0:
    #     print(0)
    fast = op[0]  
    count = 1
    for i in range(1,len(op)):
        if op[i] <= fast:
            count += 1
            fast = op[i]
    print(count)



# for fast processing we take the 
# first value ast fast to compare with the list
