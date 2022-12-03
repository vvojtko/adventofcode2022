filename = "input.txt"
listedLine = []

#variables to generate table with alphabet and its corresponding priority
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
priorities = {}
charPriority = 1
for i in alphabet:
    priorities[i]=charPriority
    charPriority=charPriority+1


with open(filename) as file:
    for line in file:
        listedLine.append(line.rstrip())
#print(listedLine)
groups = [[]]


def divideLinesInGroups():
    totalSumOfBadges = 0

    for i in range(0, len(listedLine),3):
        firstCompartment = {}
        secondCompartment = {}
        for j in list(listedLine[i]):
            firstCompartment[j] = "exist"
        for s in list(listedLine[i+1]):
            secondCompartment[s] = "exist"
        #print(firstCompartment)
        #print(secondCompartment)
        for t in list(listedLine[i+2]):
            if((secondCompartment.get(t) == "exist") and firstCompartment.get(t) == "exist"):
                print(t, " exists in both and it has priority: ",priorities.get(t))
                totalSumOfBadges = totalSumOfBadges + priorities.get(t)
                break
        #counter=counter+1
        print("i = ",i)
    return totalSumOfBadges

totalSumOfBadges = divideLinesInGroups()
print(totalSumOfBadges)