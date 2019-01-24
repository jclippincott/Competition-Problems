l = int(input())
d = int(input())
x = int(input())

n = 10001
m = 0

for i in range(l,d+1):
    total = sum(map(int, str(i)))
    if(total == x):
        if(i > m):
            m = i
        if(i < n):
            n = i
print(n)
print(m)
