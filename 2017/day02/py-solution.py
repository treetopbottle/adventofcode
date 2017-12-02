#!/usr/bin/env python3

import sys
file_name = sys.argv[1]

with open(file_name) as f:
    input_ = f.readlines()

    sum_ = 0

    for line in input_:
        line = line.strip()
        numbers = [int(i) for i in line.split('\t')]
        m = int(max(numbers))
        n = int(min(numbers))
        print(m, n)
        sum_ += m - n

    print(sum_)
