a=input()
l=list(a)
(e,o)=('','')
for i in range(len(l)):
	if i%2==0:
		e+=l[i]
	else :
		o+=l[i]
print(e,o)
