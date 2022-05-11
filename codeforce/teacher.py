import itertools
stu ,bod = map(int , input().split())
lst = {}
lt = []
lst = [int(i) for i in input().split()]
se = list(itertools.combinations(lst, stu))
print(se)
for j in se:
    an = list(j)
    gf = max(an) - min(an)
    lt.append(gf)
f = min(lt)
print(f)