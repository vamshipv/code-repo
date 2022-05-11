

#recursion for quick sort we take last element as pivot

def partionOfArray(lst,low,high):
    print("\n")
    print("partition array     ",lst)
    
    i = low - 1
    lastIndex = lst[high]

    for j in range(low,high):
        if lst[j] < lastIndex:

            i += 1
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp
            print("for loop",lst)
    lst[i+1] , lst[high] = lst[high] , lst[i+1]
    print("part value",i + 1)
    return i + 1

def quickSort(lst, low , high):
    if low < high:
        part = partionOfArray(lst,low,high)
        # print("partion value",part)
        print("quickSort before    ",lst)
        quickSort(lst,low,part-1)
        print("Left array          ",lst)
        quickSort(lst,part+1,high)
        print("right array         ",lst)



lst = [10, 7, 8, 9, 1, 5]
print("Before Sorting", lst)
length = len(lst)
low = 0 
high = length - 1
quickSort(lst,low,high)
print("After Sorting", lst)