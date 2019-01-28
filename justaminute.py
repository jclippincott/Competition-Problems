slm = 0.0
total = 0
for i in range(int(input())):
    m,s = list(map(float,input().split()))
    slm += s
    total += m
slm /= total*60
if(slm <= (1 + 1e-7)):
    print("measurement error")
else:
    print("%0.9f" %slm)
