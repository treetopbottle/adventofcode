#!/usr/bin/env python3

from collections import defaultdict

def get_squares(claim):
    id_, rest = claim[1:].split(' @ ')
    location, size = rest.split(': ')
    x, y = [int(i) for i in location.split(',')]
    width, height = [int(i) for i in size.split('x')]
    squares = []
    for i in range(x, x+width):
        for j in range(y, y+height):
            squares.append((i,j))
    return squares

with open('input') as f:
    claims = f.readlines()

    claimed_squares = set()
    overlapping_squares = set()
    for claim in claims:
        squares = get_squares(claim)
        for square in squares:
            if square in claimed_squares:
                overlapping_squares.add(square)
            claimed_squares.add(square)

    print(len(overlapping_squares))
