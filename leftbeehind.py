line = input()
while (line != "0 0"):
    j = [int(x) for x in line.split()]
    if(sum(j) == 13):
        print("Never speak again.")
    elif(j[0] > j[1]):
        print("To the convention.")
    elif(j[0] < j[1]):
        print("Left beehind.")
    else:
        print("Undecided.")
    line = input()
