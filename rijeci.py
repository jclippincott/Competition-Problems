a = 1
b = 0

for i in range(int(input())):
    temp = b
    b += a
    a = temp

print("%d %d" %(a,b))
