filename = "input.txt"
with open(filename) as file:
    for line in file:
        code = line.rstrip()
        #print(code)
        code = list(code)
        counter = 0
        markerDict = {}
        print(code[:4])
        run = True
        while run == True:
            for each in range(counter, counter+4):
                #print(code[counter])
                if len(markerDict)==4:
                    run = False
                elif markerDict.get(code[counter]) == None:
                    print(code[counter], " doesn't exist therefore adding it")
                    markerDict[code[counter]] = "exists"
                    counter=counter+1
                elif markerDict.get(code[counter]) == "exists":
                    print(code[counter], "exists already in marker Dict therefore breaking the loop")
                    markerDict = {}
                    break
        print(counter)