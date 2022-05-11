# lst = list(int,input().split())
# count = 0
# pro = 1
# mx = 0
# # lst.sort()
# for i in lst:
#     if  i == 0:
#         break
#     else:
#         pro = pro * i
#         count += 1
#         mx = max(mx,pro)
#         if pro:
            
    
# if pro < 0 and count%2 != 0:
#     print(count - 1)

lst = list(map(int,input().split()))
m = int(input())
k = int(input())
count = 0
for i in range(0,len(lst),m):
    if lst[i] == lst[i-1]:
        count += 1
if count >= k:
    print(True)
else:
    print(False)