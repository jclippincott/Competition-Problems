cards = list(map(int,input().split()))
total = 0
for i in range(3):
    total += (1+i)*cards[-1-i]

if(total >= 8):
    print("Province or ",end="")
elif(total >= 5):
    print("Duchy or ",end="")
elif(total >= 2):
    print("Estate or ",end="")

if(total >= 6):
    print("Gold")
elif(total >= 3):
    print("Silver")
else:
    print("Copper")
