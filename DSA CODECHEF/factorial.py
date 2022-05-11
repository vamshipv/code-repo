n = int(input())
while n > 0:
    m = int(input())
    dem = 5
    ans = 0
    while dem <= m:
        ans += int(m/dem)
        dem *= 5
    print(int(ans))
    n = n - 1
