#!/usr/bin/env python3

import sys
import collections


file_name = sys.argv[1]

with open(file_name) as f:
    instructions = f.readlines()

    registers = collections.defaultdict(int)
    last_played_frequency = 0

    done = False
    i = 0
    while not done:
        instruction = instructions[i].strip()
        op, *args = instruction.split(' ')
        print(op, args)

        if op == 'snd':
            last_played_frequency = registers[args[0]]
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
                print('recover', last_played_frequency)
                done = True

        elif op == 'jgz':
            if registers[args[0]] > 0:
                i += int(args[1])
                i -= 1

        i += 1

    print('---')
    print(last_played_frequency)
