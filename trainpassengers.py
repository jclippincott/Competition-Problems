line = [int(x) for x in input().split()]
on = 0

for i in range(line[1]):
    currStop = [int(x) for x in input().split()]
    leave = currStop[0]
    board = currStop[1]
    wait = currStop[2]

    if ((i == 0) and (currStop[0] > 0)):
        print("impossible")
        exit(0)
        
    on -= currStop[0]
    if(on < 0):
        print("impossible")
        exit(0)
        
    on += currStop[1]
    if(on > line[0]):
        print("impossible")
        exit(0)
                
    if((i == line[1]-1) and (on != 0)):
        print("impossible")
        exit(0)
        
    if((on < line[0]) and (currStop[2] > 0)):
        print("impossible")
        exit(0)

        
print("possible")
