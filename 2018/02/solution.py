#!/usr/bin/env python3

from collections import defaultdict

def get_nr_different_characters(id1, id2):
    different_characters = 0
    for i in range(len(id1)):
        if not id1[i] == id2[i]:
            different_characters += 1
    return different_characters

def get_correct_box_ids(lines):
    for box_id1 in lines:
        for box_id2 in lines:
            difference = get_nr_different_characters(box_id1, box_id2)
            if difference == 1:
                return [box_id1, box_id2]

with open('input') as f:
    lines = f.readlines()
    id1, id2 = get_correct_box_ids(lines)

    # Print matching characters
    for i in range(len(id1)):
        if id1[i] == id2[i]:
            print(id1[i], end='')

