import math
test = int(input())
while test > 0:
    test -= 1
    chef,rick = map(int,input().split())
    # print(game(chef,rick))
# def game(chef,rick):
    ch = 0
    ri = 1
    chef = math.ceil(chef/9)
    # print(chef)
    rick = math.ceil(rick/9)
    # print(rick)
    diff = chef - rick
    if diff == 0:
        print(1,chef)
    elif chef > rick:
        print(1,rick)
    else:
        print(0,chef)

