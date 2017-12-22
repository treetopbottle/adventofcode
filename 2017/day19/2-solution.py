#!/usr/bin/env python3

import sys
import collections


def run_progam(instructions, registers, message_bus):
    next_instruction = registers['instruction']
    if next_instruction >= len(instructions):
        return

    instruction = instructions[next_instruction].strip()
    op, *args = instruction.split(' ')
    print(op, args)

    message = None

    if op == 'snd':
        if args[0] in registers:
            val = registers[args[0]]
        else:
            val = int(args[0])

        message = val

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
        if len(message_bus) > 0:
            val = message_bus.pop(0)
            registers[args[0]] = val
        else:
            message = 'deadlock'
            registers['instruction'] -= 1

    elif op == 'jgz':
        if args[1] in registers:
            val = registers[args[1]]
        else:
            val = int(args[1])

        if registers[args[0]] > 0:
            registers['instruction'] += val
            registers['instruction'] -= 1

    registers['instruction'] += 1

    return message


file_name = sys.argv[1]

with open(file_name) as f:
    instructions = f.readlines()

    done = False
    registers0 = collections.defaultdict(int)
    registers0['instruction'] = 0
    registers0['p'] = 0
    messages0 = []

    registers1 = collections.defaultdict(int)
    registers1['instruction'] = 0
    registers1['p'] = 1
    messages1 = []

    program1_sent_nr = 0
    program0_sent_nr = 0
    deadlock = False
    while not deadlock:
        message_for1 = run_progam(instructions, registers0, messages0)
        message_for0 = run_progam(instructions, registers1, messages1)

        if message_for0 != None and message_for0 != 'deadlock':
            program1_sent_nr += 1
            messages0.append(message_for0)

        while message_for0 != 'deadlock':
            message_for0 = run_progam(instructions, registers1, messages1)

            if message_for0 != None and message_for0 != 'deadlock':
                program1_sent_nr += 1
                messages0.append(message_for0)

        if message_for1 != None and message_for1 != 'deadlock':
            program0_sent_nr += 1
            messages1.append(message_for1)

        print(registers0, messages0)
        print(registers1, messages1)
        if message_for0 == 'deadlock' and message_for1 == 'deadlock':
            deadlock = True

    print(program0_sent_nr)
    print(program1_sent_nr)
