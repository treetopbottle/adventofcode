#!/usr/bin/env python3

import fileinput


# Globals

numpad = [
    [0,0,1,0,0],
    [0,2,3,4,0],
    [5,6,7,8,9],
    [0,'A','B','C',0],
    [0,0,'D',0,0],
]
x,y = 2,0


def get_pos(x, y, instructions):
    for i in instructions:
        new_x = x
        new_y = y
        if i == 'U':
            new_x = max(0, x-1)
        elif i == 'D':
            new_x = min(4, x+1)
        elif i == 'L':
            new_y = max(0, y-1)
        elif i == 'R':
            new_y = min(4, y+1)
        if numpad[new_x][new_y] != 0:
            x = new_x
            y = new_y
    return x,y

code = ''
for line in fileinput.input():
    x,y = get_pos(x, y, line)
    code += str(numpad[x][y])

print(code)


fileinput.close()

