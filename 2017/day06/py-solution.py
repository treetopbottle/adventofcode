#!/usr/bin/env python3

import sys
import collections
import re

file_name = sys.argv[1]

with open(file_name) as f:
    input_ = f.read().strip()

    memory_banks = [int(i) for i in input_.split('\t')]

    seen_distributions = set()
    wanted_distribution = []

    nr_cycles = 0
    while True:
        # Update seen ones
        distribution = str(memory_banks)
        if distribution in seen_distributions:
            wanted_distribution = distribution
            break
        seen_distributions.add(distribution)

        # Remove memory from max bank
        index = memory_banks.index(max(memory_banks))
        print(index)
        nr_blocks = memory_banks[index]
        memory_banks[index] = 0

        # Redistribute memory
        for i in range(1, nr_blocks+1):
            index = (index+1) % len(memory_banks)
            memory_banks[index] += 1

        nr_cycles += 1

        print(memory_banks, nr_cycles)


    # how long until second?
    print('------------------')
    print(wanted_distribution)

    nr_cycles = 0
    while True:
        # Remove memory from max bank
        index = memory_banks.index(max(memory_banks))
        print(index)
        nr_blocks = memory_banks[index]
        memory_banks[index] = 0

        # Redistribute memory
        for i in range(1, nr_blocks+1):
            index = (index+1) % len(memory_banks)
            memory_banks[index] += 1

        nr_cycles += 1

        distribution = str(memory_banks)
        if distribution == wanted_distribution:
            break

        print(memory_banks, nr_cycles)

    print(nr_cycles)

