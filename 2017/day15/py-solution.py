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
    #for i in range(5):
        a_val = next_value(a_val, 16807)
        b_val = next_value(b_val, 48271)
        if (a_val % 2**16) == (b_val % 2**16):
            nr_matches += 1

    print(nr_matches)

