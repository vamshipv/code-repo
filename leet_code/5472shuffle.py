s = input()
dic = {}
ind = list(map(int,input()))
for i in range(len(ind)):
    dic.update({ind[i]:s[i]})
for i in sorted(dic):
    print(''.join(dic))
# print(dic)