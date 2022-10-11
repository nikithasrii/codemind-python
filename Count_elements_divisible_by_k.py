N,K=map(int,input().split())
a=list(map(int,input().split()))
c=0
for k in a:
    if k%K==0:
        c=c+1
print(c)