#!/usr/bin/env python3

import sys
import collections
import re
import functools

file_name = sys.argv[1]


def get_knot_hash(input_lengths):
    input_lengths = [ord(i) for i in input_lengths] + [17, 31, 73, 47, 23]

    numbers = list(range(5))
    numbers = list(range(256))

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

            # update vars
            cur_pos = (cur_pos + length + skip) % len(numbers)
            skip += 1

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

    return hex_string


with open(file_name) as f:
    input_ = f.readlines()
    input_ = 'xlqgujun'
    #input_ = 'a0c2017'
    #input_ = 'flqrgnkx'


    grid = ''

    for i in range(128):
        key = input_ + '-' + str(i)
        print(key)
        knot_hash = get_knot_hash(key)
        print(knot_hash)
        for hex_char in knot_hash:
            grid += '{:0>4b}'.format(int(hex_char, 16))
        grid += '\n'

    print(grid.count('1'))
    #lines = grid.split('\n')
    #print(len(lines))
    #print('--')
    #for l in lines:
    #    print(len(l))
    #print(grid)
    #row = ''
    #for i in input_:
    #    num = int(i, 16)
    #    row += '{:0>4b}'.format(num)

    #print(row) 
