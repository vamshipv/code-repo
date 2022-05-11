def sieve():
    spf[1] = 1
    for i in range(2, MAXN):
        spf[i] = i

    for i in range(4, MAXN, 2):
        spf[i] = 2

    for i in range(3, mt.ceil(mt.sqrt(MAXN))):

        if (spf[i] == i):

            for j in range(i * i, MAXN, i):

                if (spf[j] == j):
                    spf[j] = i
def getFactorization(temp):
    global dic
    for it in temp:
        num = it
        ret = []
        count = 0
        if it==0:
            dic[num] = 0
         
        elif it==1:
            dic[num] = 0
     
        else:
            while (it != 1):
                if spf[it] not in ret:
                    ret.append(spf[it])
                    count+=1
                it = it // spf[it]
        dic[num] = count

def print_max(a, n, k):
    global dic
    l1=[]
    l=0
    max_upto=[0 for i in range(n)] 
    s=[] 
    s.append(0) 
    for i in range(1,n): 
        while (len(s) > 0 and dic[a[s[-1]]] <= dic[a[i]]):
            max_upto[s[-1]] = i - 1
            del s[-1] 
        s.append(i) 
    while (len(s) > 0): 
        max_upto[s[-1]] = n - 1
        del s[-1] 
    j = 0
    for i in range(n - k + 1): 
        while (j < i or max_upto[j] < i + k - 1): 
            j += 1
        l1.append(a[j]) 
    print(min(l1)) 
#    print(min(l1))
import math as mt
from collections import Counter
dic={}
ans = []
MAXN = 1000001
spf = [0 for i in range(MAXN)]
sieve()
x,n = map(int,input().split(" "))
a = list(map(int, input().split(" ")))
c = Counter(a)
temp = []
for k,v in c.items():
    temp.append(k)
getFactorization(temp)
#print(temp)
print_max(a, n, x)
