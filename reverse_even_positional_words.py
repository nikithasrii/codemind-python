n=input()
s=n.split()
l=len(s)
a=0
for i in range(l):
    if i==0 or i%2==0:
        a=s[i]
        print(a[::-1],end=" ")
    else:
        print(s[i],end=" ")
        