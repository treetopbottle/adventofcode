#!/usr/bin/env python3

with open('input') as f:
    numbers = list(map(int, f.read().strip().split(' ')))


# node: ((a,b),[],value)
VALUE_INDEX = 2


def parse_node(numbers):
    nr_children, nr_metadata, *rest = numbers

    children = []
    for _ in range(nr_children):
        child, rest = parse_node(rest)
        children.append(child)
    
    metadata = rest[:nr_metadata]
    rest = rest[nr_metadata:]

    value = 0
    if nr_children == 0:
        value = sum(metadata)
    else:
        for child_index in metadata:
            i = child_index - 1
            if i >= 0 and i < len(children):
                value += children[i][VALUE_INDEX]

    node = ((nr_children, nr_metadata), children, value)
    return (node, rest)


tree, left_over = parse_node(numbers)
print(tree[VALUE_INDEX])

