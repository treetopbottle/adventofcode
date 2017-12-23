#!/usr/bin/env python3

import sys
import collections


def get_number(registers, num):
    if num in registers:
        return registers[num]
    return int(num)


file_name = sys.argv[1]

with open(file_name) as f:
    instructions = f.readlines()

    registers = collections.defaultdict(int)
    registers['a'] = 0
    registers['b'] = 0
    registers['c'] = 0
    registers['d'] = 0
    registers['e'] = 0
    registers['f'] = 0
    registers['g'] = 0
    registers['h'] = 0

    times_mul_invoked = 0

    done = False
    i = 0
    while not done:
        if i >= len(instructions) or i < 0:
            break
        instruction = instructions[i].strip()
        op, *args = instruction.split(' ')
        print(op, args)

        if op == 'set':
            registers[args[0]] = get_number(registers, args[1])
        elif op == 'sub':
            registers[args[0]] -= get_number(registers, args[1])
        elif op == 'mul':
            registers[args[0]] *= get_number(registers, args[1])
            times_mul_invoked += 1
        elif op == 'jnz':
            x = get_number(registers, args[0])
            y = get_number(registers, args[1])
            if x != 0:
                i += y
                i -= 1

        i += 1

    print('---')
    print(times_mul_invoked)
