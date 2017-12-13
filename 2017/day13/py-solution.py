#!/usr/bin/env python3

import sys
import collections
import re
import functools

file_name = sys.argv[1]


with open(file_name) as f:
    input_ = f.readlines()

    layers = {}
    severity = 0
    for line in input_:
        layer, depth = [int(i) for i in line.strip().split(': ')]

        steps_til_return = (depth - 1) * 2
        if layer % steps_til_return == 0:
            severity += layer * depth
            print('caught in layer', layer, steps_til_return)
            

        layers[layer] = (depth, 0, 1)

    print(severity)

