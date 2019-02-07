#!/usr/bin/env python3


ATTACK_POWER = 3
HIT_POINTS = 200


class Unit():
    def __init__(self, type_, hp, has_moved):
        self.type = type_
        self.hp = hp
        self.has_moved = has_moved

    def __repr__(self):
        return f"{self.type}({self.hp})"


class World():
    def __init__(self, lines, extra_elf_ap):
        self.width = len(lines[0])
        self.height = len(lines)
        self.grid = {}
        for i,line in enumerate(lines):
            for j,char in enumerate(line.strip()):
                if char in ['G', 'E']:
                    self.grid[(i,j)] = Unit(char, HIT_POINTS, False)
                else:
                    self.grid[(i,j)] = char
        self.extra_elf_ap = extra_elf_ap
        self.elves_died = False
        self.rounds = 0

    def __repr__(self):
        s = ""
        for i in range(self.height):
            units_in_line = []
            for j in range(self.width):
                c = self.grid[(i,j)]
                if isinstance(c, Unit):
                    s += c.type
                    units_in_line.append(c)
                else:
                    s += c
            s += "  " + ", ".join([str(u) for u in units_in_line])
            s += "\n"
        s += f"round: {self.rounds}\n"
        return s

    def reset_moved(self):
        for i in range(self.height):
            for j in range(self.width):
                c = self.grid[(i,j)]
                if isinstance(c, Unit):
                    c.has_moved = False

    def do_round(self):
        for i in range(self.height):
            for j in range(self.width):
                c = self.grid[(i,j)]
                if isinstance(c, Unit) and not c.has_moved:
                    found_targets = self.do_turn((i,j))
                    if not found_targets:
                        return False
        self.reset_moved()
        self.rounds += 1
        return True

    def has_targets_remaining(self, unit_type):
        for i in range(self.height):
            for j in range(self.width):
                c = self.grid[(i,j)]
                if isinstance(c, Unit) and c.type != unit_type:
                    return True
        return False

    def do_turn(self, unit_loc):
        unit_type = self.grid[unit_loc].type
        has_targets = self.has_targets_remaining(unit_type)
        if not has_targets:
            return False
        unit_loc = self.move(unit_loc)
        self.attack(unit_loc)
        return True

    def get_adjacent(self, loc):
        i, j = loc
        # sort for reading order
        possible = sorted([(i-1, j), (i+1, j), (i, j-1), (i, j+1)])
        return [p for p in possible if p in self.grid]

    def get_adjacent_available(self, loc):
        locs = self.get_adjacent(loc)
        return [l for l in locs if self.grid[l] == '.']

    def get_best_target(self, loc, unit_type):
        unit = self.grid[loc]
        adjacent_squares = self.get_adjacent(loc)
        min_hp = HIT_POINTS + 1
        target_loc = None
        for square in adjacent_squares:
            c = self.grid[square]
            if isinstance(c, Unit) and c.type != unit_type and c.hp < min_hp:
                 target_loc = square
                 min_hp = c.hp
        return target_loc

    def get_targets(self, unit_loc):
        unit = self.grid[unit_loc]
        targets = []
        for i in range(self.height):
            for j in range(self.width):
                c = self.grid[(i,j)]
                if isinstance(c, Unit) and c.type != unit.type:
                    targets.append((i,j))
        return targets

    def get_best_path(self, paths):
        best_path = paths[0]
        for path in paths[1:]:
            if path[-1] < best_path[-1]:
                best_path = path
        return best_path

    def get_path_to_target(self, unit_loc):
        paths = [[unit_loc]]
        visited = set([unit_loc])
        target_found = False
        untried_locs = True
        while untried_locs and not target_found:
            new_paths = []
            paths_to_target = []
            untried_locs = False
            for path in paths:
                available_locs = self.get_adjacent_available(path[-1])
                for loc in available_locs:
                    if loc in visited:
                        continue
                    untried_locs = True
                    if self.get_best_target(loc, self.grid[unit_loc].type):
                        target_found = True
                        paths_to_target.append(path + [loc])
                    new_paths.append(path + [loc])
                    visited.add(loc)
            paths = new_paths
        if target_found:
            return self.get_best_path(paths_to_target)
        return None

    def move(self, unit_loc):
        if self.get_best_target(unit_loc, self.grid[unit_loc].type):
            return unit_loc
        path = self.get_path_to_target(unit_loc)
        if not path:
            return unit_loc
        # Move one step
        unit = self.grid[unit_loc]
        self.grid[unit_loc] = '.'
        self.grid[path[1]] = unit
        unit.has_moved = True
        return path[1]

    def attack(self, unit_loc):
        unit = self.grid[unit_loc]
        target_loc = self.get_best_target(unit_loc, unit.type)
        if not target_loc:
            return
        target = self.grid[target_loc]
        target.hp -= ATTACK_POWER
        if unit.type == 'E':
            target.hp -= self.extra_elf_ap
        if target.hp <= 0:
            if target.type == 'E':
                self.elves_died = True
            self.grid[target_loc] = '.'

    def get_hp_sum(self):
        total = 0
        for i in range(self.height):
            for j in range(self.width):
                c = self.grid[(i,j)]
                if isinstance(c, Unit):
                    total += c.hp
        return total

    def get_nr_elves(self):
        total = 0
        for i in range(self.height):
            for j in range(self.width):
                c = self.grid[(i,j)]
                if isinstance(c, Unit) and c.type == 'E':
                    total += 1
        return total


def run_simulation(file_name):
    for i in range(50):
        world = None
        with open(file_name) as f:
            lines = [l.strip() for l in f.readlines()]
            world = World(lines, i)

        rounds = 0
        round_finished = True
        while round_finished:
            round_finished = world.do_round()

        if not world.elves_died:
            print("Simulation for '{}'".format(file_name))
            print(
                world.rounds, '*', world.get_hp_sum(), '=',
                world.rounds * world.get_hp_sum()
            )
            print("Total remaining elves", world.get_nr_elves())
            print("Total elf attack power", i + ATTACK_POWER)
            print(world)
            break


import os
for root, _, files in os.walk('examples'):
    for f in sorted(files):
        run_simulation(os.path.join(root,f))
run_simulation("input")

