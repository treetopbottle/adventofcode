#!/usr/bin/env python3

import sys
import collections
import copy


def try_component(prev_comp, components, strength, strengths, components_left):
    side1, side2 = prev_comp.split('/')

    possibilities = set(components[side1] + components[side2])

    for comp in possibilities:
        if not comp in components_left:
            continue

        components_left_copy = copy.deepcopy(components_left)
        components_left_copy.remove(comp)
        side1, side2 = prev_comp.split('/')
        new_strength = strength + int(side1) + int(side2)

        try_component(comp, components, new_strength, strengths, components_left_copy)

    strengths.add(strength)
    print('recursion done', len(strengths))


file_name = sys.argv[1]

with open(file_name) as f:
    lines = f.readlines()

    what_is_left = []
    components = collections.defaultdict(list)
    for line in lines:
        component = line.strip()
        what_is_left.append(component)

        side1, side2 = line.strip().split('/')
        components[side1].append(component)
        components[side2].append(component)

    print(components)

    strengths = set()
    strength = 0
    try_component('0/0', components, strength, strengths, what_is_left)

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

