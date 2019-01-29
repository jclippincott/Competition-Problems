for i in range(int(input())):
    if(i > 0):
        print("")
    n,k = list(map(int,input().split()))
    state = "ON"
    compare = 0
    for j in range(n):
        compare += 2**j
    if((k&compare) != compare):
        state = "OFF"
    print("Case #%d: %s" %(i+1,state),end="")


## The reason this solution works is because of the way the problem description
## is worded. when a snapper is powered (a 1 bit in this case), and we snap again,
## any powered snappers flip their position. Logically, this is the equivalent of
## a binary addition by 1 to the current number, which will flip all 1 bits until it
## finds a 0. Because of this, we can just start with k instead of doing all of the
## additions, and then compare k to a number with only 1s until the nth bit. If they
## match, that means the light has power, since all of the snappers are on, otherwise
## the light is unpowered.
