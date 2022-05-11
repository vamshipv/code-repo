

def smallkmp(word,match):
    for i in list(match):
        word.remove(i)
    
    word.append(match)
    word.sort()

    begin = match[0]
    nex = begin

    for i in list(match):
        if i != begin:
            nex = i
            break
    
    if nex < begin:
        try:
            op = word.index(begin)
            word.remove(match)
            word.insert(op,match)
        except:
            pass
    else:
        return ''.join(word)

    return ''.join(word)

testcase = int(input())
while testcase > 0:
    testcase -= 1
    word = list(input())
    match = input()
    print(smallkmp(word,match))


# test= int(input())
# while(test):
#     test-= 1
#     num, kak = list(map(int, input().split()))
#     op = input().split()
#     lst= []
#     j = 0
#     res= 1
    
    
#     while(j < num):
#         i = op[j]
#         if(i in lst):
#             res+= 1
#             lst= []
#         else:
#             lst.append(i)
#             j += 1
#     print(res)