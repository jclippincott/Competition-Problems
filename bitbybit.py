def setval(num,index,val):
    if(val == 1):
        num = num | (1 << index)
    else:
        num = num & (~(1 << index))
    return num

def main():
    n = int(input())
    while (n != 0):
        num = 0
        qs = 0
        for i in range(n):
            comm = input().split()
            shift1 = int(comm[1])
            if(comm[0] == "SET"):
                num = setval(num,shift1,1)
                qs = setval(qs,shift1,1)
            elif(comm[0] == "CLEAR"):
                num = setval(num,shift1,0)
                qs = setval(qs,shift1,1)
            else:
                shift2 = int(comm[2])
                q1 = (qs & (1 << shift1))>>shift1
                q2 = (qs & (1 << shift2))>>shift2
                dig1 = (num & (1 << shift1))>>shift1
                dig2 = (num & (1 << shift2))>>shift2
                if(comm[0] == "AND"):
                    if(q1 == q2 == 1):
                        num = setval(num,shift1,(dig1&dig2))
                    elif((q1 == 1 != dig1) or (q2 == 1 != dig2)):
                        num = setval(num,shift1,0)
                        qs = setval(qs,shift1,1)
                    else:
                        qs = setval(qs,shift1,0)
                else:
                    if(q1 == q2 == 1):
                        num = setval(num,shift1,(dig1|dig2))
                    elif((q1 == 1 == dig1) or (q2 == 1 == dig2)):
                        num = setval(num,shift1,1)
                        qs = setval(qs,shift1,1)
                    else:
                        qs = setval(qs,shift1,0)
        for i in range(31,-1,-1):
            currq = (qs & (1 << i))>>i
            if(currq == 1):                
                currdig = (num & (1 << i))>>i
                print(currdig,end="")
            else:
                print("?",end="")
        print("")
        n = int(input())

main()
