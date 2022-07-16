n=input()
s=n.split()
l=len(s)
for i in range(l):
    a=s[l-i-1]
    print(a[::-1],end=" ")