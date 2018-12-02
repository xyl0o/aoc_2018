#!/usr/bin/env python

with open('./input.txt') as f:
    txt = f.read()

num = 0
for l in txt.splitlines():
    num += int(l)

print(num)
