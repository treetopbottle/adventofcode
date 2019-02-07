#!/usr/bin/env python3


def addr(a, b, c, registers):
    registers[c] = registers[a] + registers[b]


def addi(a, b, c, registers):
    registers[c] = registers[a] + b


def mulr(a, b, c, registers):
    registers[c] = registers[a] * registers[b]


def muli(a, b, c, registers):
    registers[c] = registers[a] * b


def banr(a, b, c, registers):
    registers[c] = registers[a] & registers[b]


def bani(a, b, c, registers):
    registers[c] = registers[a] & b


def borr(a, b, c, registers):
    registers[c] = registers[a] | registers[b]


def bori(a, b, c, registers):
    registers[c] = registers[a] | b


def setr(a, b, c, registers):
    registers[c] = registers[a]


def seti(a, b, c, registers):
    registers[c] = a


def gtir(a, b, c, registers):
    if a > registers[b]:
        registers[c] = 1
    else:
        registers[c] = 0


def gtri(a, b, c, registers):
    if registers[a] > b:
        registers[c] = 1
    else:
        registers[c] = 0


def gtrr(a, b, c, registers):
    if registers[a] > registers[b]:
        registers[c] = 1
    else:
        registers[c] = 0


def eqir(a, b, c, registers):
    if a == registers[b]:
        registers[c] = 1
    else:
        registers[c] = 0


def eqri(a, b, c, registers):
    if registers[a] == b:
        registers[c] = 1
    else:
        registers[c] = 0


def eqrr(a, b, c, registers):
    if registers[a] == registers[b]:
        registers[c] = 1
    else:
        registers[c] = 0


operations = [
    addr,
    addi,
    mulr,
    muli,
    banr,
    bani,
    borr,
    bori,
    setr,
    seti,
    gtir,
    gtri,
    gtrr,
    eqir,
    eqri,
    eqrr,
]


samples = []
test_program = []
with open("input") as lines:
    for line in lines:
        if line.startswith("Before"):
            before = [int(i) for i in line.strip()[9:-1].split(", ")]
            opcode = [int(i) for i in next(lines).strip().split()]
            after = [int(i) for i in next(lines).strip()[9:-1].split(", ")]
            sample = (before, opcode, after)
            samples.append(sample)
        elif len(line) > 1:
            test_program.append(line.strip())


more_than_three_opcodes = 0
for before, opcode, after in samples:
    nr_opcodes = 0
    for operation in operations:
        _, a, b, c = opcode
        registers = before.copy()
        operation(a, b, c, registers)
        if registers == after:
            nr_opcodes += 1
    if nr_opcodes >= 3:
        more_than_three_opcodes += 1

print(more_than_three_opcodes)
