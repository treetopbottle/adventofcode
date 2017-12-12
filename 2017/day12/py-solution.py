#!/usr/bin/env python3

import sys
import collections
import re
import functools

file_name = sys.argv[1]


def extend_group(char, group, comms):
    group.add(char)
    new_chars = comms[char]
    print(group)
    for new_char in new_chars:
        if new_char not in group:
            extend_group(new_char, group, comms)


with open(file_name) as f:
    input_ = f.readlines()

    comms = collections.defaultdict(list)

    for line in input_:
        line = line.strip()

        left, right = line.split('<->')
        right = right.strip().split(',')

        for r in right:
            comms[left.strip()].append(r.strip())

    id0_group = set()
    extend_group('0', id0_group, comms)

    print(sorted(id0_group))
    print('---')
    print(len(id0_group))

