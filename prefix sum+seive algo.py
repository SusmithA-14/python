"""Problem
You are given an integer N.
You have to print number of prime numbers which are less than or equal to N

Input :
First line will contain an integer 'T' (number of test cases ).
For each test case there is an integer 'N'.

output :
for each test case print required answer.

constraints :
1<=T<=100000
2<=N<=10000000

Sample Input
4
2
10
4
20
Sample Output
1
4
2
8"""

n=10000001
p=[1]*n
A=[0]*n
def pseive():
    i=2
    while(i*i<=n):
        if p[i]==1:
            for j in range(i*i,n,i):
                p[j]=0
        i+=1
    p[0]=0
    p[1]=0
    for i in range(2,n):
        if p[i]==1:
            A[i]=A[i-1]+1
        else:
            A[i]=A[i-1]
pseive()
T=int(input())
for _ in range(T):
    n=int(input())
    print(A[n])   