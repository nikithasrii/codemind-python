n=int(input())
l=list(map(int,input().split()))
p=0
for i in range(0,n):
    if l[i]%2==0:
        break
    else:
        p+=l[i]
print(p)        