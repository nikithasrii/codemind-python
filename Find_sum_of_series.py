n=int(input())
s=0
i=1
while i in range(1,n+1):
    s=s+1/i
    i+=1
print("%0.2f"%s)