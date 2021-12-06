import pandas as pd

def read_data(filepath, typ):
    my_file = open(filepath)
    data = []
    lines = my_file.readlines()
    # save in the list
    for line in lines: data.append(int(line)) if typ == 'int' else data.append(str(line))
    return data

def move_submarine(data):
    horizontal_position = 0
    depth_position = 0
    aim = 0
    for x in data:
        command = x.split(' ')
        if command[0] == 'forward':
            horizontal_position += int(command[1])
            depth_position += aim * int(command[1])
        elif command[0] == 'down':
            aim += int(command[1])
        elif command[0] == 'up':
            aim -= int(command[1])

    return horizontal_position * depth_position

data = read_data('day_2_input.txt', 'str')
score = move_submarine(data)
print('Final horizontal position multiplied by final depth: ',score)