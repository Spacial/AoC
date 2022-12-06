#!/usr/bin/env python3
# License: GPL3
# Day 3

import sys


def part1(data):
    priorities = {}
    for i in range(0, 26):
        priorities[chr(97 + i)] = i + 1 
        priorities[chr(65 + i)] = i + 27
    total = 0  
    for i in data:
        ruck = i[slice (0, len(i)//2)]
        sack = i[slice (len(i)//2, len(i))]
        found = set()
        for c in ruck:
            if c in sack:
                found.add(c)
        total += priorities[found.pop()]
    return total


def part2(data):
    priorities = {}
    for i in range(0, 26):
        priorities[chr(97 + i)] = i + 1 
        priorities[chr(65 + i)] = i + 27
    total = 0  
    i = 0
    while (i < len(data)): 
        ruckone = data[i]
        sacktwo = data[i + 1]
        rsthree = data[i + 2]
        found = set()
        for c in ruckone:
            if c in sacktwo and c in rsthree:
                found.add(c)
        total += priorities[found.pop()]
        i += 3
    return total


entries = []
for line in sys.stdin:
    entries.append(line.strip())


print(part2(entries))