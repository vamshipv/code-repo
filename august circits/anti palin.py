def pal(string):
    # chars_ = 256
    # lst = [0]*256

    # for i in range(len(string)):
    #     lst[ord(string[i])] += 1
    # oddnum = 0
    # for i in range(0,256):
    #     if lst[i] == 1:
    #         oddnum += 1
    #     if oddnum > 1:
    #         return False
        
    # return True
    lst = []
    for i in range(len(string)):
        if string[i] in lst:
            lst.remove(string[i])
        else:
            lst.append(string[i])
    if len(string)%2 == 0 and len(lst) == 0 or len(string)%2 == 1 and len(lst) == 1:
        return True
    else:
        return False

#checking palidrome from gfg

testcase = int(input())
while testcase:
    testcase -= 1
    string = input()
    if pal(string):
        print(-1)
    else:
        print(''.join(sorted(string)))

