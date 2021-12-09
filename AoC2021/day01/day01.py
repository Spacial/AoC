#!/usr/bin/env python3
# License: GPL3
# Day 01

import sys


def part1(data):
    increase = 0
    start = data[0]
    trail = ['N/A']
    for x in range(1, len(data)):
       if data[x] > start:
#           trail.append('increase  ::'+str(start)+'/'+str(data[x]))
           increase += 1
           start = data[x]
       else:
#           trail.append('decrease ::'+str(start)+'/'+str(data[x]))
           start = data[x]
#    [print(x) for x in trail]
    return increase


def part2(data):
    increase = 0
    start = data[0] + data[1] + data[2]
    # trail = ['N/A']
    for x in range(1, len(data) - 2):
       actual = data [x] + data[x + 1] + data [x + 2]
       if actual > start:
        #    trail.append('increase  ::'+str(start)+'/'+str(actual))
           increase += 1
           start = actual
       else:
        #    trail.append('decrease ::'+str(start)+'/'+str(actual))
           start = actual
    # [print(x) for x in trail]
    return increase


entries = []
for line in sys.stdin:
    entries.append(line.strip())

data = [int(e) for e in entries]

print("Part1:", part1(data))

print("Part2:", part2(data))
