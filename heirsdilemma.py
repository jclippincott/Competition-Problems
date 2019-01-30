def isvalid(strval):
    nums = {}
    for j in range(6):
        if(int(strval[j]) in nums):
            return 0
        else:
            nums[int(strval[j])] = True
        if(i%int(strval[j]) != 0):
            return 0
    if(not invalid):
        return 1

vals = list(map(int,input().split()))
total = 0
for i in range(vals[0],vals[1]):
    strval = str(i)
    invalid = False
    if ("0" not in strval):
        total += isvalid(strval)
print(total)
