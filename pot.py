total = 0
for i in range(int(input())):
    line = input()
    total += int(line[:-1])**int(line[-1])
print(total)
