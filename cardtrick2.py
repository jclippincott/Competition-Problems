cards = { 1 : "1", 2 : "2 1", 3 : "3 1 2", 4 : "2 1 4 3", 5 : "3 1 4 5 2", 6 : "4 1 6 3 2 5", 7 : "5 1 3 4 2 6 7", 8 : "3 1 7 5 2 6 8 4", 9 : "7 1 8 6 2 9 4 5 3", 10 : "9 1 8 5 2 4 7 6 3 10", 11 : "5 1 6 4 2 10 11 7 3 8 9", 12 : "7 1 4 9 2 11 10 8 3 6 5 12", 13 : "4 1 13 11 2 10 6 7 3 5 12 9 8"}

for i in range(int(input())):
    print(cards.get(int(input())))


##This program was used to compute solutions for n = 2 to n = 11.
##After 11, the computation time was too long so I did the computation by hand.

##def shiftleft(cards,n):
##    for i in range(n):
##        temp = cards[0]
##        cards = [cards[i+1] for i in range(len(cards)-1)]
##        cards.append(temp)
##    return cards
##
##def getresult(cards,i):
##    result = []
##    for j in range(1,i+1):
##        cards = shiftleft(cards,j)
##        result.append(cards.pop(0))
##    return result
##
##
##def main():
##    for i in range(2,13):
##        cards = [str(ii+1) for ii in range(i)]
##        for elem in itertools.permutations(cards):
##            elem = list(elem)
##            if(elem[1] == "1"):
##                if(len(elem) > 4):
##                    if(len(elem) > 8):
##                        if(elem[8] == "3"):
##                            if(getresult(elem,i) == cards):
##                                print(elem)
##                    elif(elem[4] == "2"):
##                        if(getresult(elem,i) == cards):
##                            print(elem)
##                elif(getresult(elem,i) == cards):
##                    print(elem)


