sabar,saran=map(str,input().split())
yas=0
if len(sabar)>len(saran):
	sabar,saran=saran,sabar
p=0
while p<len(sabar):
	  yas+=(ord(saran[p])-ord(sabar[p]))
	  p+=1
for p in range(p,len(saran)):
	  yas+=ord(saran[p])-ord('a')+1
print(yas)

