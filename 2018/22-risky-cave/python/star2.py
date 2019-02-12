#!/usr/bin/env python3
# TODO pos = named tuple

from collections import defaultdict
import heapq


ROCKY = NEITHER = 0
WET = TORCH = 1
NARROW = CLIMBING_GEAR = 2


depth = 0
target = 0, 0
with open("input") as f:
    depth = int(next(f).strip().split(": ")[1])
    target = tuple(int(i) for i in next(f).strip().split(": ")[1].split(","))


# Cache too prevent too many recursive lookups
geologic_indices = {}
def geologic_index(position):
    if not position in geologic_indices:
        x, y = position
        if position == (0, 0):
            geologic_indices[position] = 0
        elif position == target:
            geologic_indices[position] = 0
        elif y == 0:
            geologic_indices[position] = x * 16807
        elif x == 0:
            geologic_indices[position] = y * 48271 
        else:
            erosion_left = erosion_level((x-1, y))
            erosion_up = erosion_level((x, y-1))
            geologic_indices[position] = erosion_left * erosion_up
    return geologic_indices[position]


def erosion_level(position):
    g_index = geologic_index(position)
    return (depth + g_index) % 20183


# Cache
region_types = {}
def region_type(position):
    if not position in region_types:
        region_types[position] = erosion_level(position) % 3
    return region_types[position]


def move_to(previous, move, spent_time, tool):
    if move == target:
        if tool != TORCH:
            return spent_time + 8, TORCH
        return spent_time + 1, TORCH
    if region_type(move) == tool:
        tools = [NEITHER, TORCH, CLIMBING_GEAR]
        # Remove tools unusable in the previous and next region
        tools.remove(region_type(previous))
        tools.remove(region_type(move))
        new_tool = tools[0]
        return spent_time + 8, new_tool
    return spent_time + 1, tool


time_to_target = int(1e12)
shortest_times = defaultdict(lambda: int(1e12))
queue = [(0, 0, 0, TORCH)] # spent_time, x, y, tool
while queue:
    spent_time, x, y, tool = heapq.heappop(queue)
    key = (x, y, tool)
    if shortest_times[(x, y, tool)] <= spent_time:
        continue
    shortest_times[(x, y, tool)] = spent_time
    if (x, y) == target:
        print(spent_time)
        break

    moves = [(x, y-1), (x+1, y), (x, y+1), (x-1, y)]
    for mx, my in moves:
        if mx < 0 or my < 0:
            continue
        new_time, new_tool = move_to((x, y), (mx, my), spent_time, tool)
        heapq.heappush(queue, (new_time, mx, my, new_tool))
