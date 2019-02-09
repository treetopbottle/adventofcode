#!/usr/bin/env python3

from collections import defaultdict

regex = ""
with open("input") as f:
    regex = next(f).strip()


def pprint(area_map):
    x_min = min(map(lambda v: v[0], area_map.keys()))
    x_max = max(map(lambda v: v[0], area_map.keys()))
    y_min = min(map(lambda v: v[1], area_map.keys()))
    y_max = max(map(lambda v: v[1], area_map.keys()))
    print()
    for y in range(y_min, y_max+1):
        for x in range(x_min, x_max+1):
            print(area_map[(x, y)], end="")
        print()


def set_elf_position(x, y, area_map):
    area_map[(x, y)] = '.'
    area_map[(x-1, y-1)] = '#'
    area_map[(x+1, y-1)] = '#'
    area_map[(x-1, y+1)] = '#'
    area_map[(x+1, y+1)] = '#'


def move_elf(direction, x, y, area_map):
    if direction == 'N':
        area_map[(x, y-1)] = '-'
        x, y = x, y-2
    elif direction == 'E':
        area_map[(x+1, y)] = '|'
        x, y = x+2, y
    elif direction == 'S':
        area_map[(x, y+1)] = '-'
        x, y = x, y+2
    elif direction == 'W':
        area_map[(x-1, y)] = '|'
        x, y = x-2, y
    set_elf_position(x, y, area_map)
    return x, y


# Build the map
start_pos = 0, 0
area_map = defaultdict(lambda: '#')
area_map[(start_pos)] = 'X'

x, y = start_pos
pos_stack = []
for char in regex[1:-1]:
    if char == '(':
        pos_stack.append((x, y))
    elif char == '|':
        x, y = pos_stack[-1]
    elif char == ')':
        x, y = pos_stack.pop()
    else:
        x, y = move_elf(char, x, y, area_map)

# Search for longest path
import sys; sys.setrecursionlimit(10000)

x, y = start_pos
def get_longest_path(x, y, area_map, shortest_paths, length=0, visited=[]):
    shortest_paths[(x, y)] = min(length, shortest_paths[(x, y)])
    surrounding = [
        (area_map[(x, y-1)], (x, y-2)),
        (area_map[(x+1, y)], (x+2, y)),
        (area_map[(x, y+1)], (x, y+2)),
        (area_map[(x-1, y)], (x-2, y)),
    ]
    doors = [s for s in surrounding if s[0] in ['-', '|'] and not s[1] in visited]

    lengths = [length]
    visited = visited + [(x, y)]
    for _, (x, y) in doors:
        l = get_longest_path(x, y, area_map, shortest_paths, length+1, visited)
        lengths.append(l)

    return max(lengths)

shortest_paths = defaultdict(lambda: 10_000)
get_longest_path(x, y, area_map, shortest_paths)
print(len([v for v in shortest_paths.values() if v >= 1000]))
