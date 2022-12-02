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

opponentScoreDict = {"A":1,"B":2,"C":3}
yourScoreDict = {"X":1, "Y":2,"Z":3}
#below is a dictionary that is used to output the outcome of a round
#with the following order:
# 1st letter = opponent's move
# 2nd letter = yours move

rulesDictOpponentVsYou= {
    "XA":"draw",
    "AX":"draw",
    "BY":"draw",
    "YB":"draw",
    "CZ":"draw",
    "ZC":"draw",
    "AY":"win",
    "AZ":"lose",
    "BX":"lose",
    "BZ":"win",
    "CX":"win",
    "CY":"lose"
}

def calculateScoreV2(opponentMove, yourMove):
    if(rulesDictOpponentVsYou.get(opponentMove+yourMove)=="lose"):
        return yourScoreDict.get(yourMove)
    elif(rulesDictOpponentVsYou.get(opponentMove+yourMove)=="win"):
        return yourScoreDict.get(yourMove)+6
    else:
        return yourScoreDict.get(yourMove)+3


def calculateScorePartTwo(opponentMove, roundEnding):
        match roundEnding:
            case "Y": #it's a DRAW
                return opponentScoreDict.get(opponentMove)+3
            case "X": #it's a LOSE
                match opponentMove:
                    case "A":
                        return 3
                    case "C":
                        return 2
                    case "B":
                        return 1
            case "Z": #it's a WIN
                match opponentMove:
                    case "C":
                        return 7
                    case "B":
                        return 9
                    case "A":
                        return 8


filename = "input.txt"
with open(filename) as file:
    totalScore = 0
    totalScoreV2 = 0
    totalScorePartTwo = 0
    for line in file:
        fight = line.rstrip().split(" ")
        #print(fight[0], " vs ",fight[1])
        score = calculateScore(fight[0], fight[1])
        scoreV2 = calculateScoreV2(fight[0], fight[1])
        totalScoreV2 = totalScoreV2 + scoreV2
        scorePartTwo = calculateScorePartTwo(fight[0], fight[1])
        totalScore = totalScore + score #total score sum for part 1
        totalScorePartTwo = totalScorePartTwo + scorePartTwo #total socre sum for part 2
        #print("Op move: ", fight[0], "- Your move: ", fight[1], " --  Round score: ", score)
    print("Total score: ", totalScore)
    print("Total score: ", totalScoreV2)
    print("Total score part two: ", totalScorePartTwo)