testcases = int(input())
while testcases > 0 :
    totalGroup = 0
    String = input()
    for i in range(len(String)):
        if String[i] == '1' and  i == 0:
            totalGroup += 1
        elif String[i] == '1' and String[i-1] == '0':
            totalGroup += 1
    testcases -= 1
    print(totalGroup)        



