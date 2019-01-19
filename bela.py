dom = {"A":11,"K":4,"Q":3,"J":20,"T":10,"9":14,"8":0,"7":0}
non = {"A":11,"K":4,"Q":3,"J":2,"T":10,"9":0,"8":0,"7":0}

line = input().split()
total = 0
for i in range(4*int(line[0])):
    card = input()
    if(card[1] == line[1]):
        total += dom.get(card[0])
    else:
        total += non.get(card[0])
print(total)
