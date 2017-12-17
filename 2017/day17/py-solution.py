#!/usr/bin/env python3

step_size = 312
#step_size = 3

nr_steps = 50000000
#nr_steps = 10

cur_index = 0
number_after_zero = 0
for num in range(1,nr_steps+1):
    cur_index = ((cur_index + step_size) % num) + 1

    if cur_index == 1:
        number_after_zero = num

print(number_after_zero)

