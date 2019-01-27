import math

n = int(input())
rings = list(map(int,input().split()))
r1 = rings[0]
for i in range(1,n):
    r2 = rings[i]
    div = math.gcd(r1,r2)
    print("%d/%d" %((r1/div),(r2/div)))
