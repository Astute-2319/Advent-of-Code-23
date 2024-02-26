import os
print(os.getcwd())
os.chdir("C:\\Users\\stute\\OneDrive\\Desktop\\Advent of Code\\Advent-of-Code-23\\Day 2")

inputFile = open("input.txt", 'r')

sum_powers = 0

# For each line
for x in inputFile:
    # Set initial vals
    red_max = 0
    blue_max = 0
    green_max = 0

    # Get the game id for that line
    game_id = x.split(':')
    game_id = int(game_id[0].split(' ')[1])
    print('Game ID: ', game_id)

    # remove the game id from the string
    stripped_x = x.replace('Game ' + str(game_id) + ': ', '')
    stripped_x = stripped_x.strip()

    # get each round results
    rounds = stripped_x.split(';')

    # for each round of the game
    for i in rounds:
        # get each number for each color
        colors = i.split(',')
        # for each color
        for c in colors:
            # update corresponding max value found
            if 'blue' in c:
                if int(c.strip('blue')) > blue_max:
                    blue_max = int(c.strip('blue'))
            elif 'red' in c:
                if int(c.strip('red')) > red_max:
                    red_max = int(c.strip('red'))
            elif 'green' in c:
                if int(c.strip('green')) > green_max:
                    green_max = int(c.strip('green'))
    
    print('Red max: ', red_max)
    print('Blue max: ', blue_max)
    print('Green max: ', green_max)

    # calculate the power of the set of cubes for the game
    power = red_max * blue_max * green_max

    # add the calculated power to running total
    sum_powers += power
    
    print("Sum of powers: ", sum_powers, '\n')
