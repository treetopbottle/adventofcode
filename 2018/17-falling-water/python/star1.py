#!/usr/bin/env python3

from collections import defaultdict


SPRING_X = 500

class GroundScan():
    SAND = '.'
    CLAY = '#'
    FLOWING_WATER = '|'
    SETTLED_WATER = '~'

    def __init__(self, clay_coords):
        self.ground = defaultdict(lambda: self.SAND)
        for x, y in clay_coords:
            self.ground[(x, y)] = self.CLAY
        self.x_min = min(map(lambda v: v[0], self.ground.keys()))
        self.y_min = min(map(lambda v: v[1], self.ground.keys()))
        self.x_max = max(map(lambda v: v[0], self.ground.keys()))
        self.y_max = max(map(lambda v: v[1], self.ground.keys()))

    def __repr__(self):
        s = ''
        for y in range(self.y_min-1, self.y_max+2):
            for x in range(self.x_min-1, self.x_max+2):
                s += self.ground[(x, y)]
            s += '\n'
        return s

    def blocks_water(self, x, y):
        return self.ground[(x, y)] in [self.CLAY, self.SETTLED_WATER]

    def drop_water(self, x, y):
        while y <= self.y_max+2:
            if self.ground[(x, y)] == self.SAND:
                self.ground[(x, y)] = self.FLOWING_WATER
            elif self.blocks_water(x, y):
                return x, y-1
            else: # flowing water: no need to continue
                return self.x_max+1, self.y_max+1
            y += 1
        return self.x_max+1, self.y_max+1

    def fill_directional(self, x, y, direction):
        filled_spots = [(x, y)]
        while True:
            x += direction
            if self.ground[(x, y)] == self.CLAY:
                return [], filled_spots
            if self.ground[(x, y+1)] == self.SAND:
                return [(x, y)], filled_spots
            filled_spots.append((x, y))

    def fill_water(self, x, y):
        left_overflow, left_spots = self.fill_directional(x, y, -1)
        right_overflow, right_spots = self.fill_directional(x, y, 1)
        overflows = left_overflow + right_overflow
        spots = left_spots + right_spots
        if not overflows:
            for spot in spots:
                self.ground[spot] = self.SETTLED_WATER
            return self.fill_water(x, y-1)
        for spot in spots:
            self.ground[spot] = self.FLOWING_WATER
        return overflows
        
    def start_water(self, x, y=None):
        if not y:
            y = self.y_min
        x, y = self.drop_water(x, y)
        if y <= self.y_max and self.ground[(x, y)] == self.FLOWING_WATER:
            overflows = self.fill_water(x, y)
            for x, y in overflows:
                self.start_water(x, y)

    def count_water(self):
        water = [self.SETTLED_WATER, self.FLOWING_WATER]
        total = 0
        # Don't limit x direction to initial coordinates
        x_min = min(map(lambda v: v[0], self.ground.keys()))
        x_max = max(map(lambda v: v[0], self.ground.keys()))
        for y in range(self.y_min, self.y_max+1):
            for x in range(x_min, x_max+1):
                if self.ground[(x, y)] in water:
                    total += 1
        return total


def parse(coord_string):
    coord, value = coord_string.split("=")
    if ".." in value:
        start, end = [int(v) for v in value.split("..")]
    else:
        start = int(value)
        end = start
    return coord, range(start, end + 1)


def parse_line(coord1, coord2):
    c1, values1 = parse(coord1)
    c2, values2 = parse(coord2)
    if c1 == 'x':
        return values1, values2
    return values2, values1


clay_coords = []
with open("input") as lines:
    for line in lines:
        coord1, coord2 = line.split(", ")
        xvalues, yvalues = parse_line(coord1, coord2)
        for x in xvalues:
            for y in yvalues:
                clay_coords.append((x, y))


ground_scan = GroundScan(clay_coords)
ground_scan.start_water(SPRING_X)
print(ground_scan.count_water())

