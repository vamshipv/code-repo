def gcd(a,b):
    if b == 0:
        return a
    a1 = a%b
    return gcd(b,a1)

print(gcd(357,234))