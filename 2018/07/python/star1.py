#!/usr/bin/env python

from collections import defaultdict
import itertools

with open('input') as f:
    lines = f.read().splitlines()

letters = set()
requirements = defaultdict(list)
for line in lines:
    words = line.split(' ')
    before = words[1]
    other = words[7]
    requirements[before].append(other)
    letters.add(before)
    letters.add(other)


order = ''
while len(letters) > 0:
    for letter in sorted(letters):
        not_unlocked = list(itertools.chain(*requirements.values()))
        if letter not in not_unlocked:
            order += letter
            if letter in requirements:
                requirements.pop(letter)
            break
    letters.remove(order[-1])

print(order)
