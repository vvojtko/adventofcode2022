filename = "input.txt"

input = [[]]
firstCompartments = []
secondCompartments = []
with open(filename) as file:
    for line in file:
        listedLine = list(line.rstrip())
        firstCompartment = listedLine[:len(listedLine)//2] #divide array - first part 
        secondCompartment = listedLine[len(listedLine)//2:] #divide array - second part
        firstCompartments.append(firstCompartment)
        secondCompartments.append(secondCompartment)

#variables to generate table with alphabet and its corresponding priority
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
priorities = {}
charPriority = 1
for i in alphabet:
    priorities[i]=charPriority
    charPriority=charPriority+1

firstCompartmentsDict = {}
totalSumOfRepeatedItems = 0
for i in range(0, len(secondCompartments)):
    firstCompartmentsDict = {}
    for item in firstCompartments[i]:
        firstCompartmentsDict[item] = "exists"
    for item in secondCompartments[i]:
        if firstCompartmentsDict.get(item) == "exists":
            #print(i,". Repeated character: ",item," and its priority: ",priorities.get(item)) 
            totalSumOfRepeatedItems=totalSumOfRepeatedItems+priorities.get(item)
            break

print(totalSumOfRepeatedItems)

