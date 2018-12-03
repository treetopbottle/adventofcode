#!/usr/bin/env python3

current_frequency = 0
seen_frequencies = set()


with open('input') as f:
    lines = f.readlines()
    def lines_loop():
        while True:
            for line in lines:
                yield line

    def get_change(line):
        number = int(line[1:], 10)
        if line[0] == '-':
             return number * -1
        return number

    for line in lines_loop():
        seen_frequencies.add(current_frequency)
        current_frequency += get_change(line)
        if current_frequency in seen_frequencies:
            print(current_frequency)
            break

