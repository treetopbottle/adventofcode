#!/usr/bin/env python3

import sys
import collections
import re

file_name = sys.argv[1]

with open(file_name) as f:
    input_ = f.readlines()
    
    for cnt, line in enumerate(input_):
        total_score = 0
        group_score = 0
        garbage_started = False
        ignore_next = False
        garbage_removed = 0
        for char in line:
            # new group
            if ignore_next:
                ignore_next = False
                pass
            elif char == '!':
                ignore_next = True
            elif garbage_started and not char == '>':
                garbage_removed += 1
                pass
            elif char == '<':
                garbage_started = True
            elif char == '>':
                garbage_started = False
            elif char == '{':
                group_score += 1
            elif char == '}':
                total_score += group_score
                group_score -= 1
            else:
                pass
            #print(char)

        print('line', str(cnt+1) + ':', garbage_removed)

