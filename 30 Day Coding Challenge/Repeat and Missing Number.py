#Repeat and Missing Number using XOR operations

#for Missing Number
lst = []
a = len(lst)
for i in range(a):
    a ^= i
    a ^= lst[i]
print(a)

#for repeat
#basic sum