#!/usr/bin/env python3

from collections import defaultdict


MINUTES = 1000000000


dimensions = 0
lumber_collection_area = defaultdict(lambda: '.')
with open("input") as f:
    for j,line in enumerate(f):
        for i,c in enumerate(line.strip()):
            lumber_collection_area[(i, j)] = c
    dimensions = len(line.strip())


def get_adjacent(area, i, j):
    return [
        area[(i-1, j-1)],
        area[(i,   j-1)],
        area[(i+1, j-1)],
        area[(i-1, j)],
        area[(i+1, j)],
        area[(i-1, j+1)],
        area[(i,   j+1)],
        area[(i+1, j+1)],
    ]


def change_landscape(area):
    new_area = defaultdict(lambda: '.')
    for j in range(dimensions):
        for i in range(dimensions):
            adjacent = get_adjacent(area, i, j)
            old_acre = area[(i, j)]
            new_acre = old_acre
            if old_acre == '.':
                if adjacent.count('|') >= 3:
                    new_acre = '|'
            elif old_acre == '|':
                if adjacent.count('#') >= 3:
                    new_acre = '#'
            elif old_acre == '#':
                if adjacent.count('#') < 1 or adjacent.count('|') < 1:
                    new_acre = '.'
            new_area[(i, j)] = new_acre
    return new_area


def pprint(area):
    for j in range(dimensions):
        for i in range(dimensions):
            print(area[(i, j)], end="")
        print()
    print()


seen_situations = defaultdict(list)
m = 0
while m < MINUTES:
    lumber_collection_area = change_landscape(lumber_collection_area)
    m += 1
    hash_ = tuple(lumber_collection_area.items())
    seen_situations[hash_].append(m)
    minutes_seen = seen_situations[hash_]
    if len(minutes_seen) > 1:
        loop_diff = minutes_seen[1] - minutes_seen[0]
        if m + loop_diff > MINUTES:
            continue
        number_of_loops_to_go = (MINUTES - m) // loop_diff
        m += number_of_loops_to_go * loop_diff

values = list(lumber_collection_area.values())
print(values.count('|'), values.count('#'))
print(values.count('|') * values.count('#'))
