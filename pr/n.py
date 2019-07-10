pt=int(input())
ot=[]
for ht in range(0,pt):
 pant=input()
 ot.append(pant)
ve=[]
for ht in zip(*ot):
 if(ht.count(ht[0])==len(ht)):
  ve.append(ht[0])
 else:
  break
print(''.join(ve))
