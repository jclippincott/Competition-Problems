from sys import stdin

case = 1
for line in stdin:
    linelist = line.strip().split()
    for i in range(len(linelist)):
        linelist[i] = int(linelist[i])
    nums = set(linelist[1:])
    maximum = max(nums)
    minimum = min(nums)
    numrange = maximum-minimum
    print("Case %d: %d %d %d" %(case,minimum,maximum,numrange))
    case += 1
