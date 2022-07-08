n=int(input())
l=list(map(int,input().split()))
sum=0
for i in range(0,n):
    if l[i]%2!=0:
        sum=sum+l[i]
print(sum)