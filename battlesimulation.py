moves = input()

mechMoves = ""
i = 0
while i < len(moves):
    if(i+2 < len(moves)):
        if(moves[i] == "R"):
            if((moves[i+1] == "B") and (moves[i+2] == "L")):
                mechMoves += "C"
                i += 3
            elif((moves[i+1] == "L") and (moves[i+2] == "B")):
                mechMoves += "C"
                i += 3
            else:
                mechMoves += "S"
                i += 1
        elif(moves[i] == "B"):
            if((moves[i+1] == "L") and (moves[i+2] == "R")):
                mechMoves += "C"
                i += 3
            elif((moves[i+1] == "R") and (moves[i+2] == "L")):
                mechMoves += "C"
                i += 3
            else:
                mechMoves += "K"
                i += 1
        elif(moves[i] == "L"):
            if((moves[i+1] == "B") and (moves[i+2] == "R")):
                mechMoves += "C"
                i += 3
            elif((moves[i+1] == "R") and (moves[i+2] == "B")):
                mechMoves += "C"
                i += 3
            else:
                mechMoves += "H"
                i += 1
    else:
        if(moves[i] == "R"):
            mechMoves += "S"
        elif(moves[i] == "B"):
            mechMoves += "K"
        elif(moves[i] == "L"):
            mechMoves += "H"
        i += 1

print(mechMoves)
