t = int(input())

for i in range(t):
    input()
    input()
    g = max([int(x) for x in input().split()])
    m = max([int(x) for x in input().split()])

    if(g > m):
        print("Godzilla")
    elif(g < m):
        print("MechaGodzilla")
    else:
        print("Godzilla")
