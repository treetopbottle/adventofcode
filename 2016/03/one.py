#!/usr/bin/env python3

import fileinput

legal_triangles = 0

for line in fileinput.input():
    values = sorted([int(i) for i in line.split()])
    print(values)
    if (values[0] + values[1] > values[2]):
        legal_triangles += 1

print(legal_triangles)

fileinput.close()


