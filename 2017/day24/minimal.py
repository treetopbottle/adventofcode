#!/usr/bin/env python3
import sys


def score(bridge):
    return sum(sum(map(int, i)) for i in bridge)


def find_bridges(connector, bridge, remaining):
    possibles = [i for i in remaining if connector in i]
    if len(possibles) == 0:
        return [bridge]

    bridges = []
    for next_component in possibles:
        new_remaining = remaining.copy()
        new_remaining.remove(next_component)
        new_connector = next_component.copy()
        new_connector.remove(connector)
        bridges += find_bridges(
            new_connector[0],
            bridge + [next_component],
            new_remaining
        )
    return bridges

filename = sys.argv[1]
with open(filename) as f:
    components = list(map(lambda x: x.strip().split('/'), f.readlines()))

    all_bridges = find_bridges('0', [], components)

    solution1 = max(map(score, all_bridges))
    print(solution1)

    solution2 = max(map(lambda x: (len(x), score(x)), all_bridges))
    print(solution2)
