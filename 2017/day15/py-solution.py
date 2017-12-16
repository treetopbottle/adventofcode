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
    nr_comps = 0
    #for i in range(int(40e6)):
    a_comp = []
    b_comp = []
    a_index = 0
    b_index = 0
    while nr_comps < int(5e6):
        a_val = next_value(a_val, 16807)
        b_val = next_value(b_val, 48271)

        if a_val % 4 == 0:
            a_comp.append(a_val)

        if b_val % 8 == 0:
            b_comp.append(b_val)

        if len(a_comp) > a_index and len(b_comp) > b_index:
            a = a_comp[a_index]
            a_index += 1
            b = b_comp[b_index]
            b_index += 1
            nr_comps += 1
            if (a % 2**16) == (b % 2**16):
                nr_matches += 1
                

    print(nr_matches)

