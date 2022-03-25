"""prefix sum algo for """
def prefix(p,a,n):
    p[0]=a[0]
    for i in range(1,n):
        p[i]=p[i-1]+a[i]
a=[2,5,7,11,13,1,4,44,65]
n=len(a)
p=[0 for i in range(n+1)]
prefix(p,a,n)
for i in range(n):
        print(p[i])
