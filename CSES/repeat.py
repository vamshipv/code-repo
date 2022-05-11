n = input()
n = list(n)
lst = []
for i in range(0,len(n)-1):
    count = 1
    for j in range(i+1,len(n)):
        if n[i] == n[j]:
            count += 1
        else:
            break
    lst.append(count)
print(max(lst))