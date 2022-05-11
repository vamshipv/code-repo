
# Who is taller Code for CodeChef
# num = int(input())
# for i in range(num):
#     A , B = map(int , input().split())
#     if A > B:
#         print('A')
#     else:
#         print('B')


#  Chef and chapters
# num = int(input())
# for i in range(num):
#     X,Y,Z = map(int , input().split())
#     print(X*Y*Z)

# chef and Bird Farm
num = int(input())
for i in range(num):
    X,Y,Z = map(int , input().split())
    if(Z%X==0 and Z%Y==0):
        print("any")
    elif(Z%Y==0):
        print("duck")
    elif(Z%X==0):
        print("chicken")
    else:
        print("none")