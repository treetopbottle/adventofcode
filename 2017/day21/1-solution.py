#!/usr/bin/env python3

import sys
import collections
import string
import itertools


# For rotation: https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python


def translate(block, rewrite_rules):
    new_block_str = None
    nr_rotations = 4
    nr_flips = 2
    for i in range(nr_rotations):
        for f in range(nr_flips):
            flipped_block = block
            if f > 0:
                flipped_block = block[::-1]
            rotated_block = flipped_block
            for _ in range(i):
                rotated_block = [list(x) for x in zip(*reversed(rotated_block))]
            str_block = '/'.join([''.join(b) for b in rotated_block])
            if str_block in rewrite_rules:
                new_block_str = rewrite_rules[str_block]
                break
        if new_block_str:
            break

    if new_block_str == None:
        raise ValueError('Could not translate block')

    new_block = [list(b) for b in new_block_str.split('/')]

    return new_block


def process(canvas, block_size, rewrite_rules):
    nr_blocks = len(canvas) // block_size
    new_size = nr_blocks * (block_size + 1)
    new_canvas = []
    for i in range(new_size):
        new_canvas.append([])

    new_blocks = []
    size = len(canvas)
    for i in range(size // block_size):
        for j in range(size // block_size):
            block = [b[j*block_size:(j+1)*block_size] for b in canvas[i*block_size:(i+1)*block_size]]
            new_block = translate(block, rewrite_rules)

            for k, line in enumerate(new_block):
                new_canvas[k + i*(block_size+1)].extend(line)

    print(new_canvas)
    return new_canvas


NR_ITERATIONS = 5
START_PATTERN = """.#.
..#
###
"""

canvas = [list(i) for i in START_PATTERN.strip().split('\n')]


file_name = sys.argv[1]
with open(file_name) as f:
    input_ = f.readlines()

    rewrite_rules = {}
    for line in input_:
        key, value = line.strip().split(' => ')
        rewrite_rules[key] = value

    for i in range(NR_ITERATIONS):
        size = len(canvas)

        block_size = 0
        if size % 2 == 0:
            block_size = 2
        elif size % 3 == 0:
            block_size = 3
        else:
            raise ValueError('wtf i')

        canvas = process(canvas, block_size, rewrite_rules)

        print(list(itertools.chain(*canvas)).count('#'))
