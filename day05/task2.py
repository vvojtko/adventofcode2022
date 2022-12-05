filename = "input.txt"

arraysOfMoves = [[]]
arr1 = ['R','N','P','G']
arr2 = ['T','J','B','L','C','S','V','H']
arr3 = ['T','D','B','M','N','L']
arr4 = ['R','V','P','S','B']
arr5 = ['G','C','Q','S','W','M','V','H']
arr6 = ['W','Q','S','C','D','B','J']
arr7 = ['F','Q','L']
arr8 = ['W','M','H','T','D','L','F','V']
arr9 = ['L','P','B','V','M','J','F']
arraysOfMoves.append(arr1)
arraysOfMoves.append(arr2)
arraysOfMoves.append(arr3)
arraysOfMoves.append(arr4)
arraysOfMoves.append(arr5)
arraysOfMoves.append(arr6)
arraysOfMoves.append(arr7)
arraysOfMoves.append(arr8)
arraysOfMoves.append(arr9)

with open(filename) as file:
    for line in file:
        moves = line.rstrip()
        moves = moves.replace("move ","").replace("from ","").replace("to ","")
        moves = moves.split(" ")
        moves = list(map(int, moves)) #cast strings to int
        startSlice = len(arraysOfMoves[moves[1]])-moves[0]
        arrayToMove = arraysOfMoves[moves[1]][startSlice:] #get last n characters
        for i in range(0, moves[0]):
            arraysOfMoves[moves[1]].pop()
        arraysOfMoves[moves[2]].extend(arrayToMove)

for i in arraysOfMoves:
    print(i)