#!/usr/bin/env python3

nanobots = []
with open("input") as f:
    for line in f:
        pos_s, r_s = line.strip().split(", ")
        position = [int(i) for i in pos_s[5:-1].split(",")]
        range_ = int(r_s[2:])
        nanobots.append((range_, position))


def distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1]) + abs(pos1[2] - pos2[2])


strongest = max(nanobots)
print(strongest)

nr_bots_in_range = 0
for range_, position in nanobots:
    if distance(position, strongest[1]) <= strongest[0]:
        nr_bots_in_range += 1
print(nr_bots_in_range)
