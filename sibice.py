vals = list(map(int,input().split()))
diag = ((vals[1]**2)+(vals[2]**2))**(1/2)
for i in range(vals[0]):
    match = int(input())
    if((match > vals[1]) and (match > vals[2]) and (match > diag)):
        print("NE")
    else:
        print("DA")
