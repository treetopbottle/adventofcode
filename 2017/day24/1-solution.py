#!/usr/bin/env python3

import sys
import collections
import copy


def get_bridge_strength(bridge):
    strength = 0
    for component in bridge:
        strength += sum(component)
    return strength


def find_possible_bridges(bridge_so_far, prev_port, remaining_components):
    possibilities = []
    for component in remaining_components:
        if prev_port in component:
            possibilities.append(component)

    if len(possibilities) == 0:
        return [bridge_so_far]

    possible_bridges = []
    for component in possibilities:
        remaining_components_copy = remaining_components.copy()
        remaining_components_copy.remove(component)

        to_attach = component.copy()
        to_attach.remove(prev_port)
        new_port = to_attach[0]

        new_bridge = bridge_so_far + [component]
        possible_bridges += find_possible_bridges(new_bridge, new_port, remaining_components_copy)
    return possible_bridges


file_name = sys.argv[1]

with open(file_name) as f:
    lines = f.readlines()

    components = []
    for line in lines:
        string = line.strip()
        component = [int(i) for i in string.split('/')]
        components.append(component)

    print(components)

    bridges = find_possible_bridges([], 0, components)

    max_strength = 0
    for b in bridges:
        s = get_bridge_strength(b)
        max_strength = max(s, max_strength)
    print(max_strength)


