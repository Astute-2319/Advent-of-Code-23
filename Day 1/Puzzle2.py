# import os
# print(os.getcwd())
# os.chdir("C:\\Users\\OWNER\\Desktop\\Advent of Code 23\\Advent-of-Code-23\\Day 1")

def WordToNum(word) -> int:
    if word == 'one':
        return 1
    elif word == 'two':
        return 2
    elif word == 'three':
        return 3
    elif word == 'four':
        return 4
    elif word == 'five':
        return 5
    elif word == 'six':
        return 6
    elif word == 'seven':
        return 7
    elif word == 'eight':
        return 8
    elif word == 'nine':
        return 9
    else:
        raise Exception("WordToNum: Number not provided")

inputFile = open("input.txt", 'r')

current_line = 1
sum = 0

number_txt = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

for x in inputFile:
    iteration = 0
    numbers = {}
    string = x
    string_filter = ""
    text_numbers = []
    for y in string:
        if y.isdigit():
            numbers[iteration] = int(y)
            iteration += 1
        else:
            string_filter += y
            for z in number_txt:
                if z in string_filter:
                    numbers[iteration] = WordToNum(z)
                    iteration += 1
                    text_numbers.append(z)
                    string_filter = y
            
    print('Current line: ', current_line)
    print('Numbers dict: ', numbers)

    lineNumStr = str(numbers[0]) + str(numbers[iteration-1])

    print('Line val: ', lineNumStr)

    sum += int(lineNumStr)

    print('Sum: ', sum, '\n')
    current_line += 1