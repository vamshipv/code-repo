from collections import Counter
n = int(input())
lst = []
lst = [int(i) for i in input().split()]
dic = dict(Counter(lst))
dic = {key:value for key , value in dic.items() if value>0}
for key ,value in dic.items():
    print(value)
    if (n < value):
        print('0')
