#!/usr/bin/env python3
# License: GPL3
# Day 1

import sys


def part1(data):
    elves = {}
    number = 0
    localsum = 0
    for i in data:
        if i == '':
            elves[number] = localsum
            number += 1
            localsum = 0
        else:
            localsum += int(i)
    elves[number] = localsum
    return max(elves.values())


def part2(data):
    elves = {}
    number = 0
    localsum = 0
    topsters = {}
    for i in data:
        if i == '':
            elves[number] = localsum
            number += 1
            localsum = 0
        else:
            localsum += int(i)
    elves[number] = localsum
    for i in range (0,3):
        k = max(elves, key=elves.get)
        v = max(elves.values())
        topsters[i] = v
        #print(k,v)
        elves.pop(k)
    return sum(topsters.values()) 


entries = []
for line in sys.stdin:
    entries.append(line.strip())



print(part2(entries))