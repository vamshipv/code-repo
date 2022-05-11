def DisappearanceOfIntegers (A, Q, M, t, N):
    out=[]
    en=N//2
    on=N-en

    for x in range(Q):
        time=t[x]%(2*N)
        pos=M[x]

        if time==0:
            ans=pos
        elif time==N:
            ans=-1
        elif time<N:
            if time<=on:
                if pos<=time:
                    ans=2*pos
                else:
                    ans=2*time+pos-time
            else:
                ans=(time-on)*2+2*pos
        elif time>N:
            if time-N<=on:
                ans=2*pos-1
                if time-N<pos:
                    ans=-1
            else:
                temp=2*(time-N-on)+1
                if pos<=temp:
                    ans=pos
                else:
                    ans=temp+2*(pos-temp)

        if ans>0 and ans<=N:
            print(A[ans-1])
        else:
            print(-1)

    return out

    # Write your code here
    
N = int(input())
A = list(map(int, input().split(" ")))
Q = int(input())
t=[]
M=[]
for i in range(Q):
    tmp = list(map(int, input().split(" ")))
    t.append(tmp[0])
    M.append(tmp[1])
    
out_ = DisappearanceOfIntegers(A, Q, M, t, N)