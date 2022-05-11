n = int(input())
for i in range(100,999):
    for j in range(100,999):
        a = i*j
        if (str(a) == str(a)[::-1]):
            if a < n:
                
                print(a)
        