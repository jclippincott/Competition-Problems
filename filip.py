nums = [x[::-1] for x in input().split()]

if(int(nums[0]) > int(nums[1])):
    print(nums[0])
else:
    print(nums[1])
