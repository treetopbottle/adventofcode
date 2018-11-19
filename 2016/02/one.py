#!/usr/bin/env python3

import fileinput


# Globals

numpad = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
x,y = 1,1


def get_pos(x, y, instructions):
    for i in instructions:
        if i == 'U':
            x = max(0, x-1)
        elif i == 'D':
            x = min(2, x+1)
        elif i == 'L':
            y = max(0, y-1)
        elif i == 'R':
            y = min(2, y+1)
    return x,y

code = ''
for line in fileinput.input():
    x,y = get_pos(x, y, line)
    code += str(numpad[x][y])

print(code)


fileinput.close()

