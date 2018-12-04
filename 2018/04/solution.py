#!/usr/bin/env python3

from collections import defaultdict

with open('sorted_input') as f:
    records = f.readlines()


def parse(record):
    minute = int(record[15:17])
    action = record[19:]
    return (minute, action)

sleep_minutes = defaultdict(int)
current_guard = ''
sleep_start = 0
for record in records:
    minute, action = parse(record)
    if action[0] == 'G':
        current_guard = int(action.split(' ')[1][1:])
    elif action[0] == 'f':
        sleep_start = minute
    elif action[0] == 'w':
        sleep_end = minute
        for i in range(sleep_start, sleep_end):
            key = (current_guard, i)
            sleep_minutes[key] += 1

best_guard, best_minute = max(sleep_minutes, key=sleep_minutes.get)

print(best_guard, best_minute)
print(best_guard * best_minute)


