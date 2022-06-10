N=int(input())
for i in range(1,N+1):
    p=N
    for j in range(1,N+1):
        print(p,end=" ")
        p=p-1
    print()