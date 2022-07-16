n=input()
l1=len(n)
s=""
for i in n:
    if i not in s:
        s+=i
l2=len(s)
if l1==l2:
    print(True)
else:
    print(False)
#jasmitha