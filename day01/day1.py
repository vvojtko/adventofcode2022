elvesBaggage = []

#Function for reading input from a file
#It reads the file line by line including spaces

elves = []

def readFile(filename):
    with open("input.txt") as file:
        temp = 0 #temp variable for storing sum of calories for each elf
        for line in file:
            if (len(line)<2): #if line is a space
                elves.append(temp)
                print("")
                temp = 0
            else:
                temp = temp + int((line.rstrip()))
                print(temp)

readFile("input.txt")

print("Max cal is: " + str(max(elves)))

def saveToFile():
    with open('output.txt', 'w') as fp:
        for item in elves:
            # write each item on a new line
            fp.write(str(item) + "\n")
        print('Done')
saveToFile()

