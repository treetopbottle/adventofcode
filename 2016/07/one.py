#!/usr/bin/env python3

import fileinput


# Help functions

def debug(s):
    pass


def abba(s):
    for i in range(1, len(s)-2):
        if s[i] == s[i+1] and s[i-1] == s[i+2] and s[i-1] != s[i]:
            return True
    return False

def tls(ip):
    parts = ip.replace('[',']').split(']')
    goods = range(0, len(parts), 2)
    brackets = range(1, len(parts), 2)

    in_good = False
    for g in goods:
        in_good |= abba(parts[g])

    in_bracket = False
    for b in brackets:
        in_bracket |= abba(parts[b])

    return in_good and not in_bracket


# Handle input

supporting_lines = 0
for line in fileinput.input():
    if tls(line):
        supporting_lines += 1
        # DEBUGGING
        debug(line)

print(supporting_lines)

fileinput.close()

