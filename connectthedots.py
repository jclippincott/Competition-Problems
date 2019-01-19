def drawLine(r1,c1,r2,c2,game):
    lineChar = ""
    if(r1 == r2):
        if(c1 > c2):
            temp = c1
            c1 = c2
            c2 = temp
        for i in range(c1+1,c2):
            pos = game[r1][i]
            if(pos == "."):
                game[r1] = game[r1][:i]+"-"+game[r1][i+1:]
            elif(pos == "|"):
                game[r1] = game[r1][:i]+"+"+game[r1][i+1:]
    else:
        if(r1 > r2):
            temp = r1
            r1 = r2
            r2 = temp
        for i in range(r1+1,r2):
            pos = game[i][c1]
            if(pos == "."):
                game[i] = game[i][:c1]+"|"+game[i][c1+1:]
            elif(pos == "-"):
                game[i] = game[i][:c1]+"+"+game[i][c1+1:]
    return game
import sys

game = []
pieces = []    
places = {}

line = "."
while line != "":
    line = sys.stdin.readline()
    if(line.strip() != ""):
        game.append(line.strip())
    else:
        i = 0
        for row in game:
            j = 0
            for col in row:
                if(col != "."):
                    if(col.islower()):
                        pieces.append(col.upper())
                        places[col.upper()] = [i,j]
                    elif(col.isupper()):
                        pieces.append(col.lower())
                        places[col.lower()] = [i,j]
                    else:
                        pieces.append(col)
                        places[col] = [i,j]
                j += 1
            i += 1
        pieces = sorted(pieces)
        for i in range(len(pieces)-1):
            p1 = places.get(pieces[i])
            p2 = places.get(pieces[i+1])
            game = drawLine(p1[0],p1[1],p2[0],p2[1],game)
        for row in game:
            print(row)
        print()
        game = []
        pieces = []

