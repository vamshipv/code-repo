from collections import Counter 
final = []
testcase = int(input())
while(testcase>0):
    main = str(input())
    count = Counter(main)
    instring = ''
    for letter in main:
        if letter in count:
            instring += str(letter)+str(count[letter])
            count.pop(letter)
    final.append(instring)
    testcase = testcase-1

for each in final:
    print(each)
