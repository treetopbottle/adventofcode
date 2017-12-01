#!/usr/bin/env python3

with open('input1') as f:
    input1 = f.read()
    input1 = input1.strip()

    sum_ = 0

    for i in range(len(input1)):
        if input1[i] == input1[(i+1) % len(input1)]:
            sum_ += int(input1[i])

    print(sum_)

