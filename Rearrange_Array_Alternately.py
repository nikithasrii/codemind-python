t=int(input())
k=[]
def jj(n):
    while len(l)!=0:
        k.append(max(l))
        k.append(min(l))
        for i in k:
            if i in l:
                l.remove(i)
    if(j%2!=0):
        k.pop()
    return k
while t!=0:
    j=int(input())
    l=list(map(int,input().split()))
    print(*(jj(j)))
    t=t-1
    del k[0:j]