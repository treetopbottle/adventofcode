#!/usr/bin/env python3

from collections import defaultdict

with open('input') as f:
    records = f.readlines()


def parse(record):
    #month = record[6:8]
    #day = record[9:11]
    #hour = int(record[12:14])
    minute = int(record[15:17])
    action = record[19:]
    return (minute, action)

guard_sleep_time = defaultdict(int)
guard_sleep_minutes = defaultdict(lambda: defaultdict(int))
current_guard = ''
sleep_start = 0
for record in sorted(records):
    minute, action = parse(record)
    if action[0] == 'G':
        current_guard = int(action.split(' ')[1][1:])
    elif action[0] == 'f':
        sleep_start = minute
    elif action[0] == 'w':
        sleep_end = minute
        sleep_time = sleep_end - sleep_start
        guard_sleep_time[current_guard] += sleep_time
        for i in range(sleep_start, sleep_end):
            guard_sleep_minutes[current_guard][i] += 1

best_guard = max(guard_sleep_time, key=guard_sleep_time.get)
sleep_minutes = guard_sleep_minutes[best_guard]
best_minute = max(sleep_minutes, key=sleep_minutes.get)

print(best_guard, best_minute)
print(best_guard * best_minute)


