n = int(input())
m = 0
while (n != 0):
    if(m > 0):
        print("")
    names = []
    for i in range(n):
        names.append(input())
    names = sorted(names,key=lambda name:name[:2])

    for name in names:
        print(name)
    m += 1
    n = int(input())
