osum=0
n = int(input())
x = list(map(int,input().split()))

for i in range(n):
    if x[i]%2==1:
        osum+=x[i]

print(osum)