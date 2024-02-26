import os
print(os.getcwd())
os.chdir("C:\\Users\\stute\\OneDrive\\Desktop\\Advent of Code\\Advent-of-Code-23\\Day 2")

inputFile = open("input.txt", 'r')

sum_ids = 0

for x in inputFile:
    game_id = x.split(':')
    game_id = int(game_id[0].split(' ')[1])
    print('Game ID: ', game_id)

    stripped_x = x.replace('Game ' + str(game_id) + ': ', '')
    stripped_x = stripped_x.strip()
    rounds = stripped_x.split(';')
    red_max = 0
    blue_max = 0
    green_max = 0
    for i in rounds:
        colors = i.split(',')
        for c in colors:
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

    if red_max <= 12:
        if green_max <= 13:
            if blue_max <= 14:
                sum_ids += game_id
    
    print("Sum of valid games: ", sum_ids, '\n')
