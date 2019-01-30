input()
line = [int(x) for x in input().split()]
tot = 0
for x in line:
    if(x < 0):
        tot += 1
print(tot)
