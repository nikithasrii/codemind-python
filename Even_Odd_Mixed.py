n=int(input())
c=0
v=0
l=0
b=0
while n:
    r=n%10
    n=n//10
    l+=1
    if r%2==0:
        c+=1
    if r%2!=0:
        v+=1
    else:
        b+=1
if(l==c):
    print("Even")
elif (l==v):
    print("Odd")
else:
    print("Mixed")
        