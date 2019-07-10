sara=int(input())
p=[]
saran=0
for g in range (0,sara+1):
	saran=abs((2**g)-sara)
	p.append(saran)
sd=min(p)
print(sd)

