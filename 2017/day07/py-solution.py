#!/usr/bin/env python3

import sys
import collections
import re

file_name = sys.argv[1]

def get_weight(name, weights, towers):
    w = weights[name]
    if name in towers.keys():
        for other in towers[name]:
            w += get_weight(other, weights, towers)
    return w

with open(file_name) as f:
    input_ = f.readlines()
    lines = [i.strip() for i in input_]

    pointed_to = []
    program_weights = {}
    towers = {}
    for program in lines:
        carries = None
        try:
            program, carries = program.split('->')
        except ValueError:
            pass

        name, weight = program.strip().split(' ')
        weight = int(weight[1:-1])
        program_weights[name] = weight

        if carries:
            carries = carries.strip().split(',')
            carries = [i.strip() for i in carries]
            towers[name] = carries

    total_weight = {}
    for program_name in program_weights.keys():
        total = get_weight(program_name, program_weights, towers)
        total_weight[program_name] = total


    for name in total_weight.keys():
        if name not in towers.keys():
            continue
        carries = towers[name]
        weights = [total_weight[i] for i in carries]
        if not len(set(weights)) == 1:
            print(name, weights)
            print(' ', towers[name])
            print(' ', [total_weight[i] for i in towers[name]])
    print([total_weight[i] for i in towers['ycbgx']])
    print(program_weights['ycbgx'])

