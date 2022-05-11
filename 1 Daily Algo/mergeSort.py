import random
#merge sort using recursion
def mergerSort(lst):
    if len(lst) > 1:
        n = len(lst)//2
        Larray = lst[:n]
        Rarray = lst[n:]

        mergerSort(Larray)
        # print("L1",Larray)
        # print(lst)
        mergerSort(Rarray)
        # print("R2",Rarray)
        # print("lst",lst)
        # print("\n")
        i = 0
        j = 0
        k = 0
        # [2,3,4,5,6]
        # [2,3] [4] [5,6]
        # [2] [3] [4] [5] [6]
        # L   R   L   L   R
        # print("1",lst)
        while (i < len(Larray) and j < len(Rarray)):
            if Larray[i] < Rarray[j]:
                lst[k] = Larray[i]
                i += 1
            else:
                lst[k] = Rarray[j]
                j += 1
            k += 1
            # print("1st while loop",lst)
        # print("\n")
        while i < len(Larray):
            lst[k] = Larray[i]
            i += 1
            k += 1
            # print("2nd while loop",lst)
        while j < len(Rarray):
            lst[k] = Rarray[j]
            j += 1
            k += 1
            # print("3rd while loop",lst)
        # print(lst)
lst = []
for i in range(20):
    lst.append(random.randrange(1,100))
print("Before",lst)
# lst = [8,5,5,6,4,9,2,7,3,10]
print(mergerSort(lst))
print("after",lst)



    