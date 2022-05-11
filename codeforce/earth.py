days, assi = map(int, input().split())
lst = []
while(assi > 1):
    a = list(map(int, input().split()))
    assi -= 1
    tot = sum(a)
if (days > tot):
    print(days-tot)
elif (days == tot):
    print(days-tot)
else:
    print('-1')
