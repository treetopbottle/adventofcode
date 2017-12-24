#!/usr/bin/env python3

import sys
import collections
import copy


def find_possible_bridges(bridge_so_far, all_components):
    bridge_end = bridge_so_far[-1]

    n1, n2 = bridge_end.split('/')

    # 0/x--0/y is illegal
    if n1 == '0':
        n1 = '-1'
    
    # Can only use ports once
    if len(bridge_so_far) > 2:
        cur_pins = bridge_so_far[-1].split('/')
        prev_pins = bridge_so_far[-2].split('/')

        for pin in prev_pins:
            if pin in cur_pins:
                cur_pins.remove(pin)
        n1 = cur_pins[0]
        if len(cur_pins) > 1:
            n2 = cur_pins[1]

    possible = set(all_components[n1] + all_components[n2])
    for component in possible:
        if component in bridge_so_far:
            continue
        new_bridge = bridge_so_far + [component]
        find_possible_bridges(new_bridge, all_components)
    
    print(bridge_so_far[1:])


file_name = sys.argv[1]

with open(file_name) as f:
    lines = f.readlines()

    what_is_left = []
    components = collections.defaultdict(list)
    for line in lines:
        component = line.strip()
        what_is_left.append(component)

        side1, side2 = component.split('/')
        components[side1].append(component)
        components[side2].append(component)

    print(components)

    tried_combinations = set()
    start_bridge = ['0/0']
    find_possible_bridges(start_bridge, components)
