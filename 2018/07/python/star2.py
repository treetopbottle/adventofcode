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


NR_WORKERS = 5
MIN_WORK_TIME = 61

time = 0
workers = sorted([])
free_letters = sorted([l for l in letters if not l in locked_by.keys()])

while free_letters or workers:
    # Start work
    if free_letters and len(workers) < NR_WORKERS:
        next_letter = free_letters.pop(0)
        finish_time = time + MIN_WORK_TIME + (ord(next_letter) - ord('A'))
        workers = sorted(workers + [(finish_time, next_letter)])
        continue

    # Finish work
    (finish_time, finished_letter) = workers.pop(0)
    print('finished {} at {}'.format(finished_letter, finish_time))
    time = finish_time
    
    # Free letters
    for locked_letter in locking[finished_letter]:
        locked_by[locked_letter].remove(finished_letter)
        if not locked_by[locked_letter]:
            free_letters = sorted(free_letters + [locked_letter])

print(time)

