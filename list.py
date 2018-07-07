n,k = int(raw_input()),int(raw_input())
b=[]
d=0
for i in range(n):
	x=int(raw_input())
	b.insert(i,x)
for j in range(k):
	d=d+b[j]
print (d)
