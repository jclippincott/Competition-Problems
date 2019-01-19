input()
line = input()
while line != "":
    maxMoney = 0
    prizes = []
    currentCase = [int(x) for x in line.split()]
    for i in range(currentCase[0]):
        prize = input().split()[1:]
        stickerNums = [int(x) for x in prize[:-1]]
        value = int(prize[-1])
        prizes.append([stickerNums,value])
    stickers = [int(x) for x in input().split()]

    for check in prizes:
        nums = check[0]
        if(stickers[x-1] > 0 for x in nums):
            minimum = min([stickers[x-1] for x in nums])
            for x in nums:
                stickers[x-1] -= minimum
            maxMoney += (minimum * check[1])
    print(maxMoney)
    try:    
        line = input()
    except EOFError:
        break
