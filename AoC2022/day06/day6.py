#!/usr/bin/env python3
# License: GPL3
# Day 6

import sys

def marker(count):
    ones = 0
    pos = 0
    for i in count:
        if count[i] == 1:
            ones += 1
        pos += 1
        if ones == 4:
            return pos
    return 0


def part1(data):
    count = {}
    for i in range(0, 26):
        count[chr(97 + i)] = 0
    point = 0
    for i in data:
         count[i] += 1
         point += 1
         if marker(count) > 4:
            break
    print(count)
    return point - 3


def part2(data):
    return


entries = []
for line in sys.stdin:
    entries.append(line.strip())



print(part1(entries[0]))

