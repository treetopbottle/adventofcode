#!/usr/bin/env python3


from collections import defaultdict


def get_power(x, y, serial_number):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += serial_number
    power_level *= rack_id
    hundred_digit = (power_level // 100) % 10
    return hundred_digit - 5


# puzzle input
grid_serial_number = 8444

fuel_cell_grid = {}
summed_area_table = defaultdict(int)
for x in range(1, 301):
    for y in range(1, 301):
        fuel_cell_grid[(x, y)] = get_power(x, y, grid_serial_number)
        summed_area_table[(x, y)] = fuel_cell_grid[(x, y)] + \
            summed_area_table[(x-1, y  )] + \
            summed_area_table[(x  , y-1)] - \
            summed_area_table[(x-1, y-1)]


topleftsize = (-1, -1, -1)
highest = -1000
for s in range(1, 301):
    for x in range(s, 301):
        for y in range(s, 301):
            square_power = summed_area_table[(x, y)] + \
                summed_area_table[(x-s, y-s)] - \
                summed_area_table[(x-s, y  )] - \
                summed_area_table[(x  , y-s)]
            if square_power > highest:
                highest = square_power
                topleftsize = (x-s+1, y-s+1, s)

print(highest)
print(topleftsize)
