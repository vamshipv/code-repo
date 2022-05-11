newlst = []
lst =[]
m = int(input())
while m > 0:
    a = str(input())
    lst.append(a)
    m = m -1
newlst = list(dict.fromkeys(lst))
print(len(newlst))
