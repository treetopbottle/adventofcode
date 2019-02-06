#!/usr/bin/env python3

import collections
import itertools


Unit = collections.namedtuple('Unit', ['type', 'hp', 'has_moved'])


class World():
    def __init__(self, lines):
        self.width = len(lines[0])
        self.height = len(lines)
        self.grid = {}
        for j,line in enumerate(lines):
            for i,char in enumerate(line.strip()):
                if char in ['G', 'E']:
                    self.grid[(i,j)] = Unit(char, 200, False)
                else:
                    self.grid[(i,j)] = char

    def __repr__(self):
        s = ''
        for j in range(self.height):
            for i in range(self.width):
                c = self.grid[(i,j)]
                if isinstance(c, Unit):
                    s += c.type
                else:
                    s += c
            s += '\n'
        return s

    def reset_moved(self):
        # TODO loop over all units: duplication
        for j in range(self.height):
            for i in range(self.width):
                c = self.grid[(i,j)]
                if isinstance(c, Unit):
                    # TODO mutable tuple alternative?
                    self.grid[(i,j)] = Unit(c.type, c.hp, False)

    def do_round(self):
        for j in range(self.height):
            for i in range(self.width):
                c = self.grid[(i,j)]
                if isinstance(c, Unit) and not c.has_moved:
                    self.do_turn((i,j))
                pass
        self.reset_moved()
        return False

    def do_turn(self, unit_loc):
        self.move(unit_loc)
        self.attack(unit_loc)

    def get_adjacent(self, loc):
        i, j = loc
        possible = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        return [p for p in possible if p in self.grid]

    def get_adjacent_available(self, loc):
        locs = self.get_adjacent(loc)
        return [l for l in locs if self.grid[l] == '.']

    def is_in_range_of_target(self, loc, unit_type):
        unit = self.grid[loc]
        adjacent_squares = self.get_adjacent(loc)
        for square in adjacent_squares:
            c = self.grid[square]
            if isinstance(c, Unit) and c.type != unit_type:
                return True
        return False

    def get_targets(self, unit_loc):
        unit = self.grid[unit_loc]
        targets = []
        for j in range(self.height):
            for i in range(self.width):
                c = self.grid[(i,j)]
                if isinstance(c, Unit) and c.type != unit.type:
                    targets.append((i,j))
        return targets

    def get_path_to_target(self, unit_loc):
        paths = [[unit_loc]]
        visited = set([unit_loc])
        target_found = False
        paths_to_target = []
        while not target_found:
            new_paths = []
            for path in paths:
                available_locs = self.get_adjacent_available(path[-1])
                for loc in available_locs:
                    if loc in visited:
                        continue
                    if self.is_in_range_of_target(loc, self.grid[unit_loc].type):
                        target_found = True
                        paths_to_target.append(path + [loc])
                    new_paths.append(path + [loc])
                    visited.add(loc)
            paths = new_paths
        # TODO return first in reading order
        if target_found:
            return paths_to_target[0]
        return None

    def move(self, unit_loc):
        if self.is_in_range_of_target(unit_loc, self.grid[unit_loc].type):
            return
        #targets = self.get_targets(unit_loc)
        #adjacent_to_targets = list(
        #    itertools.chain(
        #        *map(self.get_adjacent_available, targets)
        #    )
        #)
        path = self.get_path_to_target(unit_loc)
        if not path:
            return
        #print(path)
        unit = self.grid[unit_loc]
        self.grid[unit_loc] = '.'
        self.grid[path[1]] = Unit(unit.type, unit.hp, True)

    def attack(self, unit_loc):
        pass



world = {}
with open("input") as f:
    lines = [l.strip() for l in f.readlines()]
    world = World(lines)

print(world)
import time
for i in range(45):
    world.do_round()
    time.sleep(1)
    print(world)

