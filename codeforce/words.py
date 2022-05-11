m = int(input())
while(m > 0):
    str = input()
    if (len(str) > 10):
        es = len(str[1:-1])
        print('{}{}{}'.format(str[0], es, str[-1]))
    else:
        print(str)
    m = m-1
