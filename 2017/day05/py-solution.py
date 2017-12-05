#!/usr/bin/env python3

import sys
import collections
import re

file_name = sys.argv[1]

with open(file_name) as f:
    jumps = f.read().strip()

    jumps = [int(i) for i in jumps.split('\n')]

    steps = 0
    position = 0
    next_pos = 0
    try:
        while True:
            #print(jumps, steps)
            next_pos += jumps[position]
            if jumps[position] >= 3:
                jumps[position] -= 1
            else:
                jumps[position] += 1
            position = next_pos
            steps += 1
    except IndexError:
        pass
        

    print(steps)

