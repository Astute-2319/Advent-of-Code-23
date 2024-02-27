import os
print(os.getcwd())
os.chdir("C:\\Users\\stute\\OneDrive\\Desktop\\Advent of Code\\Advent-of-Code-23\\Day 3")

import re

inputFile = open("input.txt", 'r')

# save three lines at a time, as symbols can be read diagonally
line1 = []
line2 = []
line3 = []

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
        line3.append(i)

    # start reading numbers once each line list is filled
    if line1 != []:
        line_pos = 0
        # iterate through line 1, getting locations of symbols and numbers
        print("Line 1")
        for item in line1:
            # item is a symbol
            if not re.search("[0-9.\n]", item):
                print(item)
        print("Line 2")
        for item in line2:
            # item is a symbol
            if not re.search("[0-9.\n]", item):
                print(item)
        print("Line 3")
        for item in line3:
            # item is a symbol
            if not re.search("[0-9.\n]", item):
                print(item)
        

    