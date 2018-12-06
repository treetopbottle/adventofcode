#!/usr/bin/env python3

def lines_loop():
    while True:
        for line in lines:
            yield line


with open('input') as f:
    lines = f.readlines()

frequency_changes = map(int, lines_loop())

frequency = 0
seen_frequencies = set()
for change in frequency_changes:
    if frequency in seen_frequencies:
        break
    seen_frequencies.add(frequency)
    frequency += change

print(frequency)

