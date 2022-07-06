n=int(input())
l=list(map(int,input().split()))
s=int(input())
p=0
for i in range(0,n):
    if i==s:
        break
    else:
        p=p+l[i]
print(p)        