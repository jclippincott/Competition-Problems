vals = list(map(int,input().split()))
cols = ["" for x in range(vals[1])]
words = []

for i in range(vals[0]):
    line = input()
    for j in range(len(line)):
        cols[j] += line[j]
    words.extend([x for x in line.split("#") if len(x) > 1])

for col in cols:
    words.extend([x for x in col.split("#") if len(x) > 1])

print(min(words))
