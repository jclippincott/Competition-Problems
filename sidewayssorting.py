line = input().split()
r = int(line[0])
c = int(line[1])
ii = 0

while ((r > 0) and (c > 0)):
    if(ii > 0):
        print("")

    lines = []
    for i in range(r):
        lines.append(input())
    words = ["" for x in range(c)]
    for i in range(r):
        for j in range(c):
            words[j] += lines[i][j]
    words = sorted(words,key= lambda word:word.lower())

    for i in range(r):
        for j in range(c):
            print(words[j][i],end="")
        print("")
        
    line = input().split()
    r = int(line[0])
    c = int(line[1])
    ii += 1
