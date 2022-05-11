def stars(lst_of_sg):
    final_lst = []
    i=0
    while i <(N-2):
        flg=0
        if lst_of_sg[0][i] == '#':
            final_lst.append("#")
            i+=1
            continue
        if lst_of_sg[0][i] == '.' and lst_of_sg[0][i+1] == '*' and lst_of_sg[0][i+2] == '.':
            if lst_of_sg[1][i]=='*' and lst_of_sg[1][i+1]=='*' and lst_of_sg[1][i+2]=='*':
                # if lst_of_sg[2][i]=='*' and lst_of_sg[2][i+1]=='.' and lst_of_sg[2][i+2]=='*':
                final_lst.append("A")
                flg=1
        if lst_of_sg[0][i]=='*' and lst_of_sg[0][i+1]=='*' and lst_of_sg[0][i+2]=='*':
            if lst_of_sg[1][i]=='*' and lst_of_sg[1][i+1]=='*' and lst_of_sg[1][i+2]=='*':
                # if lst_of_sg[2][i]=='*' and lst_of_sg[2][i+1]=='*' and lst_of_sg[2][i+2]=='*':
                final_lst.append("E")
                flg=1
        if lst_of_sg[0][i]=='*' and lst_of_sg[0][i+1]=='*' and lst_of_sg[0][i+2]=='*':
            if lst_of_sg[1][i]=='.' and lst_of_sg[1][i+1]=='*' and lst_of_sg[1][i+2]=='.':
                # if lst_of_sg[2][i]=='*' and lst_of_sg[2][i+1]=='*' and lst_of_sg[2][i+2]=='*':
                final_lst.append("I")
                flg=1
        if lst_of_sg[0][i]=='*' and lst_of_sg[0][i+1]=='*' and lst_of_sg[0][i+2]=='*':
            if lst_of_sg[1][i]=='*' and lst_of_sg[1][i+1]=='.' and lst_of_sg[1][i+2]=='*':
                # if lst_of_sg[2][i]=='*' and lst_of_sg[2][i+1]=='*' and lst_of_sg[2][i+2]=='*':
                final_lst.append("O")
                flg=1
        if lst_of_sg[0][i]=='*' and lst_of_sg[0][i+1]=='.' and lst_of_sg[0][i+2]=='*':
            if lst_of_sg[1][i]=='*' and lst_of_sg[1][i+1]=='.' and lst_of_sg[1][i+2]=='*':
                # if lst_of_sg[2][i]=='*' and lst_of_sg[2][i+1]=='*' and lst_of_sg[2][i+2]=='*':
                final_lst.append("U")
                flg=1
        if flg:
            i+=3
        else:
            i+=1

    return ''.join(final_lst)

N = int(input())
lst_of_sg = []
for i in range(3):
    lst_of_sg.append(list(input().split()))
print(stars(lst_of_sg))