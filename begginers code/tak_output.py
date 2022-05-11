n = int(input())
lst = []
for i in range(n):
    m = input()
    lst.append(m)

print("AC x",lst.count("AC"))
print("WA x",lst.count("WA"))
print("TLE x",lst.count("TLE"))
print("RE x",lst.count("RE"))