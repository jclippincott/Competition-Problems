n = int(input())
while (n != -1):
    hrs = 0
    miles = 0
    for i in range(n):
        vals = list(map(int,input().split()))
        miles += vals[0] * (vals[1]-hrs)
        hrs = vals[1]
    print("%d miles" %miles)
    n = int(input())
