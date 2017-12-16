#!/usr/bin/env python3

import sys
import collections
import re

file_name = sys.argv[1]

with open(file_name) as f:
    input_ = f.read().strip()
    #input_ = 's1,x3/4,pe/b'

    original_positions = list('abcdefghijklmnop')
    #original_positions = list('abcde')
    positions = original_positions[:]

    moves = input_.split(',')

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

    total_done = 1
    print(''.join(positions))

    swaps = {}
    for i,char in enumerate(original_positions):
        new_position = positions.index(char)
        swaps[i] = new_position

    good_swaps = {}
    for k in swaps:
        good_swaps[swaps[k]] = k
    swaps = good_swaps
    print(swaps)

    circle_num = 0
    for i in range(0,int(1e9)):
        new_positions = []
        for j in range(len(positions)):
            new_char = positions[swaps[j]]
            new_positions.append(new_char)
        positions = new_positions
        print(''.join(positions))
        total_done += 1

        if positions == original_positions:
            break

    print(total_done)
    total_to_do = int(1000000000)
    to_do = (total_to_do - total_done) % total_done
    print(to_do)
    positions = original_positions
    for i in range(total_to_do):
        new_positions = []
        for j in range(len(positions)):
            new_char = positions[swaps[j]]
            new_positions.append(new_char)
        positions = new_positions



    #print(''.join(original_positions))
    print('---')
    print(''.join(positions))

