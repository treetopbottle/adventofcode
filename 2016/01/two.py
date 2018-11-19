#!/usr/bin/env python3
import fileinput

# Data
x,y = 0,0
facing = 0
visited_locations = []


# Helper functions

def north(x,y,d):
    return x+d,y

def east(x,y,d):
    return x,y+d

def south(x,y,d):
    return x-d,y

def west(x,y,d):
    return x,y-d

move_function = [north, east, south, west]

def turn(facing, pivot):
    if pivot == "R":
        facing = (facing + 1) % 4
    elif pivot == "L":
        facing = (facing - 1 + 4) % 4
    return facing

def move(x, y, distance):
    x,y = move_function[facing](x,y,distance)
    return x, y


# Input

line = fileinput.input()[0]
instructions = line.split(',')
instructions = [i.strip() for i in instructions]


# Output

visited_locations.append((x,y))
for i in instructions:
    pivot, distance = i[0], int(i[1:])
    facing = turn(facing, pivot)
    visited = False
    for _ in range(distance):
        x, y = move(x, y, 1)
        if (x,y) in visited_locations:
            print(x,y)
            print(abs(x) + abs(y))
            visited = True
            break
        visited_locations.append((x,y))
    if visited:
        break
else:
    print("not found")

fileinput.close()

