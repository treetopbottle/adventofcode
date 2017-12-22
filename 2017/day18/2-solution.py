#!/usr/bin/env python3

import sys
import collections


def run_progam(instructions, registers, message_bus):
    instruction = instructions[registers['instruction']].strip()
    op, *args = instruction.split(' ')
    print(op, args)

    done = False

    if op == 'snd':
        registers['last_played'] = registers[args[0]]

    elif op == 'set':
        if args[1] in registers:
            val = registers[args[1]]
        else:
            val = int(args[1])

        registers[args[0]] = val

    elif op == 'add':
        if args[1] in registers:
            val = registers[args[1]]
        else:
            val = int(args[1])

        registers[args[0]] += val

    elif op == 'mul':
        if args[1] in registers:
            val = registers[args[1]]
        else:
            val = int(args[1])

        registers[args[0]] *= val

    elif op == 'mod':
        if args[1] in registers:
            val = registers[args[1]]
        else:
            val = int(args[1])

        registers[args[0]] %= val

    elif op == 'rcv':
        if registers[args[0]] != 0:
            print('recover', registers['last_played'])
            done = True

    elif op == 'jgz':
        if registers[args[0]] > 0:
            registers['instruction'] += int(args[1])
            registers['instruction'] -= 1

    registers['instruction'] += 1

    return done


file_name = sys.argv[1]

with open(file_name) as f:
    instructions = f.readlines()

    registers = collections.defaultdict(int)
    last_played_frequency = 0

    done = False
    registers['instruction'] = 0
    while not done:
        done = run_progam(instructions, registers, [])

