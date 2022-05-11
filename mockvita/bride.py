n = int(input())
bride = list(map(str,input()))
groom = list(map(str,input()))
pairs = 0
while pairs < len(bride):
    # if bride[0] == groom[0]:
    # for i in range(len(bride)):
    if bride[0] == groom[0]:
        pairs = 0
        del bride[0]
        del groom[0]
    else:
        pairs +=1
        groom.insert(n,groom[0])
        del groom[0]
print(pairs)