import re
import itertools

# file1 = open('example.txt', 'r')
file1 = open('input.txt', 'r')
Lines = file1.readlines()

letterMatrix= [] 

equationDictionary = {}
for line in Lines:
    numbers = re.findall(r'\d+', line)
    numberKey = int(numbers[0])
    numbers = numbers[1:]
    equationDictionary[numberKey] = [int(i) for i in numbers]


def computeEquation(eq):
    number = eq[0]
    operatorToUse = ''
    for t in eq[1:]:
        if t in ["*", "+", "|"]:
            operatorToUse = t
        else:
            if operatorToUse == "*":
                number = (number * t)
            elif operatorToUse == "+":
                number = (number + t)
            elif operatorToUse == "|":
                number = (int(f"{number}{t}"))
    return number


def calculate(equationDictionary, operators):
    ret = 0
    for equationKey in equationDictionary.keys():
        punks = equationDictionary[equationKey]
        val = equationKey
        numberOfOperators = len(equationDictionary[equationKey]) - 1

        for ops in itertools.product(operators, repeat=numberOfOperators):
            eq = []
            for p, o in zip(punks, ops):
                eq.append(p)
                eq.append(o)
            eq.append(punks[-1])
            if val == computeEquation(eq):
                ret += val
                break
    return ret


print(equationDictionary)
print(calculate(equationDictionary, "+*"))
print(calculate(equationDictionary, "+*|"))