# def sieve_of_primes(n):
# 	sev=[True for x in range(n+1)]
# 	sev[1]=False
# 	p=2
# 	while (p*p<=n):
# 		if sev[p] == True:
# 			for i in range(p*p,n+1,p):
# 				sev[i] = False
# 		p += 1
# 	return sev

# def chess(lst,a,k):
#     # sev = sieve_of_primes(k+1)
#     # arr = []
#     if k%2 != 0 and k%3 != 0:
#         return -1
#     lst.sort()
#     dic = {}
#     for i in range(len(lst)):
#         p = lst[i]
#         if lst[i] < k:
#             count = 0
#             while lst[i]<=k:
#                 lst[i] = lst[i] + lst[i]
#                 count += 1
#                 if lst[i] > k and lst[i]%2 == 0:
#                     lst[i] = int((lst[i]/2)//2)
#                     count = 0
#                     while lst[i]<=k:   
#                         lst[i] = lst[i] + lst[i]
#                         count += 1
#                 if lst[i] > k and lst[i]%3 == 0:
#                     lst[i] = lst[i]//2
#                     count = 0
#                     while lst[i]<=k:                        
#                         lst[i] = lst[i] + lst[i]
#                         count += 1
#             if lst[i]%2 == 0 and lst[i] > 2:
#                 dic.update({count:lst[i]//2})
#             elif lst[i]>3:
#                 dic.update({count:lst[i]//3})
#             else:
#                 dic.update({count:lst[i]})
#             # arr.append(count)
#         elif lst[i] > k:
#             break
#     for i in sorted(dic.keys()):
#         return dic[i]
#     return - 1
# test = int(input())
# while test > 0:
#     a,k = map(int,input().split())
#     lst = list(map(int,input().split()))
#     print(chess(lst,a,k))
#     test = test - 1


def chess(lst,c,k):
    # if k%2 != 0 and k %3 != 0:
    #     return -1
    # jai = []
    # for i in lst:
    #     if i == k:
    #         return i
    #     if i+i == k:
    #         return i
    #     if i < k and k%i == 0:
    #         jai.append(k//i)
    # if len(jai) == 0:
    #     return -1
    # return min(jai)
    jai = {}
    mi = []
    for i in lst:
        if k%i == 0:
            jai.update({k//i:i})
            mi.append(k//i)
    if len(mi) == 0:
        return -1
    mi.sort()
    return jai[mi[0]]


test = int(input())
while test > 0:
    c,k = map(int,input().split())
    lst = list(map(int,input().split()))
    print(chess(lst,c,k))
    test -= 1