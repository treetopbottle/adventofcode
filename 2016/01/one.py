#!/usr/bin/env python3
import fileinput

# globals
x,y = 0,0
facing = 0

def north(x,y,d):
    return x+d,y

def east(x,y,d):
    return x,y+d

def south(x,y,d):
    return x-d,y

def west(x,y,d):
    return x,y-d

move_function = [north, east, south, west]

def move(facing, x, y, turn, distance):
    if turn == "R":
        facing = (facing + 1) % 4
    elif turn == "L":
        facing = (facing - 1 + 4) % 4
    x,y = move_function[facing](x,y,distance)
    return facing, x, y

line = fileinput.input()[0]
instructions = line.split(',')
instructions = [i.strip() for i in instructions]

for i in instructions:
    facing, x, y = move(facing, x, y, i[0], int(i[1:]))

print(x,y)

fileinput.close()

