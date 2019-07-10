import math
saran,pavi=map(int,input().split())
Sri=[]
loga=list(map(int,input().split()))
for i in range(0,pavi):
	l,h=map(int,input().split())
Sri.append([l,h])
for i in Sri:
	kk=i[0]-1
        ll=i[1]-1
        print(math.gcd(loga[kk],loga[ll]))

