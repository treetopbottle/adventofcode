#!/usr/bin/env python3

from collections import defaultdict

with open('input') as f:
    lines = f.readlines()

    two_occurences = 0
    three_occurences = 0
    for box_id in lines:
        letter_occurences = defaultdict(int)
        for letter in box_id:
            letter_occurences[letter] += 1
        occurences = letter_occurences.values()
        if 2 in occurences:
            two_occurences += 1
        if 3 in occurences:
            three_occurences += 1
    print(two_occurences * three_occurences)
        
