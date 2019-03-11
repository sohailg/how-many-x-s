import math
t=int(input())
for i in range(t):
    n,x=input().split()
    n=int(n)
    k=math.ceil(n/2)
    x=int(x)
    s=k*x
    s=int(s)
    print(s)