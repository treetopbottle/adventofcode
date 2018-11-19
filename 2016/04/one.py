#!/usr/bin/env python3

import fileinput
import collections


# Globals

sector_id_sum = 0


# Helpers

def is_room(letters, checksum):
    occurence = collections.defaultdict(int)
    for letter in letters:
        occurence[letter] += 1
    flipped = sorted([(100-value,key) for (key, value) in occurence.items()])
    expected = ''.join([letter for (number, letter) in flipped][:5])
    return expected == checksum


for line in fileinput.input():
    rest = line[:-8].split('-')
    letters = ''.join(rest[:-1])
    sector_id = int(rest[-1])
    checksum = line[-7:-2]

    if is_room(letters, checksum):
        sector_id_sum += sector_id


print(sector_id_sum)

fileinput.close()


