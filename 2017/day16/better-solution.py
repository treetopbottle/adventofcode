#!/usr/bin/env python3

import sys
import collections
import re

file_name = sys.argv[1]

def dance(positions, moves):
    for move in moves:
        type_ = move[0]
        op = move[1:]

        if type_ == 's':
            index = -1 * int(op)
            positions = positions[index:] + positions[:index]
        elif type_ == 'x':
            index1, index2 = [int(i) for i in op.split('/')]

            # swap
            temp = positions[index1]
            positions[index1] = positions[index2]
            positions[index2] = temp
        elif type_ == 'p':
            char1, char2 = op.split('/')
            index1 = positions.index(char1)
            index2 = positions.index(char2)

            # swap
            temp = positions[index1]
            positions[index1] = positions[index2]
            positions[index2] = temp
    return positions
    

with open(file_name) as f:
    input_ = f.read().strip()
    #input_ = 's1,x3/4,pe/b'

    original_positions = list('abcdefghijklmnop')
    #original_positions = list('abcde')
    positions = original_positions[:]

    moves = input_.split(',')

    i = 0
    print(''.join(positions), i)
    while i < 1e9:
        positions = dance(positions, moves)
        i += 1

        if positions == original_positions:
            print('skipping', i)
            i += (int(1e9 / i) * i) - i

        print(''.join(positions), i)

    print(''.join(positions))

