#!/usr/bin/env python3

with open('input') as f:
    numbers = list(map(int, f.read().strip().split(' ')))


# node: ((a,b),[],[])


def parse_node(numbers, metadata_sum):
    nr_children, nr_metadata, *rest = numbers

    children = []
    for _ in range(nr_children):
        child, rest, metadata_sum = parse_node(rest, metadata_sum)
        children.append(child)
    
    metadata = rest[:nr_metadata]
    metadata_sum += sum(metadata)
    rest = rest[nr_metadata:]

    node = ((nr_children, nr_metadata), children, metadata)
    return (node, rest, metadata_sum)


tree, left_over, metadata_sum = parse_node(numbers, 0)
print(metadata_sum)

