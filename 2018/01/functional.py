#!/usr/bin/env python3

with open('input') as f:
    lines = f.readlines()

numbers = map(int, lines)
total = sum(numbers)

print(total)

