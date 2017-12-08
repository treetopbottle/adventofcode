#!/usr/bin/env python3

import sys
import collections
import re

file_name = sys.argv[1]

with open(file_name) as f:
    input_ = f.readlines()

    registers = collections.defaultdict(int)

    max_amount = 0
    for line in input_:
        line = line.strip()
        if not line:
            continue

        print(line)
        reg, amnt, val, _, reg_condi, operator_condi, val_condi = line.split()

        if operator_condi == '>':
            if registers[reg_condi] > int(val_condi):
                if amnt == 'inc':
                    registers[reg] += int(val)
                elif amnt == 'dec':
                    registers[reg] -= int(val)
        elif operator_condi == '<':
            if registers[reg_condi] < int(val_condi):
                if amnt == 'inc':
                    registers[reg] += int(val)
                elif amnt == 'dec':
                    registers[reg] -= int(val)
        elif operator_condi == '>=':
            if registers[reg_condi] >= int(val_condi):
                if amnt == 'inc':
                    registers[reg] += int(val)
                elif amnt == 'dec':
                    registers[reg] -= int(val)
        elif operator_condi == '<=':
            if registers[reg_condi] <= int(val_condi):
                if amnt == 'inc':
                    registers[reg] += int(val)
                elif amnt == 'dec':
                    registers[reg] -= int(val)
        elif operator_condi == '==':
            if registers[reg_condi] == int(val_condi):
                if amnt == 'inc':
                    registers[reg] += int(val)
                elif amnt == 'dec':
                    registers[reg] -= int(val)
        elif operator_condi == '!=':
            if registers[reg_condi] != int(val_condi):
                if amnt == 'inc':
                    registers[reg] += int(val)
                elif amnt == 'dec':
                    registers[reg] -= int(val)
        print(registers)
        max_amount = max(max_amount, max(registers.values()))
    print(max(registers.values()))
    print(max_amount)

