#Triplet
saran=int(input())
pavi=list(map(int,input().split()))
c=0
for i in range(0,saran-2):
	for j in range(1,saran-1):
		for k in range(2,saran):
			if(pavi[i]<pavi[j] and pavi[j]<pavi[k]):
					c+=1
print(c)

