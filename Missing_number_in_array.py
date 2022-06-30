t=int(input())
for i in range(t):
    j=int(input())
    l=list(map(int,input().split()))
    for i in range(1,j+1):
        if i not in l:
            print(i)