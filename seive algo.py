"""Number of primes in given range using sieve eratosthenes"""
def seive(n):
    a=[1 for i in range(n+1)]
    p=2
    while(p*p<=n):
        if(a[p]==1):
            for i in range(p*p,n+1,p):
                a[i]=0
        p+=1
    a[0]=False
    a[1]=False
    for p in range(2,n+1):
        if a[p]:
            print(p)
n=int(input())
seive(n)
