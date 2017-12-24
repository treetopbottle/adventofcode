#!/usr/bin/env python3

import sys
import collections
import copy


def get_bridge_strength(bridge):
    strength = 0
    for component in bridge:
        n1, n2 = component.split('/')
        strength += int(n1) + int(n2)
    return strength


def sort_components(components):
    order = []
    for comp in components:
        strength = get_bridge_strength([comp])
        order.append((strength, comp))
    return [o[1] for o in sorted(order)]


def find_possible_bridges(bridge_so_far, all_components, strengths, tried_bridges):
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
    possible = sort_components(possible)
    for component in possible:
        if component in bridge_so_far:
            continue
        new_bridge = bridge_so_far + [component]
        if len(new_bridge) > 3:
            generic_bridge = str((new_bridge[0], new_bridge[-1], sorted(new_bridge[1:-1])))
            if generic_bridge in tried_bridges:
                continue
            tried_bridges.add(generic_bridge)
        find_possible_bridges(new_bridge, all_components, strengths, tried_bridges)
    
    strengths.add(get_bridge_strength(bridge_so_far))
    #print(bridge_so_far[1:])
    if len(tried_bridges) % 1000 == 0:
        print(len(strengths), len(tried_bridges))


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

    tried_bridges = set()
    start_bridge = ['0/0']
    strengths = set()
    find_possible_bridges(start_bridge, components, strengths, tried_bridges)

    print(max(strengths))
