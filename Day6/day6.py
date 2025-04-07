# file1 = open('example.txt', 'r')
file1 = open('input.txt', 'r')
Lines = file1.readlines()

letterMatrix= [] 
for line in Lines:
    newList = []
    for letter in line:
        if letter != '\n':
            newList.append(letter)
    letterMatrix.append(newList)

characters = ['^', '>', 'v', '<']
walls = ['#', '$']

def rotate(character): 
    if character == '^': 
        return '>'
    elif character == '>':
        return 'v'
    elif character == 'v':
        return '<'
    elif character == '<':
        return '^'

def getDirection(character): 
    if character == '^': 
        return [0, -1]
    elif character == '>':
        return [1, 0]
    elif character == 'v':
        return [0, 1]
    elif character == '<':
        return [-1, 0]

startingX = 0
startingY = 0

for y in range(len(letterMatrix)):
    print(y, letterMatrix[y])
    for x in range(len(letterMatrix[y])):
        if(letterMatrix[y][x] in characters):
            startingY = y
            startingX = x
            myChar = letterMatrix[y][x]

xDirection, yDirection = getDirection(myChar)

movingY = startingY
movingX = startingX
nextX = movingX + xDirection
nextY = movingY + yDirection

pointsTravelled = [(movingX, movingY)]

while(nextY >= 0 and nextY < len(letterMatrix) and nextX >= 0 and nextX < len(letterMatrix[0])):
    if(letterMatrix[nextY][nextX] == '#'):
        myChar = rotate(myChar)
        xDirection, yDirection = getDirection(myChar)
        nextX = movingX + xDirection
        nextY = movingY + yDirection
        continue
    if not((nextX, nextY) in pointsTravelled):
        pointsTravelled.append((nextX, nextY))

    movingX = nextX
    movingY = nextY
    nextX = movingX + xDirection
    nextY = movingY + yDirection

print("Part 1", len(pointsTravelled))

infiniteLoops = 0

for x, y in pointsTravelled:
    if(letterMatrix[y][x] in characters or letterMatrix[y][x] == '#'):
        print("Found Wall")
    else:
        letterMatrix[y][x] = '#'

        movingY = startingY
        movingX = startingX
        myChar = letterMatrix[movingY][movingX]

        xDirection, yDirection = getDirection(myChar)

        nextX = movingX + xDirection
        nextY = movingY + yDirection
        loopChecker = []

        while(nextY >= 0 and nextY < len(letterMatrix) and nextX >= 0 and nextX < len(letterMatrix[0])):
            if(letterMatrix[nextY][nextX] == '#'):
                myChar = rotate(myChar)
                xDirection, yDirection = getDirection(myChar)
                nextX = movingX + xDirection
                nextY = movingY + yDirection
                continue

            if((movingX, movingY, nextX, nextY) in loopChecker):
                print('FoundInfinite')
                infiniteLoops += 1
                break

            loopChecker.append((movingX, movingY, nextX, nextY))

            movingX = nextX
            movingY = nextY
            nextX = movingX + xDirection
            nextY = movingY + yDirection

        letterMatrix[y][x] = '.'
    print(x,y)

print(infiniteLoops)