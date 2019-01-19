problems = {}
line = input()
numSolved = 0
totalTime = 0

while line != "-1":
    parts = line.split()
    time = int(parts[0])
    letter = parts[1]
    outcome = parts[2]
    if(letter in problems):
        problem = problems.get(letter)
        if(problem[1] != "done"):
            if(outcome == "right"):
                outcome = "done"
                numSolved += 1
                totalTime += time + problem[0]
            else:
                problem[0] += 20
        problems[letter] = problem
    else:
        if(outcome == "right"):
            outcome = "done"
            numSolved += 1
            totalTime += time
        else:
            time = 20
        problems[letter] = [time,outcome]
    line = input()

print("%d %d" %(numSolved,totalTime))
