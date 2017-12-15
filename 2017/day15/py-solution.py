#!/usr/bin/env python3

import sys
import collections
import re
import functools

file_name = sys.argv[1]


def next_value(val, factor):
    return (val * factor) % 2147483647


with open(file_name) as f:
    a_val = 703
    b_val = 516
    #a_val = 65
    #b_val = 8921

    nr_matches = 0
    for i in range(int(40e6)):
        a_val = next_value(a_val, 16807)
        b_val = next_value(b_val, 48271)
        a_bin = '{:0>32b}'.format(a_val)
        b_bin = '{:0>32b}'.format(b_val)
        if a_bin[-16:] == b_bin[-16:]:
            nr_matches += 1

    print(nr_matches)

