line = input().split()
lights = {}

for i in range(int(line[0])):
    light = [int(x) for x in input().split()]
    lights[light[0]] = light[1:]

d = 0
t = 0
L = int(line[1])
while d < L:
    d += 1
    t += 1
    if(d in lights):
        rg = lights[d]
        if((t%sum(rg)) < rg[0]):
            t += rg[0] - t%sum(rg)
print(t)
