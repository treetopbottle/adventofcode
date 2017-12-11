#!/usr/bin/env python3

import sys
import collections
import re
import functools

file_name = sys.argv[1]

with open(file_name) as f:
    input_ = f.readlines()

    directions = ['n', 'ne', 'se', 's', 'sw', 'nw']
    opposites = {
        'n': 's',
        'ne': 'sw',
        'se': 'nw',
        's': 'n',
        'sw': 'ne',
        'nw': 'se'
    }

    for line in input_:
        steps = line.strip().split(',')

        travelled = collections.defaultdict(int)
        for step in steps:
            travelled[step] += 1

        distance = 0

        for d in directions:
            if travelled[d] > travelled[opposites[d]]:
                travelled[d] -= travelled[opposites[d]]
                travelled[opposites[d]] -= travelled[opposites[d]]

        print('---')
        print(travelled)

