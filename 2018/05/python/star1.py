#!/usr/bin/env python3


with open('input') as f:
    polymer = f.readlines()[0].strip()


i = 0
while i < len(polymer) - 1:
    unit1 = polymer[i]
    unit2 = polymer[i+1]

    different_case = \
        (unit1.islower() and unit2.isupper()) \
        or (unit1.isupper() and unit2.islower())

    if different_case and (unit1.lower() == unit2.lower()):
        polymer = polymer[:i] + polymer[i+2:]
        i = max(i-2, -1)

    i += 1


print(len(polymer))
