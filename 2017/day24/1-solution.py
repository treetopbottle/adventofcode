#!/usr/bin/env python3

import sys
import collections
import copy


def try_component(left_side, components, strength, strengths):
    if len(components[left_side]) == 0:
        strengths.append(strength)
        return

    possibilities = components[left_side]

    for pos in possibilities:
        components_copy = copy.deepcopy(components)
        components_copy[left_side].remove(pos)
        new_strength = strength + int(pos)
        try_component(pos, components_copy, new_strength, strengths)


file_name = sys.argv[1]

with open(file_name) as f:
    lines = f.readlines()

    components = collections.defaultdict(list)
    for line in lines:
        side1, side2 = line.strip().split('/')
        components[side1].append(side2)

    print(components)

    strengths = []
    strength = 0
    try_component('0', components, strength, strengths)

    print(strengths)
    print(max(strengths))

    #comp_left = True
    #sum_ = 0
    #current = '0'
    #while comp_left:
    #    next_ = take_component(current, components)
    #    print(next_)

    #    if next_ == None:
    #        comp_left = False
    #        break

    #    sum_ += int(next_)

    #    current = next_

    #print(sum_)

