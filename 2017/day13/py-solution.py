#!/usr/bin/env python3

import sys
import collections
import re
import functools

file_name = sys.argv[1]


with open(file_name) as f:
    input_ = f.readlines()

    end_layer = 0
    #layers = collections.defaultdict(tuple)
    layers = {}
    for line in input_:
        layer, depth = [int(i) for i in line.strip().split(': ')]

        layers[layer] = (depth, 0, 1)
        print(layer, depth)
        end_layer = layer

    severity = 0
    for cur_layer in range(end_layer+1):
        if cur_layer in layers and layers[cur_layer][1] == 0:
            severity += cur_layer * layers[cur_layer][0]
            print('caught in layer', cur_layer, severity)

        for layer in layers:
            depth, position, direction = layers[layer]
            position += direction
            if position == depth - 1:
                direction = direction * -1
            elif position == 0:
                direction = direction * -1
            layers[layer] = (depth, position, direction)
        print(layers)
        

    print(severity)

