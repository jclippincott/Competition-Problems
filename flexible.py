w, p = list(map(int,input().split()))
lengths = [0 for x in range(w+1)]
partitions = list(map(int,input().split()))

for i in range(len(partitions)):
    lengths[partitions[i]] += 1
    lengths[w-partitions[i]] += 1
    for j in range(len(partitions)):
        if(i != j):
            width = abs(partitions[j]-partitions[i])
            lengths[width] += 1
lengths[w] += 1

for i in range(1,len(lengths)):
    if(lengths[i] > 0):
        print(i,"",end="")
print("")
