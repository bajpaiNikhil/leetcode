n=[1,4,3,2]
n.sort()
m=[]
print(n)
a=0
while(a<len(n)-1):
    m.append(min(n[a],n[a+1]))
    a+=2
print(sum(m))