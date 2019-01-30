from sys import stdin

for line in stdin:
    n = [int(x) for x in line.strip().split()]
    print(abs(n[0]-n[1]))
