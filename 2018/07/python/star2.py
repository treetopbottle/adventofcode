#!/usr/bin/env python3

from collections import defaultdict
import itertools

with open('input') as f:
    lines = f.read().splitlines()

letters = set()
locked_by = defaultdict(list)
locking = defaultdict(list)
for line in lines:
    words = line.split(' ')
    blocker = words[1]
    blockee = words[7]
    locked_by[blockee].append(blocker)
    locking[blocker].append(blockee)
    letters.add(blockee)
    letters.add(blocker)


workers = []
free_letters = [l for l in letters if not l in locked_by.keys()]

time = 0
while free_letters or workers:
    if free_letters and len(workers) < 5:
        next_letter, *free_letters = sorted(free_letters)
        finish_time = time + 61 + (ord(next_letter) - ord('A'))
        workers.append((finish_time, next_letter))
        continue

    (finish_time, finished_letter) = workers.pop(0)
    print('finished {} at {}'.format(finished_letter, finish_time))
    time = finish_time
    
    for locked_letter in locking[finished_letter]:
        locked_by[locked_letter].remove(finished_letter)
        if not locked_by[locked_letter]:
            free_letters.append(locked_letter)

print(time)

