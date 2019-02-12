#!/usr/bin/env python3

import re


def search(target, line):
    result = []
    matches = re.search(target, line)
    if matches:
        result = matches.groups()[0].split(', ')
    return result


def parse_group(line, army_type, number):
    nr_units = int(search("(\d+) units each", line)[0])
    hit_points = int(search("(\d+) hit points", line)[0])
    weaknesses = search("weak to ([^;)]*)", line)
    immunities = search("immune to ([^;)]*)", line)
    attack_power = int(search("attack that does (\d+)", line)[0])
    attack_type = search("(\w+) damage", line)[0]
    initiative = int(search("at initiative (\d+)", line)[0])
    return Group(
        nr_units,
        hit_points,
        weaknesses,
        immunities,
        attack_power,
        attack_type,
        initiative,
        army_type,
        number
    )


def parse_army(lines):
    army_type = lines[0][:-1]
    groups = []
    for i,line in enumerate(lines[1:]):
        groups.append(parse_group(line, army_type, i + 1))
    return Army(army_type, groups)


def parse_file(file_name):
    with open(file_name) as f:
        s = f.read()
    s1, s2 = s.split('\n\n')

    immune_system = parse_army(s1.splitlines())
    infection = parse_army(s2.splitlines())
    return immune_system, infection


class Army():
    def __init__(self, name, groups):
        self.name = name
        self.groups = groups

    def __repr__(self):
        s = f"{self.name}:\n"
        if self.groups:
            for group in self.groups:
                s += str(group) + '\n'
        else:
            s += "No groups remain.\n"
        return s[:-1]

    @property
    def total_units(self):
        return sum(map(lambda g: g.nr_units, self.groups))

    def contains_units(self):
        return len(self.groups) > 0

    @staticmethod
    def sort_groups(groups):
        effective_powers = map(lambda g: g.effective_power, groups)
        initiatives = map(lambda g: g.initiative, groups)
        return sorted(zip(effective_powers, initiatives, groups), reverse=True)

    def select_targets(self, other_army):
        targets = other_army.groups[:]
        sorted_groups = Army.sort_groups(self.groups)
        for _, _, group in sorted_groups:
            target = group.select_target(targets)
            if target:
                targets.remove(target)

    def remove_empty_groups(self):
        self.groups = list(
            filter(lambda g: g.effective_power > 0, self.groups)
        )

    def boost(self, amount):
        for group in self.groups:
            group.attack_power += boost


class Group():
    def __init__(self, nr_units, hit_points, weaknesses, immunities, 
            attack_power, attack_type, initiative, army_type, number):
        self.nr_units = nr_units
        self.hit_points = hit_points
        self.weaknesses = weaknesses
        self.immunities = immunities
        self.attack_power = attack_power
        self.attack_type = attack_type
        self.initiative = initiative
        self.army_type = army_type
        self.number = number
        self.target = None

    def __repr__(self):
        return f"Group {self.number}, containing {self.nr_units} units"

    @property
    def effective_power(self):
        return self.nr_units * self.attack_power

    def damage(self, target):
        if self.attack_type in target.weaknesses:
            return 2 * self.effective_power
        if self.attack_type in target.immunities:
            return 0
        return self.effective_power

    def select_target(self, targets):
        if not targets:
            return None
        damages = map(lambda t: self.damage(t), targets)
        effective_powers = map(lambda t: t.effective_power, targets)
        initiatives = map(lambda t: t.initiative, targets)
        sorted_targets = sorted(
            zip(damages, effective_powers, initiatives, targets),
            reverse=True
        )
        # only select a target if it can deal damage
        if sorted_targets[0][0] > 0:
            self.target = sorted_targets[0][3]
        #print()
        #print('selecting')
        #print(self)
        #print(self.target)
        #print(sorted_targets[0][0])
        return self.target

    def attack(self):
        if self.target == None:
            return
        damage = self.damage(self.target)
        nr_units_damaged = damage // self.target.hit_points
        #print(damage, self.target.hit_points)
        nr_units_killed = min(nr_units_damaged, self.target.nr_units)
        #print(nr_units_killed, nr_units_damaged)
        self.target.nr_units -= nr_units_killed
        self.target = None


if __name__ == '__main__':
    #boost_min, boost_max = 0, 10_000
    # Manually found boost level, some get stuck in an infinite loop
    boost_min, boost_max = 61, 61
    while True:
        immune_system, infection = parse_file("input")

        boost = boost_min + ((boost_max - boost_min) // 2)
        #print("boosting with", boost)
        immune_system.boost(boost)
        while immune_system.contains_units() and infection.contains_units():
            # Select targets
            immune_system.select_targets(infection)
            infection.select_targets(immune_system)

            # Attack
            all_groups = []
            all_groups.extend(immune_system.groups)
            all_groups.extend(infection.groups)
            initiatives = map(lambda g: g.initiative, all_groups)
            sorted_groups = sorted(zip(initiatives, all_groups), reverse=True)
            for _, group in sorted_groups:
                group.attack()

            # Update armies
            immune_system.remove_empty_groups()
            infection.remove_empty_groups()

        if immune_system.contains_units():
            boost_max = boost
        else:
            boost_min = boost

        if boost_max == boost_min:
            print(immune_system.total_units)
            break

