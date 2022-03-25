n=int(input())
k=int(input())
l=[0]*(n+1)
a=[]
for i in range(n+1):
    l[i]=i
i=2
while(i*i<=n):
    if l[i]==i:
        for j in range(i*i,n+1,i):
            l[j]=i
    i+=1
while(n!=1):
    a.append(l[n])
    n=n//l[n]
a.sort()
print(a[k-1])
        
