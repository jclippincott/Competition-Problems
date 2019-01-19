def genMoves(s):
    moves = set()
    letter = ord(s[0])-1
    num = int(s[2])-1
    while((num > 0) and (letter > 64)):
        moves.add((chr(letter)+" "+str(num)))
        letter -= 1
        num -= 1
    letter = ord(s[0])+1
    num = int(s[2])-1
    while((num > 0) and (letter < 73)):
        moves.add((chr(letter)+" "+str(num)))
        letter += 1
        num -= 1
    letter = ord(s[0])-1
    num = int(s[2])+1
    while((num < 9) and (letter > 64)):
        moves.add((chr(letter)+" "+str(num)))
        letter -= 1
        num += 1
    letter = ord(s[0])+1
    num = int(s[2])+1
    while((num < 9) and (letter < 73)):
        moves.add((chr(letter)+" "+str(num)))
        letter += 1
        num += 1
    return moves
        
N = int(input())

black = set(["A 1","A 3","A 5","A 7","B 2","B 4","B 6","B 8","C 1","C 3","C 5","C 7","D 2","D 4","D 6","D 8","E 1","E 3","E 5","E 7","F 2","F 4","F 6","F 8","G 1","G 3","G 5","G 7","H 2","H 4","H 6","H 8"])

for i in range(N):
    spaces = input()
    s1 = spaces[:3]
    s2 = spaces[4:]
    
    if((s1 in black)==(s2 not in black)):
        print("Impossible")
    else:
        if(s1 == s2):
            print("0",s1)
        else:            
            s1moves = genMoves(s1)
            if(s2 in s1moves):
                print("1",s1,s2)
            else:
                s2moves = genMoves(s2)
                s3 = s1moves.intersection(s2moves)
                print("2",s1,s3.pop(),s2)
