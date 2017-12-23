#!/usr/bin/env python3

import sys
import collections


def vis(instructions, cur_inst, registers):
    for i in range(len(instructions)):
        if i == cur_inst:
            print('-> ', end='')
        else:
            print('   ', end='')
        print(instructions[i], end='')

    print()

    for reg in registers:
        print(reg, registers[reg])


def get_number(registers, num):
    if num in registers:
        return registers[num]
    return int(num)


file_name = sys.argv[1]

with open(file_name) as f:
    instructions = f.readlines()

    registers = collections.defaultdict(int)
    registers['a'] = 1
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
    cntr = 1
    while not done:
        if i >= len(instructions) or i < 0:
            break
        instruction = instructions[i].strip()
        op, *args = instruction.split(' ')
        #print(op, args)
        import time; time.sleep(0.1)
        vis(instructions, i, registers)
        if cntr % 1000 == 0:
            pass

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
        cntr += 1
