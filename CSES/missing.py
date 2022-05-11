n = int(input())
lst = list(map(int,input().split()))
# lst.sort()
# for i in range():
#     if lst[i+1] - lst[i] != 1:
#         print(lst[i]+1)
#         break
for i in range(1,n+1):
    if i not in lst:
        print(i)
        break