def fact(n):
    su=0
    if(n>0):
        for i in range(1,n+1):
            if n%i==0:
                su=su+i
        return su
l=list(map(int,input().split(',')))
a=[]
c=0
for i in l:
    if fact(i) in l:
        a.append(i)
    else:
        c=c+1
if len(l)==c:
    print(-1)
else:
    a.sort()
    print(*a)