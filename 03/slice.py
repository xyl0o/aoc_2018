#!/usr/bin/env python

import sys

from functools import reduce

import numpy as np

from typing import Tuple


Claim = Tuple[int, int, int, int, int]


def parse_claim(line: str) -> Claim:
    num, _, coord, size = line.split()
    left, right = coord.split(',')
    width, height = size.split('x')

    return int(num[1:]), int(left), int(right[:-1]), int(width), int(height)


if __name__ == '__main__':

    with open(sys.argv[1]) as f:
        claims = [parse_claim(line) for line in f.read().splitlines()]

    shape = reduce(
        lambda agg, e: (max(agg[0], e[1] + e[3]), max(agg[1], e[2] + e[4])),
        claims,
        (0, 0))

    sum_array = np.zeros(shape=shape, dtype=np.int16)

    for _, x, y, w, h in claims:
        sum_array[x:x + w, y: y + h] += 1

    print(f'Square inches with >= 2 claims: {np.sum(sum_array >= 2)}')

    for cid, x, y, w, h in claims:  # python is fast enough to be dumb
        if (sum_array[x:x + w, y: y + h] == 1).all():
            break

    print(f'First claim which does not overlap: {cid}')

