s=input()
c=0
for i in s:
    if(i=='z'):
        c=c+1
d=len(s)-c
if(2*c==d):
    print("Yes")
else:
    print("No")