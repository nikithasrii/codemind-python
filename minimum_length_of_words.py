n=input()
m=n.split()
p=[]
for i in m:
    c=0
    for j in i:
        c+=1
    p.append(c)
print(min(p))