n = int(input())
lst = []
while n > 0:
    nm = int(input())
    chef = 0
    morty = 0
    # draw = 0
    while nm > 0:
        c,m = map(int,input().split())
        if sum(map(int,str(c))) > sum(map(int,str(m))):
            chef = chef + 1
            # Cwins = Cwins + 1
        if sum(map(int,str(m))) > sum(map(int,str(c))):
            morty = morty + 1
            # Mwins = Mwins + 1
        nm = nm - 1
    if morty == chef:
        print(2,chef)
    if chef > morty:
        print(0,chef)
    if morty > chef:
        print(1,morty)
    
    n = n - 1


