lst =[3,2,10,12,1,5,4,6]

length = len(lst)
for i in range(1,length):
    arrayMin = lst[i]
    j = i - 1
    while j >= 0 and arrayMin < lst[j]:
        lst[j+1] = lst[j]
        j = j - 1
        print(lst)
    lst[j+1] = arrayMin
    print(lst)
    print("\n")        







        # arr[j + 1] = arr[j] 
        #         j -= 1
        # arr[j + 1] = key 