r,s,kk = list(map(int,input().split()))
if((r == 3) and (s == 3)):
    print(1)
    print("+-+")
    print("|*|")
    print("+-+")
else:
    grid = []
    for i in range(r):
        grid.append(input())
    x = 0
    y = 0
    inside = kk-2
    flies = 0
    for i in range(1,r-inside):
        for j in range(1,s-inside):
            numflies = 0
            for k in range(i,i+inside):
                numflies+=grid[k][j:j+inside].count("*")
                if(numflies > flies):
                    x = j-1
                    y = i-1
                    flies = numflies
    print(flies)
    for i in range(r):
        if((i == y) or (i == y+kk-1)):
            grid[i] = grid[i][:x]+"+"+("-"*inside)+"+"+grid[i][x+kk:]
        elif((i > y) and (i < y+kk-1)):
            grid[i] = grid[i][:x]+"|"+grid[i][x+1:x+kk-1]+"|"+grid[i][x+kk:]
        print(grid[i])
