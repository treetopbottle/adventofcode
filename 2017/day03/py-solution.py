#!/usr/bin/env python3

import sys
file_name = sys.argv[1]

with open(file_name) as f:
    nr = int(f.read().strip())

    location = [0,0]

    current_nr = 1
    stop = 1
    while True:
        # right
        if current_nr + stop > nr:
            location[1] += nr - current_nr
            #print(location, current_nr, stop)
            break
        location[1] += stop
        current_nr += stop

        #print(location)
        # up
        if current_nr + stop > nr:
            location[0] += nr - current_nr
            #print(location, current_nr, stop)
            break
        location[0] += stop
        current_nr += stop

        stop += 1

        #print(location)
        # left
        if current_nr + stop > nr:
            location[1] -= nr - current_nr
            #print(location, current_nr, stop)
            break
        location[1] -= stop
        current_nr += stop

        #print(location)
        # down
        if current_nr + stop > nr:
            location[0] -= nr - current_nr
            #print(location, current_nr, stop)
            break
        location[0] -= stop
        current_nr += stop

        stop += 1
        #print(location)

    print(abs(location[0]) + abs(location[1]))


