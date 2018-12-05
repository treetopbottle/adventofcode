#!/usr/bin/env python3


def react(polymer):
    for i in range(len(polymer) - 1):
        unit1 = polymer[i]
        unit2 = polymer[i+1]
        if (unit1.islower() and unit2.isupper()) \
            or (unit1.isupper() and unit2.islower()):
            if unit1.lower() == unit2.lower():
                return polymer[:i] + polymer[i+2:]
    return polymer


with open('input') as f:
    polymer = f.readlines()[0].strip()


old = None
new = polymer
while not old == new:
    old = new
    new = react(old)


print(len(new))
