def stand(code_length,code):

    if code_length == 13:
        lst1 = list(str(code))
        l1 = 13 - len(lst1)
        for i in range(l1):
            lst1.insert(0,str(0))
        return ''.join(lst1)

    if code_length == 14:
        sumlst = []
        ab = list(str(code))
        lst = [int(a) for a in ab]
        length1 = 14 - len(lst)
        for i in range(len(lst)):
            if i%2 == 0:
                sumlst.append(lst[i]*3)
            else:
                sumlst.append(lst[i])
        # print(sumlst)
        if sum(sumlst)%10 == 0:
            # l2 = 14 - len(lst)
            for i in range(length1-1):
                lst.insert(0,str(0))
            lst.insert(14,0)
            finallst = [str(a) for a in lst]
            return ''.join(finallst)
        else:
            a = str(sum(lst))
            # l3 = 14 - len(lst)
            for i in range(length1-1):
                lst.insert(0,0)
            lst.insert(14,a[-1])
            finallst = [str(a) for a in lst]
            return ''.join(finallst)
    
code_length = 14
code = 93247658
print(stand(code_length,code))