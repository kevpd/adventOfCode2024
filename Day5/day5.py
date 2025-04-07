file1 = open('example.txt', 'r')
# file1 = open('input.txt', 'r')
Lines = file1.readlines()


rules = {}
printingLines = []
for line in Lines:

    if '|' in line:
        numbers = line.split('\n')[0].split("|")

        if numbers[0] in rules:
            rules[numbers[0]] += [numbers[1]]
        else: 
            rules[numbers[0]] = [numbers[1]]

    if ',' in line:
        printingLines.append(line.split('\n')[0].split(","))

print(rules)
print(printingLines)
def printOrders(rules, printingLines):
    safeCounter = 0
    for order in printingLines:
        isSafe = True
        previousNumbers = []
        for number in order:
            if(len(previousNumbers) > 0 and number in rules and len(list(set(rules[number]) & set(previousNumbers))) > 0):
                isSafe = False
                break
            previousNumbers.append(number)
        if(isSafe):
            middleIndex = round((len(order) - 1) / 2)
            safeCounter += int(order[middleIndex])

    return safeCounter

def correctOrders(rules, printingLines):
    newPrintLines = []
    for order in printingLines:
            isSafe = True
            previousNumbers = []
            for number in order:
                if(len(previousNumbers) > 0 and number in rules and len(list(set(rules[number]) & set(previousNumbers))) > 0):
                    isSafe = False
                    intersection = list(set(rules[number]) & set(previousNumbers))
                    smallestNumber = 1000
                    for offendingNumber in intersection:
                        offendingIndex = previousNumbers.index(offendingNumber)

                        if(offendingIndex < smallestNumber):
                            smallestNumber = offendingIndex

                    previousNumbers.insert(smallestNumber, number)
                else:
                    previousNumbers.append(number)

            if(not isSafe):
                newPrintLines.append(previousNumbers)
    return newPrintLines
                
print("Part 1: ", printOrders(rules, printingLines))
newPrintLines = correctOrders(rules, printingLines)
print("Part 2: ", printOrders(rules, newPrintLines))