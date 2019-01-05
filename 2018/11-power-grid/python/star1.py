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

topleft = (-1, -1)
highest = -1000
for x in range(1,298):
    for y in range(1,298):
        square_power = 0
        for i in range(0,3):
            for j in range(0,3):
                square_power += fuel_cell_grid[(x+i, y+j)]
        if square_power > highest:
            highest = square_power
            topleft = (x, y)

print(highest)
print(topleft)
