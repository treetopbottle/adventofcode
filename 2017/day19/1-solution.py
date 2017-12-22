#!/usr/bin/env python3

import sys
import collections
import string


file_name = sys.argv[1]

with open(file_name) as f:
    diagram = [i[:-1] for i in f.readlines()]

    x,y = diagram[0].index('|'), 0
    dir_x, dir_y = 0, 1

    letters = ''
    end = False
    while not end:
        print(diagram[y][x])
        x += dir_x
        y += dir_y

        if diagram[y][x] == '+':
            if diagram[y+dir_x][x+dir_y] != ' ':
                tmp = dir_y
                dir_y = dir_x
                dir_x = tmp
            elif diagram[y-dir_x][x-dir_y] != ' ':
                tmp = -1 * dir_y
                dir_y = -1 * dir_x
                dir_x = tmp
        

        elif diagram[y][x] == ' ':
            end = True

        elif diagram[y][x] not in '-|+':
            letters += diagram[y][x]

    print(letters)

