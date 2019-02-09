#!/usr/bin/env python3

depth = 0
target = 0, 0
with open("input") as f:
    depth = int(next(f).strip().split(": ")[1])
    target = [int(i) for i in next(f).strip().split(": ")[1].split(",")]


def erosion_level(x, y, geologic_indices):
    g_indices = geologic_indices[(x, y)]
    return (depth + g_indices) % 20183


def region_type(x, y, geologic_indices):
    return erosion_level(x, y, geologic_indices) % 3


geologic_indices = {}
region_types = {}
for y in range(target[1] + 1):
    for x in range(target[0] + 1):
        if (x, y) == (0, 0):
            geologic_indices[(x, y)] = 0
        elif (x, y) == target:
            geologic_indices[(x, y)] = 0
        elif y == 0:
            geologic_indices[(x, y)] = x * 16807
        elif x == 0:
            geologic_indices[(x, y)] = y * 48271 
        else:
            erosion_left = erosion_level(x-1, y, geologic_indices)
            erosion_up = erosion_level(x, y-1, geologic_indices)
            geologic_indices[(x, y)] = erosion_left * erosion_up
        region_types[(x, y)] = region_type(x, y, geologic_indices)

print(sum(region_types.values()))
