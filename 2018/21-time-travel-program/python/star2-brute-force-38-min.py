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


function_dict = {
    'addr': addr,
    'addi': addi,
    'mulr': mulr,
    'muli': muli,
    'banr': banr,
    'bani': bani,
    'borr': borr,
    'bori': bori,
    'setr': setr,
    'seti': seti,
    'gtir': gtir,
    'gtri': gtri,
    'gtrr': gtrr,
    'eqir': eqir,
    'eqri': eqri,
    'eqrr': eqrr,
}


ip_reg = 0
program = []
with open("input") as lines:
    ip_reg = int(next(lines).strip()[-1])
    for line in lines:
        opcode, *ints = line.split()
        a, b, c = [int(i) for i in ints]
        program.append((opcode, a, b, c))

seen_register_4 = []

registers = [0, 0, 0, 0, 0, 0]
while (0 <= registers[ip_reg] < len(program)):
    instr_nr = registers[ip_reg]
    opcode, a, b, c = program[instr_nr]
    function_dict[opcode](a, b, c, registers)
    # The comparison is done on line 28 between r0 and r4
    if registers[ip_reg] == 28:
        # Find the last value before a loop occurs
        if registers[4] in seen_register_4:
            print(seen_register_4[-1])
            break

        seen_register_4.append(registers[4])
    registers[ip_reg] += 1


#r0, r1, r2, r3, r4, r5 = registers
#r4 = 0
#while True:
#    r1 = r4 | 65536
#    r4 = 16031208
#    while True:
#        r1 = r4 | 65536
#        r4 = r4 + r3
#        r4 = r4 & 16777215
#        r4 = 4 * 65899
#        r4 = r4 & 16777215
#    
