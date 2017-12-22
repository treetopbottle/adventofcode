#!/usr/bin/env python3

import sys
import collections


def visualize_grid(infected, grid_size):
    for y in range(grid_size, -1*grid_size + 1, -1):
        for x in range(-1*grid_size + 1, grid_size):
            if infected_nodes[x,y]:
                print('#', end='')
            else:
                print('.', end='')
        print()


file_name = sys.argv[1]

with open(file_name) as f:
    grid = f.readlines()
    #grid = ['..#\n', '#..\n', '...\n']

    infected_nodes = collections.defaultdict(bool)

    nr_bursts = 10000
    nr_bursts_cause_infection = 0

    # determine infected nodes
    grid_size = len(grid)
    y = int((grid_size-1) / 2)
    for line in grid:
        x = int((grid_size-1) / 2 * -1)
        for node in line.strip():
            if node == '#':
                infected_nodes[x,y] = True
            elif node == '.':
                pass
            else:
                raise ValueError('not # or . node, but "{0}"'.format(node))
            x += 1
        y -= 1

    nr_start_infected = list(infected_nodes.values()).count(True)

    dir_x, dir_y = 0,1
    x,y = 0,0
    for i in range(nr_bursts):
        if infected_nodes[x,y]:
            # turn right
            if dir_x == 0:
                dir_x, dir_y = dir_y, 0
            else:
                dir_x, dir_y = 0, -1*dir_x
        else:
            # turn left
            if dir_x == 0:
                dir_x, dir_y = -1*dir_y, 0
            else:
                dir_x, dir_y = 0, dir_x

        # change node
        infected_nodes[x,y] = not infected_nodes[x,y]

        if (infected_nodes[x,y]):
            nr_bursts_cause_infection += 1

        # move
        x += dir_x
        y += dir_y

        #print(x,y)
        #visualize_grid(infected_nodes, 9)

    nr_infected = list(infected_nodes.values()).count(True)

    visualize_grid(infected_nodes, 40)
    print('----')
    print('extra infected:', nr_infected - nr_start_infected)
    print('(total infected:', nr_infected, ', start:', nr_start_infected, ')')
    print(nr_bursts_cause_infection)


