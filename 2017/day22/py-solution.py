#!/usr/bin/env python3

import sys
import collections


def visualize_grid(infected, grid_size):
    for y in range(grid_size, -1*grid_size + 1, -1):
        for x in range(-1*grid_size + 1, grid_size):
            print(infected_nodes[x,y], end='')
        print()


file_name = sys.argv[1]

with open(file_name) as f:
    grid = f.readlines()
    #grid = ['..#\n', '#..\n', '...\n']

    infected_nodes = collections.defaultdict(lambda: '.')

    nr_bursts = 10000000
    nr_bursts_cause_infection = 0

    # determine infected nodes
    grid_size = len(grid)
    y = int((grid_size-1) / 2)
    for line in grid:
        x = int((grid_size-1) / 2 * -1)
        for node in line.strip():
            if node == '#':
                infected_nodes[x,y] = '#'
            elif node == '.':
                pass
            else:
                raise ValueError('not # or . node, but "{0}"'.format(node))
            x += 1
        y -= 1

    dir_x, dir_y = 0,1
    x,y = 0,0
    for i in range(nr_bursts):
        if infected_nodes[x,y] == '#':
            # turn right
            if dir_x == 0:
                dir_x, dir_y = dir_y, 0
            else:
                dir_x, dir_y = 0, -1*dir_x

            # flag infected
            infected_nodes[x,y] = 'F'

        elif infected_nodes[x,y] == 'W':
            # don't turn

            # infect weakened
            infected_nodes[x,y] = '#'

        elif infected_nodes[x,y] == '.':
            # turn left
            if dir_x == 0:
                dir_x, dir_y = -1*dir_y, 0
            else:
                dir_x, dir_y = 0, dir_x

            # weaken clean
            infected_nodes[x,y] = 'W'

        elif infected_nodes[x,y] == 'F':
            # reverse direction
            dir_x, dir_y = -1*dir_x, -1*dir_y

            # clean flagged
            infected_nodes[x,y] = '.'

        else:
            raise ValueError('wtf is happening')

        if (infected_nodes[x,y] == '#'):
            nr_bursts_cause_infection += 1

        # move
        x += dir_x
        y += dir_y

        #print(x,y)
        #visualize_grid(infected_nodes, 9)

    visualize_grid(infected_nodes, 40)
    print('----')
    print(nr_bursts_cause_infection)


