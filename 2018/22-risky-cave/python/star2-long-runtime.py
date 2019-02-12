#!/usr/bin/env python3
# TODO pos = named tuple

from collections import defaultdict


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


region_types = {}
def region_type(position):
    if not position in region_types:
        region_types[position] = erosion_level(position) % 3
    return region_types[position]


# globals
shortest_times = defaultdict(lambda: int(1e12))


def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def get_moves(position, target):
    x, y = position
    moves = [(x, y-1), (x+1, y), (x, y+1), (x-1, y)]
    distance_to_target = lambda x: distance(x, target)
    sorted_by_distance = sorted(zip(map(distance_to_target, moves), moves))
    return map(lambda x: x[1], sorted_by_distance)


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
        assert region_type(previous) != region_type(move)
        assert new_tool != tool
        return spent_time + 8, new_tool
    return spent_time + 1, tool


def fastest_to_target(time_to_target, visited, position, tool, spent_time):
    moves = get_moves(position, target)
    for move in moves:
        if move in visited:
            continue
        x, y = move
        if x < 0 or y < 0:
            continue
        new_time, new_tool = move_to(position, move, spent_time, tool)
        if shortest_times[(move, new_tool)] > new_time:
            shortest_times[(move, new_tool)] = new_time
        else:
            continue
        if new_time + distance(move, target) > time_to_target:
            continue
        if move == target:
            time_to_target = min(time_to_target, new_time)
        time_to_target = fastest_to_target(
            time_to_target, visited + [move], move, new_tool, new_time
        )
    return time_to_target


import sys; sys.setrecursionlimit(100000)

time_to_target = int(1e12)
start = (0, 0)
tool = TORCH
print(fastest_to_target(time_to_target, [], start, tool, 0))
