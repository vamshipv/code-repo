arrayOfElements = [64,25,12,22,11]

length = len(arrayOfElements)
#insertion sort
for i in range(length):
    minIndex = i

    for j in range(i+1,length):
        if arrayOfElements[minIndex] > arrayOfElements[j]:
            minIndex = j
    print(arrayOfElements)
    print("\n")
    #swap numbers
    temp = arrayOfElements[minIndex]
    arrayOfElements[minIndex] = arrayOfElements[i]
    arrayOfElements[i] = temp
    print(arrayOfElements)

# print(arrayOfElements)
    