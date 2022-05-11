n = int(input())
while n!=0:
    sn = int(input())
    s=sn%12
    if s==0:
        print(sn-11,'WS')
    elif s==1:
        print(sn+11,'WS')
    elif s==2:
        print(sn+9,'MS')
    elif s==3:
        print(sn+7,'AS')
    elif s==4:
        print(sn+5,'AS')
    elif s==5:
        print(sn+3,'MS')
    elif s==6:
        print(sn+1,'WS')
    elif s==7:
        print(sn-1,'WS')
    elif s==8:
        print(sn-3,'MS')
    elif s==9:
        print(sn-5,'AS')
    elif s==10:
        print(sn-7,'AS')
    elif s==11:
        print(sn-9,'MS')
    n=n-1