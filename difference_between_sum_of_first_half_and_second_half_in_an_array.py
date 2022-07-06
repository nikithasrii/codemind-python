n=int(input())
l=list(map(int,input().split()))
sum_first=0
sum_last=0
for i in range(0,n):
    if(i<n//2):
        sum_first+=l[i];
    else:
        sum_last+=l[i];
p=sum_first-sum_last
if p<0:
    p=p*-1
print(p)