def sieve_of_primes(n):
# n = 20
	sev=[True for x in range(n+1)]
	sev[1]=False
	p=2
	while (p*p<=n):
		if sev[p] == True:
			for i in range(p*p,n+1,p):
				sev[i] = False
		p += 1
	return sev

hours,part=input().split()
hours = int(hours)
part = int(part)
div=hours//part
sev = sieve_of_primes(500)
# print(sev)
count=0
for x in range(1,div+1):
	flg=0
	for y in range(part):
		if not sev[x+y*div]:
			flg=1
			break
	if flg==0:
		count+=1
print(count)

