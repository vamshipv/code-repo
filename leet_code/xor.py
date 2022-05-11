def xorOperation(n, start):
    if n <= 0:
        return
    for i in range(n):
        return (start +2*i)^(xorOperation(n-1,start))
print(xorOperation(5,0))