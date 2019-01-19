line = input()
while line != "":
    nums = [int(x) for x in line.split()]
    mosquitos = nums[0]
    pupae = nums[1]
    larvae = nums[2]
    E = nums[3]
    R = nums[4]
    S = nums[5]
    N = nums[6]
    eggs = 0

    for i in range(N):
        eggs = mosquitos * E
        mosquitos = pupae//S
        pupae = larvae//R
        larvae = eggs

    print(mosquitos)
        
    try:
        line = input()
    except EOFError:
        break
