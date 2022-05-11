mes = '123'
import itertools
a = {chr(Y):Y-64 for Y in range(65,91)}
se = list(itertools.combinations(a))

print(se)