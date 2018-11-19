#!/usr/bin/env python3

import fileinput
import re


# Help functions

def debug(s):
    pass


def aba(s):
    matches = []
    for i in range(1, len(s)-1):
        if s[i-1] == s[i+1] and s[i-1] != s[i]:
            matches.append(s[i-1:i+2])
    return matches

def has_bab(s, bab):
    return re.search(bab, s) != None

def tls(ip):
    parts = ip.replace('[',']').split(']')
    goods = range(0, len(parts), 2)
    brackets = range(1, len(parts), 2)

    abas = []
    for g in goods:
        abas.extend(aba(parts[g]))

    aba_and_bab = False
    for b in brackets:
        for a in abas:
            bab = a[1:] + a[1]
            aba_and_bab |= has_bab(parts[b], bab)

    return aba_and_bab


# Handle input

supporting_lines = 0
for line in fileinput.input():
    if tls(line):
        supporting_lines += 1
        # DEBUGGING
        debug(line)

print(supporting_lines)

fileinput.close()

