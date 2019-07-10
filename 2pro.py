numer,sar=input().strip().split(" ")
sar=int(sar)
i=0;
while i<len(numer)-1 and sar:
		if(numer[i]>numer[i+1]):
			sar-=1
			numer=numer[:i]+numer[i+1:]
			if(i!=0):
				i-=1
		else:
			i+=1
saran=numer[:len(numer)-sar]
print(saran)

