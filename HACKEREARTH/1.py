num,l,r = map(int,input().split())
factorial = 1  
lst = []
ls = []
for i in range(1,num + 1):  
    factorial = factorial*i  
lg = (((factorial)-1)/factorial)*10000000000000000
lg1 = int(lg)
for i in str(lg1):
  if (i == 0) or (i == '.'):
    del i
  else:
    lst.append(i)
ls = lst[:7]
lk = ''.join(ls)
lf = lst[-1]
lp = ''.join(lf)
print(lk+lp+'0')