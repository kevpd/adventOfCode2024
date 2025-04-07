# file1 = open('example.txt', 'r')
file1 = open('input.txt', 'r')
Lines = file1.readlines()

letterMatrix = []

for line in Lines:
    newList = []
    for letter in line:
        if letter != '\n':
            newList.append(letter)
    letterMatrix.append(newList)

for myL in letterMatrix:
    print(myL)

def checkSurroundings(letterMatrix, x, y):
    
    directions = [-1, 0, 1]
    xmasFound = 0

    for oy in directions:
        for ox in directions:
            if(ox != 0 or oy != 0):
                letterCheck = True
                for i in range(4):
                    newX = x + ox * i
                    newY = y + oy * i
                    if newX < 0 or newX >= len(letterMatrix) or newY < 0 or newY >= len(letterMatrix[0]) or letterMatrix[newX][newY] != "XMAS"[i]:
                        letterCheck = False
                if letterCheck:
                    xmasFound += 1
    
    return xmasFound

def checkCross(letterMatrix, x, y):
    directions = [[-1, 1], [-1, -1]]
    mas = ['M', 'S']

    masXFound = 0

    letterCheck = True

    for directionList in directions:
        ox = directionList[0]
        oy = directionList[1]
        
        newX = x + ox
        newY = y + oy

        oppositeX = x - ox
        oppositeY = y - oy

        if newX < 0 or newX >= len(letterMatrix) or newY < 0 or newY >= len(letterMatrix[0]):
            letterCheck = False
        elif oppositeX < 0 or oppositeX >= len(letterMatrix) or oppositeY < 0 or oppositeY >= len(letterMatrix[0]):
            letterCheck = False
        elif not((letterMatrix[newX][newY] == 'M' and letterMatrix[oppositeX][oppositeY] == 'S') or (letterMatrix[newX][newY] == 'S' and letterMatrix[oppositeX][oppositeY] == 'M')):
            letterCheck = False
    if letterCheck:
        masXFound += 1
    
    return masXFound

def calculate(letterMatrix):
    maxX = len(letterMatrix)
    maxY = len(letterMatrix[0])

    xmasFound = 0
    masXFound = 0

    for x in range(maxX):
        for y in range(maxY):
            if(letterMatrix[x][y] == "X"):
                xmasFound += checkSurroundings(letterMatrix, int(x), int(y))
            if(letterMatrix[x][y] == "A"):
                masXFound += checkCross(letterMatrix, int(x), int(y))

    print('Part1: ', xmasFound)
    print('Part2: ', masXFound)

calculate(letterMatrix)