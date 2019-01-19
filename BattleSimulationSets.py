try:
    moves = input()
except EOFError:
    exit(0)

mechMoves = ""
moveReplace = {"R":"S", "B":"K", "L":"H"}
RBL = set(["R","B","L"])               
i = 0

while i < len(moves):
    if(i+2 < len(moves)):
        moveset = set(moves[i:i+3])
        if(moveset == RBL):
            mechMoves += "C"
            i += 3
        elif moves[i] in RBL:
            mechMoves += moveReplace.get(moves[i])
            i += 1
    else:
        mechMoves += moveReplace.get(moves[i])
        i += 1

print(mechMoves)
