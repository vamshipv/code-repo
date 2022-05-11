#Sort an array of 0’s 1’s 2’s without using extra space or sorting algo

n = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
c1 = 0 
c2 = 0
c3 = 0

for i in n:
    if i == 0:
        c1 += 1
    elif i == 1:
        c2 += 1
    else:
        c3 += 1

i = 0

while(c1>0):
    n[i] = 0
    i += 1
    c1 -= 1
while(c2>0):
    n[i] = 1
    i += 1
    c2 -= 1
while(c3>0):
    n[i] = 2
    i += 1
    c3 -= 1

print(n)


# Time complexity is o(n) and space complexity is o(1)
# This can also be solved used Dutch National Flag Algorithm OR 3-way Partitioning
