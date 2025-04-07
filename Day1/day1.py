# file1 = open('example.txt', 'r')
file1 = open('input.txt', 'r')
Lines = file1.readlines()

leftDigits = []
rightDigits = []

for line in Lines:
    digits = line.split()
    leftDigits.append(digits[0])
    rightDigits.append(digits[1])

leftDigits.sort()
rightDigits.sort()


def partOne():
    reading = 0
    count = 0

    for left in leftDigits:
        right = rightDigits[count]
        reading += abs(int(left) - int(right))
        count += 1

    print("Part 1: ", reading)
    

def partTwo():
    reading = 0
    count = 0

    for left in leftDigits:
        occurances = rightDigits.count(left)
        reading += int(left) * occurances
    print("Part 2: ", reading)

partOne()
partTwo()





