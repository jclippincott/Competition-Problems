n = int(input())

for i in range(n):
    line = input().split()
    add = int(line[1])
    mins = int(line[3])
    hrs = int(line[2])
    mins = (mins + add) if (line[0] == "F") else (mins-add)
    if(mins < 0):
        amt = mins//60
        mins += (60*abs(amt))
        hrs -= abs(amt)
        hrs = (hrs+24) if (hrs < 0) else hrs
    if(mins >= 60):
        amt = mins//60
        mins -= (60*abs(amt))
        hrs += abs(amt)
        hrs = (hrs-24) if (hrs > 23) else hrs
    print("%d %d" %(hrs,mins))
