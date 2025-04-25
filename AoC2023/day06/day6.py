#!/usr/bin/env python3
# License: GPL3
# Day 6

import sys

def part1(data):
    for i in range(0, len(data)):
        mark = set()
        for k in range(0, 4):
            c = data[i + k]
            if c not in mark:
                mark.add(c)
            else:
                break
        if len(mark) == 4:
            return i + 4
    return 0


def part2(data):
    for i in range(0, len(data)):
        mark = set()
        for k in range(0, 14):
            c = data[i + k]
            if c not in mark:
                mark.add(c)
            else:
                break
        if len(mark) == 14:
            return i + 14
    return 0


entries = []
for line in sys.stdin:
    entries.append(line.strip())



print(part2(entries[0]))

