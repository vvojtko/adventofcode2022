filename = "input.txt"
with open(filename) as file:
    for line in file:
        code = line.rstrip()
        #print(code)
        code = list(code)
        counter = 0
        counterRepeat = 0 #counter for repeating checking same characters in next loops
        markerDict = {}
        print(code[:4])
        distinctCharacterNumber = 4
        run = True
        while run == True:
            counter=counterRepeat
            for each in range(counter, counter+distinctCharacterNumber):
                if len(markerDict)==distinctCharacterNumber:
                    run = False
                elif markerDict.get(code[counter]) == None:
                    print(code[counter], " doesn't exist therefore adding it")
                    markerDict[code[counter]] = "exists"
                    counter=counter+1
                elif markerDict.get(code[counter]) == "exists":
                    print(code[counter], "exists already in marker Dict therefore breaking the loop")
                    counterRepeat=counterRepeat+1
                    print("counter: ",counter)
                    print("counter repeat: ", counterRepeat)
                    markerDict = {}
                    break
        print(counter+distinctCharacterNumber)

with open(filename) as file:
    for line in file:
        code = line.rstrip()
        #print(code)
        code = list(code)
        counter = 0
        counterRepeat = 0 #counter for repeating checking same characters in next loops
        markerDict = {}
        print(code[:4])
        distinctCharacterNumber = 14
        run = True
        while run == True:
            counter=counterRepeat
            for each in range(counter, counter+distinctCharacterNumber):
                if len(markerDict)==distinctCharacterNumber:
                    run = False
                elif markerDict.get(code[counter]) == None:
                    print(code[counter], " doesn't exist therefore adding it")
                    markerDict[code[counter]] = "exists"
                    counter=counter+1
                elif markerDict.get(code[counter]) == "exists":
                    print(code[counter], "exists already in marker Dict therefore breaking the loop")
                    counterRepeat=counterRepeat+1
                    print("counter: ",counter)
                    print("counter repeat: ", counterRepeat)
                    markerDict = {}
                    break
        print(counter+distinctCharacterNumber)