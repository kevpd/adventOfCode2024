# file1 = open('example.txt', 'r')
file1 = open('input.txt', 'r')
Lines = file1.readlines()
reading = 0

leftDigits = []
rightDigits = []

for line in Lines:
    digits = line.split()
    leftDigits.append(digits[0])
    rightDigits.append(digits[1])



leftDigits.sort()
rightDigits.sort()

count = 0

for left in leftDigits:
    right = rightDigits[count]
    reading += abs(int(left) - int(right))
    count += 1


print("ANSWER: ", reading)
