#!/usr/bin/env python

import sys

from itertools import cycle


if __name__ == '__main__':

    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()

    changes = [int(l) for l in lines]

    print(f'Resulting frequency: {sum(changes)}')

    reached: set = set()
    frequency = 0
    for change in cycle(changes):
        frequency += change
        if frequency in reached:
            break
        else:
            reached.add(frequency)

    print(f'First reached twice: {frequency}')
