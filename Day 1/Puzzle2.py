import os
print(os.getcwd())
os.chdir("C:\\Users\\stute\\OneDrive\\Desktop\\Advent of Code\\Advent-of-Code-23\\Day 1")

# function used to convert a number word to its int val
# takes in a string, returns an int
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

# list of each valid number word
number_txt = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

# for each line
for x in inputFile:
    iteration = 0
    # create a list of numbers present in the line
    numbers = []

    string = x

    # will update with non-int vals, then check each time to see if a number is found
    string_filtered = ""

    # for each character
    for y in string:
        # add y to the list if it's an int
        if y.isdigit():
            numbers.append(int(y))
            iteration += 1
        # otherwise, save the char to the filtered string
        else:
            string_filtered += y
            for z in number_txt:
                # if a number word is present in the string, save its corresponding int val
                if z in string_filtered:
                    numbers.append(WordToNum(z))
                    iteration += 1
                    # save the last character of the filtered string
                    # this way, something like 'oneight' will read one, then eight
                    string_filtered = y
            
    print('Current line: ', current_line)
    print('Numbers dict: ', numbers)

    # the result for the line is equal to the first and last numbers combined into one val
    # for example, 5 and 3 become 53
    lineNumStr = str(numbers[0]) + str(numbers[iteration-1])

    print('Line val: ', lineNumStr)

    # add this number to the total
    sum += int(lineNumStr)

    print('Sum: ', sum, '\n')
    current_line += 1