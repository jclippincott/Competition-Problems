import sys

line = "."
while line != "":
    line = sys.stdin.readline().strip()
    if(line != ""):
        line = line.split()
        t1 = [int(x) for x in line[3].split(":")]
        t2 = [int(x) for x in line[4].split(":")]

        if(t1[1] > t2[1]):
            t2[1] += 60
            t2[0] -= 1
        print("%s %s %s %d hours %d minutes" %(line[0],line[1],line[2],(t2[0]-t1[0]),(t2[1]-t1[1])))
