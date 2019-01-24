nums = input().split()

if(int(nums[0]) > int(nums[1])):
    for i in range(len(nums[0])-1,-1,-1):
        print(nums[0][i],end="")
    print("")
else:
    for i in range(len(nums[1])-1,-1,-1):
        print(nums[1][i],end="")
    print("")
    
