n = int(input())
lsteven = []
lstodd = []
paris = 0
# while n > 0:
mo = list(map(int,input().split()))
for m in range(len(mo)):
    if len(str(mo[m])) == 2:
        if (m)%2 == 0:
            lsteven.append(mo[m])
        else:
            lstodd.append(mo[m])
    else:
        a = max(map (int, str (mo[m]))) *11
        b = min(map (int, str (mo[m]))) *7
        if len(str(a+b)) == 2:
            if (m)%2 == 0:
                lsteven.append(a+b)
            else:
                lstodd.append(a+b)

        else:
            if (m)%2 == 0:
                lsteven.append(int(str(a+b)[len(str(a+b))-2:]))
            else:
                lstodd.append(int(str(a+b)[len(str(a+b))-2:]))

lsteven = [int(i/10) for i in lsteven]
lstodd = [int(i/10) for i in lstodd]
even = set(lsteven)
odd = set(lstodd)
for i in set(lsteven):
    if lsteven.count(i) >= 2:
        paris = paris + (lsteven.count(i)-1)
        even.discard(i)
for i in set(lstodd):
    if lstodd.count(i) >= 2:
        paris = paris + (lstodd.count(i)-1)
        odd.discard(i)

# lsteven = [int(i/10) for i in lsteven]
# lstodd = []
# for i in set(even):
#     if lsteven.count(i) >= 2:
#         paris = paris + (lsteven.count(i)-1)
# for i in set(odd):
#     if lstodd.count(i) >= 2:
#         paris = paris + (lstodd.count(i)-1)

print(paris)
