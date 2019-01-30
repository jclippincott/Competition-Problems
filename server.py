t = int((input().split())[1])
times = [int(x) for x in input().split()]

total = 0
i = 0
n = 0
found = False
for i in range(len(times)):
    total += times[i]
    if((total > t) and (not found)):
        n = i
        found = True

if(not found):
    n = len(times)

print(n)
