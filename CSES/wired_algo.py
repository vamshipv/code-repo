# n = int(input())
# lst = []
# while n != 1:
#     if n%2 == 0:
#         lst.append(n//2)
#     else:
#         lst.append((n*3)+1)
# print(' '.join(lst))

def wa(n):
    lst = []
    while n == 1:
        lst.append(str(n))
        return (''.join(lst))
    lst.insert(0,str(n))
    while n != 1:
        if n%2 == 0:
            n = n//2
            lst.append(str(n))
        else:
            n = (n*3)+1
            lst.append(str(n))
    return (' '.join(lst))

n = int(input())
print(wa(n))