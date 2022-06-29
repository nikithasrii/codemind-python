p,r,t=list(map(int,input().split()))
compound_intrest=p*pow(1+r/100,t)
print("%0.2f" %compound_intrest)
