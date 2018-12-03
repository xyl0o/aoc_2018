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


def claim_to_field(claim: Claim) -> np.ndarray:
    arr = np.zeros(shape=(claim[3], claim[4]), dtype=np.int16)
    arr[claim[1]:claim[3], claim[2]:claim[4]] = 1
    return arr


if __name__ == '__main__':

    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()

    sum_array = np.ndarray(shape=(0, 0), dtype=np.int16)

    for line in lines:
        claim = parse_lines(line)
        idx_claim = size_to_indicies(claim)
        field = claim_to_field(idx_claim)
        zero_array = np.zeros(shape=(
            max(sum_array.shape[0], field.shape[0]),
            max(sum_array.shape[1], field.shape[1])))
        zero_array[:sum_array.shape[0], :sum_array.shape[1]] += sum_array
        zero_array[:field.shape[0], :field.shape[1]] += field

        sum_array = zero_array

    print(f'Square inches with >= 2 claims: {np.sum(sum_array >= 2)}')
