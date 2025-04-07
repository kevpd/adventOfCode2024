import re

# file1 = open('example.txt', 'r')
file1 = open('input.txt', 'r')
Lines = file1.readlines()

fullText = ''
for line in Lines:
    fullText += line

pattern = r"don't\(\).*?do\(\)"
cleanedText = re.sub(pattern, "", fullText, flags=re.DOTALL)
print(cleanedText)
trailingDont = r"don't\(\).*"
cleanedText = re.sub(trailingDont, "", cleanedText, flags=re.DOTALL)

uncleanedNumbers = re.findall(r'mul\((\d+),(\d+)\)', fullText)
cleanedNumbers = re.findall(r'mul\((\d+),(\d+)\)', cleanedText)

def calculate(numberList):
    total = 0
    for multipliers in numberList:
        if(int(multipliers[0]) <= 999 and int(multipliers[1]) <= 999):
            total += int(multipliers[0]) * int(multipliers[1])

    return total
# def isSafeReport(report):
#     oldNum = None
#     isSafe = True
#     total = 0

#     direction = 0

#     for number in report:
#         if(oldNum):
#             difference = oldNum - int(number)
#             if(abs(difference) > 3 or difference == 0 or (direction * difference < 0)) : 
#                 isSafe = False

#             total += difference
#             direction = difference

#         oldNum = int(number)

#     return isSafe


print("Part 1:", calculate(uncleanedNumbers))
print("Part 2:", calculate(cleanedNumbers))





