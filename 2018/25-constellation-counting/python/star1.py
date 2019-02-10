#!/usr/bin/env python3

points = []
with open("input") as f:
    for line in f:
        point = [int(i) for i in line.strip().split(',')]
        points.append(point)


def distance(point1, point2):
    return abs(point1[0] - point2[0]) \
        + abs(point1[1] - point2[1]) \
        + abs(point1[2] - point2[2]) \
        + abs(point1[3] - point2[3])


def in_constellation(point1, point2):
    return distance(point1, point2) <= 3


constellations = []
for point in points:
    point_constellation = [point]
    new_constellations = []
    for constellation in constellations:
        for c_point in constellation:
            if in_constellation(point, c_point):
                point_constellation += constellation
                break
        else:
            new_constellations.append(constellation)
    new_constellations.append(point_constellation)
    constellations = new_constellations

print(len(constellations))
