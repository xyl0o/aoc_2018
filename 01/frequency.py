#!/usr/bin/env python

with open('./input.txt') as f:
    freq = [int(l) for l in f.read().splitlines()]

print(f'Sum of frequencies: {sum(freq)}')


def freq_gen():
    while True:
        for f in freq:
            yield f


reached = set()
freq_sum = 0
for f in freq_gen():
    freq_sum += f
    if freq_sum in reached:
        break
    else:
        reached.add(freq_sum)

print(f'First reached twice: {freq_sum}')
