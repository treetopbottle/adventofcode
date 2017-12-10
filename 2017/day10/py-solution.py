#!/usr/bin/env python3

import sys
import collections
import re
import functools

file_name = sys.argv[1]

with open(file_name) as f:
    input_lengths = f.read().strip()
    input_lengths = [ord(i) for i in input_lengths] + [17, 31, 73, 47, 23]

    numbers = list(range(5))
    numbers = list(range(256))

    print(input_lengths)
    print(numbers)
    print('---')

    skip = 0
    cur_pos = 0
    for _ in range(64):
        for length in input_lengths:
            if length > len(numbers) + 1:
                continue

            # get sublist
            end = cur_pos + length
            to_reverse = numbers[cur_pos:min(end, len(numbers))]
            if end > len(numbers):
                to_reverse += numbers[0:end % len(numbers)]

            # reverse
            to_replace = list(reversed(to_reverse))

            # replace
            for i in range(cur_pos, end):
                numbers[i % len(numbers)] = to_replace[i-cur_pos]

            #print(cur_pos, end)
            #print(to_reverse)
            print(numbers)
            #print(skip)

            # update vars
            cur_pos = (cur_pos + length + skip) % len(numbers)
            skip += 1

    #print(list(sorted(numbers)))

    # dense hash
    sparse_hash = numbers
    dense_hash = []
    for i in range(16):
        n = functools.reduce(lambda x, y: x ^ y, sparse_hash[i*16:i*16+16])
        dense_hash.append(n)

    # to hex
    hex_string = ''
    for i in dense_hash:
        hex_string += format(i, '02x')

    print('----')
    print(hex_string)
    

