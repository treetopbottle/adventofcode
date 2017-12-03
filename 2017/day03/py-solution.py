#!/usr/bin/env python3

import sys
import collections

file_name = sys.argv[1]

with open(file_name) as f:
    nr = int(f.read().strip())

    location = [0,0]

    values = collections.defaultdict(int)
    values[(0,0)] = 1

    current_nr = 1
    stop = 1
    while True:
        # right
        for i in range(stop):
            location[1] += 1
            values[tuple(location)] = \
                values[(location[0],   location[1]+1)] + \
                values[(location[0]+1, location[1]+1)] + \
                values[(location[0]+1, location[1])] + \
                values[(location[0]+1, location[1]-1)] + \
                values[(location[0],   location[1]-1)] + \
                values[(location[0]-1, location[1]-1)] + \
                values[(location[0]-1, location[1])] + \
                values[(location[0]-1, location[1]+1)]
            if values[tuple(location)] > nr:
                print(values[tuple(location)])
                import sys; sys.exit(0)
            current_nr += 1
            print(values[tuple(location)])

        # up
        for i in range(stop):
            location[0] += 1
            values[tuple(location)] = \
                values[(location[0],   location[1]+1)] + \
                values[(location[0]+1, location[1]+1)] + \
                values[(location[0]+1, location[1])] + \
                values[(location[0]+1, location[1]-1)] + \
                values[(location[0],   location[1]-1)] + \
                values[(location[0]-1, location[1]-1)] + \
                values[(location[0]-1, location[1])] + \
                values[(location[0]-1, location[1]+1)]
            if values[tuple(location)] > nr:
                print(values[tuple(location)])
                import sys; sys.exit(0)
            current_nr += 1
            print(values[tuple(location)])

        stop += 1

        # left
        for i in range(stop):
            location[1] -= 1
            values[tuple(location)] = \
                values[(location[0],   location[1]+1)] + \
                values[(location[0]+1, location[1]+1)] + \
                values[(location[0]+1, location[1])] + \
                values[(location[0]+1, location[1]-1)] + \
                values[(location[0],   location[1]-1)] + \
                values[(location[0]-1, location[1]-1)] + \
                values[(location[0]-1, location[1])] + \
                values[(location[0]-1, location[1]+1)]
            if values[tuple(location)] > nr:
                print(values[tuple(location)])
                import sys; sys.exit(0)
            current_nr += 1
            print(values[tuple(location)])

        # down
        for i in range(stop):
            location[0] -= 1
            values[tuple(location)] = \
                values[(location[0],   location[1]+1)] + \
                values[(location[0]+1, location[1]+1)] + \
                values[(location[0]+1, location[1])] + \
                values[(location[0]+1, location[1]-1)] + \
                values[(location[0],   location[1]-1)] + \
                values[(location[0]-1, location[1]-1)] + \
                values[(location[0]-1, location[1])] + \
                values[(location[0]-1, location[1]+1)]
            if values[tuple(location)] > nr:
                print(values[tuple(location)])
                import sys; sys.exit(0)
            current_nr += 1
            print(values[tuple(location)])

        stop += 1


