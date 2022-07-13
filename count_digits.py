a=int(input())
p=list(map(int,input().split()))
for i in range(a):
    if p[i]<0:
        p[i]=abs(p[i])
for i in p:
    i=str(i)
    k=len(i)
    print(k,end=" ")