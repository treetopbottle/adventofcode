#!/usr/bin/env python3

from collections import defaultdict


def distance(c1, c2):
    return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])


with open('input') as f:
    lines = f.read().splitlines()

coords = [tuple([int(i) for i in l.split(', ')]) for l in lines]

xs = [c[0] for c in coords]
ys = [c[1] for c in coords]

top_left = (min(xs), min(ys))
bottom_right = (max(xs), max(ys))

print(top_left, bottom_right)

def inside_edge(coord, top_left, bottom_right):
    x, y = coord
    x_inside = top_left[0] < x and x < bottom_right[0]
    y_inside = top_left[1] < y and y < bottom_right[1]
    return x_inside and y_inside

finite_coords = [c for c in coords if inside_edge(c, top_left, bottom_right)]

nr_closest = defaultdict(int)
for i in range(top_left[0]+1, bottom_right[0]):
    for j in range(top_left[1]+1, bottom_right[1]):
        closest_dist = 1e5
        closest_coords = []
        for coord in coords:
            dist = distance((i,j), coord)
            if dist == closest_dist:
                closest_coords.append(coord)
            elif dist < closest_dist:
                closest_coords = [coord]
                closest_dist = dist
        if len(closest_coords) == 1 and closest_coords[0] in finite_coords:
            nr_closest[closest_coords[0]] += 1

print(max(nr_closest.values()))

