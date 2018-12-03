#!/usr/bin/env python

import sys

from collections import defaultdict
from functools import reduce

from typing import Tuple, List, Generator


def single_box(box: str) -> Tuple[int, int]:
    counts: defaultdict = defaultdict(int)
    for char in box:
        counts[char] += 1
    return (
        int(2 in counts.values()),
        int(3 in counts.values()))


def hamming_dist(box: str, other: str) -> int:
    return sum(c_box != c_other for c_box, c_other in zip(box, other))


def boxes_to_check(boxes: List[str]) -> Generator[Tuple[str, str], None, None]:
    for idx, box in enumerate(boxes):
        for other in boxes[idx + 1:]:
            yield box, other


if __name__ == '__main__':

    with open(sys.argv[1]) as f:
        boxes = f.read().splitlines()

    counts = [single_box(box) for box in boxes]
    sum_two, sum_three = reduce(
        lambda agg, el: (agg[0] + el[0], agg[1] + el[1]),
        counts,
        (0, 0))

    print(f'Checksum for all boxes: {sum_two * sum_three}')

    for box, other in boxes_to_check(boxes):
        if hamming_dist(box, other) == 1:
            break
    else:
        print('Could not find boxes with hamming distance of 1.')
        sys.exit(1)

    print(f'Found matching boxes: {box}, {other}')

    common_chars = ''.join(b for b, o in zip(box, other) if b == o)
    print(f'Common chars: {common_chars}')
