for i in range(int(input())):
    line = input().split()
    stu = int((line[1].split("/"))[0])
    bd = int((line[2].split("/"))[0])

    if ((stu > 2009) or (bd > 1990)):
        print("%s eligible" %line[0])
    elif(int(line[3]) > 40):
        print("%s ineligible" %line[0])
    else:
        print("%s coach petitions" %line[0])
