
# print(timeZones)
# print(totalTime)
# print(leftTime)
# print(Ntime)
def main():
    for i in ntime:
        if i + leftTime >= totalTime:
            return "YES"
    return "NO"

timeZones , totalTime , leftTime = map(int , input().split())
ntime = list(map(int,input().split()))
print (main())