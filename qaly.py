qaly = 0
for i in range(int(input())):
    line = input().split()
    qaly += float(line[0])*float(line[1])
print(qaly)
