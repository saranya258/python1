saran,sara=input().split()
sabar=abs(len(sara)-len(saran))
for g in range(len(saran)):
	    if(len(sara)==1 and sara[g] in saran):
	        break
	    if (saran[g]!=sara[g]):
	        sabar=sabar+1
print(sabar)

