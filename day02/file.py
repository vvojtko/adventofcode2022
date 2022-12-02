# Yours moves dictionary:
# X for Rock
# Y for Paper
# Z for Scissors

# Opponents moves dictionary:
# A for Rock
# B for Paper
# C for Scissors 

# Scores: 
# 1 for Rock
# 2 for Paper
# 3 for Scissors
# 6 if you won
# 0 if you lost
# 3 if a draw

# e.g. A vs Y (your pick) then your score = 8 (2 for paper + 6 for win)
# e.g. B vs X (your pick) then your score = 1 (1 for Rock + 0 for lose)
def calculateScore(opponentMove, yourMove):
    tempScore = 0
    if yourMove == "X":
        tempScore = 1
        if opponentMove == "C": #WIN
            tempScore = tempScore + 6
        elif opponentMove == "A": #DRAW
            tempScore = tempScore + 3
    elif yourMove == "Y":
        tempScore = 2
        if opponentMove == "A":
            tempScore = tempScore + 6
        elif opponentMove == "B":
            tempScore = tempScore + 3
    else: #IF Z - SCISSORS
        tempScore = 3
        if opponentMove == "B":
            tempScore = tempScore + 6
        elif opponentMove == "C":
            tempScore = tempScore + 3
    return tempScore

filename = "input.txt"
with open(filename) as file:
    totalScore = 0
    for line in file:
        fight = line.rstrip().split(" ")
        #print(fight[0], " vs ",fight[1])
        score = calculateScore(fight[0], fight[1])
        totalScore = totalScore + score
        print("Op move: ", fight[0], "- Your move: ", fight[1], " --  Round score: ", score)
    print("Total score: ", totalScore)