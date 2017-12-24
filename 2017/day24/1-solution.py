#!/usr/bin/env python3

import sys
import collections
import copy


def take_component(to_take, components):
    if len(components[to_take]) == 0:
        return None

    next_ = max(components[to_take])
    components[to_take].remove(next_)
    return next_


file_name = sys.argv[1]

with open(file_name) as f:
    lines = f.readlines()

    components = collections.defaultdict(list)
    for line in lines:
        side1, side2 = line.strip().split('/')
        components[side1].append(side2)

    print(components)

    comp_left = True
    sum_ = 0
    current = '0'
    while comp_left:
        next_ = take_component(current, components)
        print(next_)

        if next_ == None:
            comp_left = False
            break

        sum_ += int(next_)

        current = next_

    print(sum_)

