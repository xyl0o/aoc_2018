#!/usr/bin/env python

import sys

import numpy as np

from typing import Tuple, List

Claim = Tuple[int, int, int, int, int]
Shape = Tuple[int, int]


def parse_lines(line: str) -> Claim:
    num, _, coord, size = line.split()
    left, right = coord.split(',')
    width, height = size.split('x')

    return int(num[1:]), int(left), int(right[:-1]), int(width), int(height)


def size_to_indicies(claim: Claim) -> Claim:
    return (
        claim[0], claim[1], claim[2], claim[1] + claim[3], claim[2] + claim[4])


def max_shape(claims: List[Claim]) -> Shape:
    return (
        max(claims, key=lambda x: x[3])[3],
        max(claims, key=lambda x: x[4])[4])


def claim_to_field(claim: Claim, shape: Shape) -> np.ndarray:
    arr = np.zeros(shape=shape, dtype=np.int16)
    arr[claim[1]:claim[3], claim[2]:claim[4]] = 1
    return arr


if __name__ == '__main__':

    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()

    claims = [parse_lines(c) for c in lines]

    idx_claims = [size_to_indicies(c) for c in claims]
    shape = max_shape(idx_claims)
    fields = [claim_to_field(claim, shape=shape) for claim in idx_claims]
    field_array = np.stack(fields, axis=0)
    sum_array = np.sum(field_array, axis=0)

    print(f'Square inches with >= 2 claims: {np.sum(sum_array >= 2)}')
