#!/usr/bin/env python3

import sys
import collections
import copy


def state_A(tape, cursor):
    if tape[cursor] == 0:
        tape[cursor] = 1
        return 'B', cursor + 1
    else:
        tape[cursor] = 0
        return 'C', cursor - 1


def state_B(tape, cursor):
    if tape[cursor] == 0:
        tape[cursor] = 1
        return 'A', cursor - 1
    else:
        tape[cursor] = 1
        return 'A', cursor + 1


def state_C(tape, cursor):
    if tape[cursor] == 0:
        tape[cursor] = 0
        return 'B', cursor - 1
    else:
        tape[cursor] = 0
        return 'E', cursor - 1


def state_D(tape, cursor):
    if tape[cursor] == 0:
        tape[cursor] = 1
        return 'A', cursor + 1
    else:
        tape[cursor] = 0
        return 'B', cursor + 1


def state_E(tape, cursor):
    if tape[cursor] == 0:
        tape[cursor] = 1
        return 'F', cursor - 1
    else:
        tape[cursor] = 1
        return 'C', cursor - 1


def state_F(tape, cursor):
    if tape[cursor] == 0:
        tape[cursor] = 1
        return 'D', cursor + 1
    else:
        tape[cursor] = 1
        return 'A', cursor + 1


def simulate(state, tape, cursor):
    if state == 'A':
        return state_A(tape, cursor)
    elif state == 'B':
        return state_B(tape, cursor)
    elif state == 'C':
        return state_C(tape, cursor)
    elif state == 'D':
        return state_D(tape, cursor)
    elif state == 'E':
        return state_E(tape, cursor)
    elif state == 'F':
        return state_F(tape, cursor)


file_name = sys.argv[1]
with open(file_name) as f:
    lines = f.readlines()
    
    begin_state = lines.pop(0)
    begin_state = begin_state[-3]
    nr_steps = lines.pop(0).strip().split(' ')
    nr_steps = int(nr_steps[-2])

    print('begin', begin_state)
    print('steps', nr_steps)

    tape = collections.defaultdict(int)
    cursor = 0
    state = begin_state
    for i in range(nr_steps):
        if i % 1000000 == 0:
            print(i)
        #print(tape)
        state, cursor = simulate(state, tape, cursor)

    print('checksum:', sum(tape.values()))


