#!/usr/bin/env python3

import sys
import collections
import re

file_name = sys.argv[1]

with open(file_name) as f:
    input_ = f.read().strip()
    step_size = 312
    #step_size = 3

    nr_steps = 50000000
    #nr_steps = 10

    buf = [0]
    cur_index = 0
    number_after_zero = 0
    for num in range(1,nr_steps+1):
        buf_size = num
        cur_index = ((cur_index + step_size) % buf_size) + 1

        if cur_index == 1:
            number_after_zero = num
            print('after', number_after_zero)


    print('---')
    print(number_after_zero)

