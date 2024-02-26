import os
print(os.getcwd())
os.chdir("C:\\Users\\stute\\OneDrive\\Desktop\\Advent of Code\\Advent-of-Code-23\\Day 1")

inputFile = open("input.txt", 'r')

sum = 0

# for each line
for x in inputFile:
    # create a list to house every number found
    numbers = []
    string = x
    # for each character
    for y in string:
        if y.isdigit():
            # add y if it is an int
            numbers.append(y)

    # the result for the line is equal to the first and last numbers combined into one val
    # for example, 5 and 3 become 53
    lineNumStr = numbers[0] + numbers[-1]

    # add this number to the total
    sum += int(lineNumStr)

    print(sum)