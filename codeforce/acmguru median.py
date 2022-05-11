n = list(map(int,input().split()))
m = list(map(int,input().split()))
b = list(map(int,input().split()))
a = n.sort()
s = m.sort()
d = b.sort()
q = [n[1],m[1],b[1]]
q.sort()
print(q[1])
