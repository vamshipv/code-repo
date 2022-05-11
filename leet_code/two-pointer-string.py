n = ["h","e","l","l","o"]
left =  0 
right = len(n)-1
while left < right:
    n[left],n[right] = n[right],n[left]
    left = left + 1
    right = right - 1
print(n)    