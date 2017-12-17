#!/usr/bin/env python3

import sys
import collections
import re

file_name = sys.argv[1]

with open(file_name) as f:
    input_ = f.read().strip()
    step_size = 312
    #step_size = 3

    nr_steps = 2017
    #nr_steps = 5

    buf = [0]
    cur_index = 0
    for num in range(1,nr_steps+1):
        #print(cur_index, step_size, len(buf))
        cur_index = ((cur_index + step_size) % len(buf)) + 1
        #print(cur_index)
        buf.insert(cur_index, num)

        #print(buf)

    i = buf.index(2017)
    print('---')
    print(buf[i-3:i+3])
    next_number = buf[i+1]
    print(next_number)

