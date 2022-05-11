import re
m = int(input())
for i in range(m):
    n = str(input())

    x = re.sub('ch$', 'ches', n) and re.sub('x$', 'xes', n) and re.sub('s$', 'ses', n) and re.sub('o$', 'oes', n) and re.sub('f$', 'ves', n) and re.sub('fe$', 'ves', n) and re.sub('y$', 'ies', n)
    # if n in x:
print(x)
    # else:
    #     print(n+'s')

