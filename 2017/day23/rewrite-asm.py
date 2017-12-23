#!/usr/bin/env python3

# https://stackoverflow.com/questions/18833759/python-prime-number-checker/18833870#18833870
import math
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


b = 106500
c = 123500
step_size = 17

h = 0
for b in range(b, c+step_size, step_size):
    if not is_prime(b):
        h += 1

print(h)
