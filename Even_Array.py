a=int(input())
b=list(map(int,input().split()))
c=0
for i in range(a):
    if b[i]%2==0:
        c=c+1
if a==c:
    print("True")
else:
    print("False")