str = "ABC"  
n = len(str) 
#For holding all the formed substrings  
arr = []
   
#This loop maintains the starting character  
for i in range(0,n):  
    #This loop will add a character to start character one by one till the end is reached  
    for j in range(i,n):  
        arr.append(str[i:(j+1)])  
   
#Prints all the subset  
print("All subsets for given string are: ")  
for i in arr:  
    print(i)  