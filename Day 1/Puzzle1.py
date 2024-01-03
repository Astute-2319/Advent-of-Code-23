import os
print(os.getcwd())
os.chdir("C:\\Users\\OWNER\\Desktop\\Advent of Code 23\\Advent-of-Code-23\\Day 1")

inputFile = open("input.txt", 'r')

sum = 0

for x in inputFile:
    numbers = []
    string = x
    for y in string:
        if y.isdigit():
            numbers.append(y)

    lineNumStr = numbers[0] + numbers[-1]

    sum += int(lineNumStr)

    print(sum)