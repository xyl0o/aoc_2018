#!/usr/bin/env python

from functools import reduce

with open('./input.txt') as f:
    freq = f.read().splitlines()

num = reduce(lambda x, y: x + int(y), freq, 0)

print(f'Sum of frequencies {num}')
