#!/usr/bin/env python3

with open('input1') as f:
    input1 = f.read()
    input1 = input1.strip()

    sum_ = 0

    input_length = len(input1)
    for i in range(input_length):
        index_half_way = (int)((input_length / 2) + i) % input_length
        if input1[i] == input1[index_half_way]:
            sum_ += int(input1[i])

    print(sum_)

