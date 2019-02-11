#!/usr/bin/env python3

nanobots = []
with open("input") as f:
    for line in f:
        pos_s, r_s = line.strip().split(", ")
        position = [int(i) for i in pos_s[5:-1].split(",")]
        range_ = int(r_s[2:])
        nanobots.append((range_, position))


def get_half(coord1, coord2):
    return coord1 + ((coord2 - coord1) // 2)


def divide(cube):
    (x1, y1, z1), (x2, y2, z2) = cube
    x_half = get_half(x1, x2)
    y_half = get_half(y1, y2)
    z_half = get_half(z1, z2)
    return [
        [(x1,       y1,       z1),       (x_half, y_half, z_half)],
        [(x1,       y1,       z_half+1), (x_half, y_half, z2)    ],
        [(x1,       y_half+1, z1),       (x_half, y2,     z_half)],
        [(x1,       y_half+1, z_half+1), (x_half, y2,     z2)    ],
        [(x_half+1, y1,       z1),       (x2,     y_half, z_half)],
        [(x_half+1, y1,       z_half+1), (x2,     y_half, z2)    ],
        [(x_half+1, y_half+1, z1),       (x2,     y2,     z_half)],
        [(x_half+1, y_half+1, z_half+1), (x2,     y2,     z2)    ],
    ]


def distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1]) + abs(pos1[2] - pos2[2])


def cube_in_range(cube, nanobot):
    corner1, corner2 = cube
    range_, position = nanobot
    return distance(corner1, position) <= range_ \
        or distance(corner2, position) <= range_ \
        or (
            corner1[0] <= position[0] <= corner2[0] \
            and corner1[1] <= position[1] <= corner2[1] \
            and corner1[2] <= position[2] <= corner2[2]
           ) 


def nr_bots_in_range(cube, nanobots):
    total = 0
    for bot in nanobots:
        if cube_in_range(cube, bot):
            total += 1
    return total


# Determine corners of search space
x_min = int(1e12)
y_min = int(1e12)
z_min = int(1e12)
x_max = int(-1e12)
y_max = int(-1e12)
z_max = int(-1e12)
for range_, position in nanobots:
    x_min = min(x_min, position[0])
    y_min = min(y_min, position[1])
    z_min = min(z_min, position[2])
    x_max = max(x_max, position[0])
    y_max = max(y_max, position[1])
    z_max = max(z_max, position[2])

cube = [(x_min, y_min, z_min), (x_max, y_max, z_max)]
while True:
    cubes = divide(cube)
    max_cube, max_bots = None, -1
    for cube in cubes:
        bots_in_range = nr_bots_in_range(cube, nanobots)
        if bots_in_range > max_bots:
            max_cube, max_bots = cube, bots_in_range
    cube = max_cube
    # Single point found
    if cube[0] == cube[1]:
        break

print(distance((0,0,0), max_cube[0]))
