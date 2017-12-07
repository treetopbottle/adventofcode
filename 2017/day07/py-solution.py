#!/usr/bin/env python3

import sys
import collections
import re

file_name = sys.argv[1]

with open(file_name) as f:
    input_ = f.readlines()
    lines = [i.strip() for i in input_]

    pointed_to = []
    program_weights = {}
    for program in lines:
        carries = None
        try:
            program, carries = program.split('->')
        except ValueError:
            pass

        name, weight = program.strip().split(' ')
        weight = weight[1:-1]
        program_weights[name] = weight

        if carries:
            carries = carries.strip().split(',')
            carries = [i.strip() for i in carries]
            pointed_to.extend(carries)


    print(pointed_to)
    for p in program_weights.keys():
        if p not in pointed_to:
            print(p)
