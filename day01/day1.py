elvesBaggage = []

#Function for reading input from a file
#It reads the file line by line including spaces

elves = [] #list init for storing elves' calories

def readFileToList(filename):
    with open("input.txt") as file:
        temp = 0 #temp variable for storing sum of calories for each elf
        for line in file:
            if (len(line)<2): #if line is a space
                elves.append(temp)
                #print("")
                temp = 0
            else:
                temp = temp + int((line.rstrip()))
                #print(temp)

readFileToList("input.txt")

print("Max cal is: " + str(max(elves)))


def listTopThree(list):
    topThree = []
    total = 0
    copyList = list
    for i in range(0,3):
        topThree.append(max(list))
        total = total + max(list)
        copyList.remove(max(list))
    print("Total top three = ",total)
    for i in range(0,3):
        print("Top ", i+1, " ",topThree[i])


listTopThree(elves)

