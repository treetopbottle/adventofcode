#!/usr/bin/env python3

from collections import defaultdict


MINUTES = 10


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


pprint(lumber_collection_area)
for _ in range(MINUTES):
    lumber_collection_area = change_landscape(lumber_collection_area)
    pprint(lumber_collection_area)

values = list(lumber_collection_area.values())
print(values.count('|'), values.count('#'))
print(values.count('|') * values.count('#'))
