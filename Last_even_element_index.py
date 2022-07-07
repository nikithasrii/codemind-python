n=int(input())
arr=list(map(int,input().split()))
c=[]
for i in range(0,n):
    if arr[i]%2==0:
        c.append(i)
print(c[-1])