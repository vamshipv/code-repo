n = int(input())
m = list(map(int, input().split()))
p = 1
o = (10**9 + 7)  # modulos
for i in m:
    p = (p*i) % o
print(p)
