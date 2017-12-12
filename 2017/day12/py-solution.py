#!/usr/bin/env python3

import sys
import collections
import re
import functools

file_name = sys.argv[1]


def extend_group(char, group, comms):
    group.add(char)
    new_chars = comms[char]
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

    all_groups = set()
    for k in comms.keys():
        group = set()
        extend_group(k, group, comms)
        all_groups.add(str(sorted(group)))

    print(sorted(all_groups))
    print('---')
    print(len(all_groups))

