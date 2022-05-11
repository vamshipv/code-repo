days , assi = map(int,input().split())
lst = []
lst = [int(i) for i in input().split()]
tot = sum(lst)
if (tot>days):
    print(-1)
else:
    print(days-tot)