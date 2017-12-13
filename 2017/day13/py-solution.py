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
            

        layers[layer] = depth
    print(severity)
    print(layers)

    for wait in range(10000000):
        print('---')
        caught = False
        for layer in layers:
            depth = layers[layer]

            steps_til_return = (depth - 1) * 2
            if (layer + wait) % steps_til_return == 0:
                caught = True
                print('caught in layer', layer, '( wait', wait, ')', steps_til_return)
                break

        if caught == False:
            print('---')
            print(wait)
            break


