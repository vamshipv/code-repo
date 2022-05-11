# def disap (A, Q, M, t, N):
#     outside=[]
#     op=N//2
#     mode=N-op

#     for x in range(Q):
#         time=t[x]%(2*N)
#         lop=M[x]

#         if time==0:
#             ans=lop
#         elif time==N:
#             ans=-1
#         elif time<N:
#             if time<=mode:
#                 if lop<=time:
#                     ans=2*lop
#                 else:
#                     ans=2*time+lop-time
#             else:
#                 ans=(time-mode)*2+2*lop
#         elif time>N:
#             if time-N<=mode:
#                 ans=2*lop-1
#                 if time-N<lop:
#                     ans=-1
#             else:
#                 temp=2*(time-N-mode)+1
#                 if lop<=temp:
#                     ans=lop
#                 else:
#                     ans=temp+2*(lop-temp)

#         if ans>0 and ans<=N:
#             print(A[ans-1])
#         else:
#             print(-1)

#     return outside


    
# N = int(input())
# A = list(map(int, input().split(" ")))
# Q = int(input())
# t=[]
# M=[]
# for i in range(Q):
#     tap = list(map(int, input().split(" ")))
#     t.append(tap[0])
#     M.append(tap[1])
    
# out_ = disap(A, Q, M, t, N)
a = 111
b = 10111
print(a&b)