#!/usr/bin/env python3

import sys
import collections
import copy


def parse(lines):
    actions = {}
    while len(lines) > 0:
        _ = lines.pop(0)
        state = lines.pop(0)[-3]
        # first value
        value = int(lines.pop(0)[-3])
        new_value = int(lines.pop(0)[-3])
        direction = lines.pop(0).split(' ')[-1][:-2]
        if direction == 'right':
            direction = 1
        else:
            direction = -1
        new_state = lines.pop(0)[-3]
        actions[(state, value)] = (new_value, direction, new_state)
        # second value
        value = int(lines.pop(0)[-3])
        new_value = int(lines.pop(0)[-3])
        direction = lines.pop(0).split(' ')[-1][:-2]
        if direction == 'right':
            direction = 1
        else:
            direction = -1
        new_state = lines.pop(0)[-3]
        actions[(state, value)] = (new_value, direction, new_state)
    return actions


def simulate(actions, state, tape, cursor):
    current_value = tape[cursor]
    new_value, offset, new_state = actions[(state, current_value)]
    tape[cursor] = new_value

    return cursor + offset, new_state


file_name = sys.argv[1]
with open(file_name) as f:
    lines = f.readlines()
    
    begin_state = lines.pop(0)
    begin_state = begin_state[-3]

    nr_steps = lines.pop(0).strip().split(' ')
    nr_steps = int(nr_steps[-2])

    actions = parse(lines)

    tape = collections.defaultdict(int)
    cursor = 0
    state = begin_state
    for i in range(nr_steps):
        if i % 1000000 == 0:
            print('step', i)
        cursor, state = simulate(actions, state, tape, cursor)

    print('checksum:', sum(tape.values()))


