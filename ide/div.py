n = int(input())
nlst = []
lst = []
while(n>0):
    o , p = map(int,input().split())
    ans = [nlst]
    for i in range(1,o+1):
        if (i%p == 0):
            po = i//p
            if po == 1:
                lst.append(po)
            else:
                while po>=1:
                    if (po == 1) :
                        lst.append(po)
                        break
                    else:
                        if ( po%p == 0):
                           po = po//p
                        else:
                            lst.append(po)
                            break      
        else:
            lst.append(i)
    ans.append(lst)      
    n = n -1
print(lst)
