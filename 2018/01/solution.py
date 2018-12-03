#!/usr/bin/env python3

result = 0

with open('input') as f:
    lines = f.readlines()
    for line in lines:
        number = int(line[1:], 10)
        if line[0] == '+':
            result += number
        else:
            result -= number

print(result)
