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
            instruction = [int(i) for i in next(lines).strip().split()]
            after = [int(i) for i in next(lines).strip()[9:-1].split(", ")]
            sample = (before, instruction, after)
            samples.append(sample)
        elif len(line) > 1:
            test_program.append([int(i) for i in line.strip().split()])


opcode_operations = {}
while len(opcode_operations) < 16:
    for before, instruction, after in samples:
        matching_operations = []
        for operation in operations:
            opcode, a, b, c = instruction
            registers = before.copy()
            operation(a, b, c, registers)
            if registers == after:
                matching_operations.append((opcode, operation))
        if len(matching_operations) == 1:
            opcode, operation = matching_operations[0]
            opcode_operations[opcode] = operation
            operations.remove(operation)


registers = [0, 0, 0, 0]
for instruction in test_program:
    opcode, a, b, c = instruction
    opcode_operations[opcode](a, b, c, registers)

print(registers[0])
