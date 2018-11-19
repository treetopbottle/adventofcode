#!/usr/bin/env python3

import fileinput

legal_triangles = 0

lines = list(fileinput.input())
nr_lines = len(lines)

for i in range(0, nr_lines, 3):
    v1 = [int(i) for i in lines[i+0].split()]
    v2 = [int(i) for i in lines[i+1].split()]
    v3 = [int(i) for i in lines[i+2].split()]

    l1 = sorted([v1[0], v2[0], v3[0]])
    l2 = sorted([v1[1], v2[1], v3[1]])
    l3 = sorted([v1[2], v2[2], v3[2]])

    if l1[0] + l1[1] > l1[2]:
        legal_triangles += 1
    if l2[0] + l2[1] > l2[2]:
        legal_triangles += 1
    if l3[0] + l3[1] > l3[2]:
        legal_triangles += 1


print(legal_triangles)

fileinput.close()


