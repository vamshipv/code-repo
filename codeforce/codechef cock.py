#from itertools import chain
n = int(input())
lift = 0
diff = []
for i in range(n):
    x , y = map(int,input().split(' '))
    for j in range(y):
        k , l = map(int,input().split(' '))
        diff1 = diff.append(k,j)
        print(diff)

