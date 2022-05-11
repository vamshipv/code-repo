n = int(input("Enter the range"))

prime = [True for i in range(n+1)]

p = 2

while(p*p <=n):
    if prime[p] == True:
        for i in range(p*p,n+1,p):
            prime[i] = False
    p = p + 1

lst = []

for p in range(2,n+1):
    if prime[p]:
        lst.append(p)

print("The prime numbers are",lst)