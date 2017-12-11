#!/usr/bin/env python3

import sys
import collections
import re
import functools

file_name = sys.argv[1]

with open(file_name) as f:
    input_ = f.readlines()

    for line in input_:
        steps = line.strip().split(',')

        pos = [0,0]
        max_distance = 0
        for step in steps:
            if step == 'n':
                pos[0] += 0
                pos[1] += 1
            elif step == 'ne':
                pos[0] += 1
                pos[1] += 0
            elif step == 'se':
                pos[0] += 1
                pos[1] += -1
            elif step == 's':
                pos[0] += 0
                pos[1] += -1
            elif step == 'sw':
                pos[0] += -1
                pos[1] += 0
            elif step == 'nw':
                pos[0] += -1
                pos[1] += 1

            distance = max(abs(pos[0]), abs(pos[1]))
            if pos[0] < 0 and pos[1] < 0:
                distance = abs(pos[0]) + abs(pos[1])
            elif pos[0] > 0 and pos[1] > 0:
                distance = abs(pos[0]) + abs(pos[1])
            
            max_distance = max(distance, max_distance)

        print(max_distance)
        print('----')

