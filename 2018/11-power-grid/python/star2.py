#!/usr/bin/env python3


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
for x in range(1,301):
    for y in range(1,301):
        fuel_cell_grid[(x, y)] = get_power(x, y, grid_serial_number)

topleftsize = (-1, -1, -1)
highest = -1000
for s in range(10, 20):
    for x in range(1, 302-s):
        for y in range(1, 302-s):
            square_power = 0
            for i in range(0,s):
                for j in range(0,s):
                    square_power += fuel_cell_grid[(x+i, y+j)]
            if square_power > highest:
                highest = square_power
                topleftsize = (x, y, s)

print(highest)
print(topleftsize)
