a,b,c = list(map(int,input().split()))
times = []
times.append(list(map(int,input().split())))
times.append(list(map(int,input().split())))
times.append(list(map(int,input().split())))

park = [0 for x in range(100)]

for time in times:
    for i in range(time[0],time[1]):
        park[i] += 1

total = 0
for num in park:
    if(num > 0):    
        if(num == 3):
            total += c*num
        elif(num == 2):
            total += b*num
        else:
            total += a

print(total)
