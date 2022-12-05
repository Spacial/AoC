#!/usr/bin/env python3
# License: GPL3
# Day 4

import sys


def part1(data):
    total = 0
    for i in data:
        f, s = i.split(',')
        ff1, ff2 = f.split('-')
        ss1, ss2 = s.split('-')
        if int(ff1) >= int(ss1) and int(ff2) <= int(ss2):
            total += 1
        elif int(ss1) >= int(ff1) and int(ss2) <= int(ff2):
            total += 1
    return total


def part2(data):
    total = 0
    for i in data:
        f, s = i.split(',')
        ff1, ff2 = f.split('-')
        ss1, ss2 = s.split('-')
        if int(ss1) > int(ff2):
            total += 1
        elif int(ss2) < int(ff1):
            total += 1
    return len(data) - total


entries = []
for line in sys.stdin:
    entries.append(line.strip())


print(part2(entries))