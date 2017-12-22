#!/usr/bin/env python3

import sys
import collections
import string


def to_numbers(vector):
    relevant = vector[3:-1]
    separated = relevant.split(',')
    return [int(i) for i in separated]


file_name = sys.argv[1]

with open(file_name) as f:
    lines = f.readlines()

    particles = []
    for line in lines:
        p, v, a = [to_numbers(i) for i in line.strip().split(', ')]
        particles.append((p,v,a))


    change = True
    prev_order = []
    order = []

    while change:
        # move particles
        new_particles = []
        distances = []
        for i, particle in enumerate(particles):
            p, v, a = particle

            v[0] += a[0]
            v[1] += a[1]
            v[2] += a[2]

            p[0] += v[0]
            p[1] += v[1]
            p[2] += v[2]

            new_particles.append((p,v,a))

            distance = abs(p[0]) + abs(p[1]) + abs(p[2])
            distances.append((distance, i))
        particles = new_particles

        order = [i[1] for i in sorted(distances)]
        print(order)
        if order == prev_order:
            change = False

        prev_order = order


print(sorted(distances)[0])

