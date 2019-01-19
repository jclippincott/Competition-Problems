n = int(input())
while (n != 0):
    am = []
    pm = []
    am12 = []
    pm12 = []
    for i in range(n):
        line = input().split()
        if(":" in line[0][:2]):
            line[0] = "0"+line[0]
        if(line[1] == "a.m."):
            if(line[0][:2] == "12"):
                am12.append(line[0])
            else:
                am.append(line[0])
        else:
            if(line[0][:2] == "12"):
                pm12.append(line[0])
            else:
                pm.append(line[0])
    am = sorted(am)
    pm = sorted(pm)
    am12 = sorted(am12)
    pm12 = sorted(pm12)
    
    for time in am12:
        print(time,"a.m.")
    for time in am:
        if(time[0] == "0"):
            print(time[1:],"a.m.")
        else:
            print(time,"a.m.")
    for time in pm12:
        print(time,"p.m.")
    for time in pm:
        if(time[0] == "0"):
            print(time[1:],"p.m.")
        else:
            print(time,"p.m.")
    print()
    n = int(input())
