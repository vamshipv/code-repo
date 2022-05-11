chars = 256
def pali(val):
# val = input()
    count = [0]*chars
    for i in range(0,len(val)):
        count[ord(val[i])] += 1

    od = 0
    for i in range(0,chars):
        if(count[i]&1):
            od += 1
        if od>1:
            return False
    
    return True

if(pali(str(input()))):
    print("YES")
else:
    print("NO")