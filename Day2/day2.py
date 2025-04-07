# file1 = open('example.txt', 'r')
file1 = open('input.txt', 'r')
Lines = file1.readlines()

digits = []
for line in Lines:
    digits.append( [int(s) for s in line.split()])

def isSafeReport(report):
    oldNum = None
    isSafe = True
    total = 0

    direction = 0

    for number in report:
        if(oldNum):
            difference = oldNum - int(number)
            if(abs(difference) > 3 or difference == 0 or (direction * difference < 0)) : 
                isSafe = False

            total += difference
            direction = difference


        oldNum = int(number)

    return isSafe

def partOne():
    safetyNumbers = 0
    for newReport in digits:
        isSafe = isSafeReport(newReport)

        print(isSafe, newReport)
        if(isSafe):
            safetyNumbers += 1
            print(newReport)

    print("Part 1: ", safetyNumbers)
    

def partTwo():
    safetyNumbers = 0

    for report in digits:
        isSafe = isSafeReport(report)

        if(isSafe):
            safetyNumbers += 1
            print(report)
        else:
            for index in range(len(report)):
                newReport = list(report)
                newReport.pop(index)
                isSafe = isSafeReport(newReport)

                if(isSafe):
                    print(report)
                    safetyNumbers += 1
                    break
    print("Part 2: ", safetyNumbers)


partOne()
partTwo()





