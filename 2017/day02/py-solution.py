#!/usr/bin/env python3

import sys
file_name = sys.argv[1]

with open(file_name) as f:
    input_ = f.readlines()

    sum_ = 0

    for line in input_:
        line = line.strip()
        numbers = [int(i) for i in line.split('\t')]
        for i in numbers:
            for j in numbers:
                if i == j:
                    continue
                if i % j == 0:
                    print(i,j)
                    sum_ += max(i, j) / min(i,j)

    print(sum_)
