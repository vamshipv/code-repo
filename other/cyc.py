# Write your code here
from collections import deque
a=int(input())
ans=[]
for i in range(a):
    n,m,c=input().split()
   n=int(n)
    m=int(m)
    num=bin(n)
    num = num[2:]
    n = [0]*(16-len(num))
    n = ''.join(map(str,n))
    num=deque(n+num)
    l=len(num)
    if c=='L':
      num.rotate(-m)
      num=''.join(map(str,num))
      ans.append(int(num,2))

    else:
      num.rotate(m)
      num=''.join(map(str,num))
      ans.append(int(num,2))

for i in ans:
    print(i)
