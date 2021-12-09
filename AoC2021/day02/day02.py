#!/usr/bin/env python3
# License: GPL3
# Day 02

import sys


def part1(data):
    cmds = []
    # hor, vert
    start = [0, 0]
    for l in data:
        c, v = l.split()
        cmds.append((c, v))
    for i in cmds:
        c = i[0]
        v = i[1]
        if c == 'forward':
            start[0] += int(v)
        elif c == 'down':
            start[1] += int(v)
        elif c == 'up':
            start[1] -= int(v)
    return int(start[0]) * int(start[1])


def part2(data):
    cmds = []
    # hor, aim, depth
    start = [0, 0, 0]
    for l in data:
        c, v = l.split()
        cmds.append((c, v))
    for i in cmds:
        c = i[0]
        v = i[1]
        if c == 'forward':
            start[0] += int(v)
            start[2] += int(v) * start[1]
        elif c == 'down':
            start[1] += int(v)
        elif c == 'up':
            start[1] -= int(v)
    return int(start[0]) * int(start[2])

entries = []
for line in sys.stdin:
    entries.append(line.strip())


print(part2(entries))
