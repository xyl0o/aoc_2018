#!/usr/bin/env python

from collections import defaultdict
from functools import reduce

from typing import Tuple


def singe_box(box: str) -> Tuple[int, int]:
    counts: defaultdict = defaultdict(int)
    for char in box:
        counts[char] += 1
    return (
        int(2 in counts.values()),
        int(3 in counts.values()))


if __name__ == '__main__':

    with open('./input.txt') as f:
        boxes = f.read().splitlines()

    counts = [singe_box(box) for box in boxes]
    sum_two, sum_three = reduce(
        lambda agg, el: (agg[0] + el[0], agg[1] + el[1]),
        counts,
        (0, 0))

    print(f'Checksum for all boxes: {sum_two * sum_three}')
