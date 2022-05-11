def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

flag = [0]*100001
dicc = {}
hec = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'a':10,'b':11,'c':12, 'd':13, 'e':14,'f':15}

aws=[]

for _ in range(int(input())):
    fc = 0
    l,r = map(int,input().split())

    if ((l >= 1) and (r < 10)):
        if l == 1:
            aws.append(r-l)
        else:
            aws.append(r-l+1)

    else:
     
        if l == 1:
            start = l+1
        else:
            start = l
        for i in range(start,r+1):

            if i < 10:
                fc += 1
             
            else:
              
                if(flag[i]==0):
                    tot = 0
                    n1 = hex(i)
                    n1 = str(n1)
                    n1 = n1[2:]
                    le = len(n1)
                    for j in range(le):
                        val = n1[j]
                        tot = tot + hec[val]


                    flag[i] = tot
                    cu1 = flag[i]
                    if cu1 != 1:
                        so = gcd(i,cu1)
                        if so > 1:
                            fc+=1

                else:
                    cu1 = flag[i]
                    if cu1 != 1:
                        so = gcd(i,cu1)
                        if so > 1:
                            fc+=1

        aws.append(fc)

for i in aws:
    print(i)
