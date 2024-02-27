import os
print(os.getcwd())
os.chdir("C:\\Users\\stute\\OneDrive\\Desktop\\Advent of Code\\Advent-of-Code-23\\Day 3")

import re

inputFile = open("input.txt", 'r')

# save three lines at a time, as symbols can be read diagonally
line1 = []
line2 = []
line3 = []

# create a dictionary to store where symbols are for each line
# key will be the line num
# data will be a list of symbol locations
symbols = {'line_1': [], 'line_2': [], 'line_3': []}

# for each line
for x in inputFile:
    # push all the other lines "down"
    line1.clear()
    for i in line2:
        line1.append(i)
    line2.clear()
    for i in line3:
        line2.append(i)
    # save the line to the "highest" of the three lists
    line3.clear()
    for i in x:
        if i != '\n':
            line3.append(i)

    # start reading number and symbol locations once each line list is filled
    if line1 != []:
        line_pos = 0
        # iterate through line 1, getting locations of symbols and numbers
        print("Line 1")
        for item in line1:
            # if item is a symbol
            if not re.search("[0-9.\n]", item):
                # save the position of the symbol
                symbols["line_1"].append(line_pos)
            line_pos += 1

        line_pos = 0
        # iterate through line 2, getting locations of symbols and numbers
        print("Line 2")
        for item in line2:
            # if item is a symbol
            if not re.search("[0-9.\n]", item):
                # save the position of the symbol
                symbols["line_2"].append(line_pos)
            line_pos += 1

        line_pos = 0
        # iterate through line 3, getting locations of symbols and numbers
        print("Line 3")
        for item in line3:
            # if item is a symbol
            if not re.search("[0-9.\n]", item):
                # save the position of the symbol
                symbols["line_3"].append(line_pos)
            line_pos += 1
        

    