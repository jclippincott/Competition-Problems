moves = input()
vals = {"A":1,"B":1,"C":2}

pos = 1
for char in moves:
    if (char == "A"):
        if(pos == 1):
            pos = 2
        elif(pos == 2):
            pos = 1
    elif (char == "B"):
        if(pos == 2):
            pos = 3
        elif(pos == 3):
            pos = 2
    else:
        if(pos == 1):
            pos = 3
        elif(pos == 3):
            pos = 1

print(pos)
