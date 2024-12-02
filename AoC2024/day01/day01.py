#!/usr/bin/env python3
# License: GPL3
# Day 1

import sys

def part1(data):
    list1 = []
    list2 = []
    for i in data:
        xplod = i.split()
        list1.append(int(xplod[0]))
        list2.append(int(xplod[1]))
    list1.sort()
    list2.sort()
    total = 0
    for i in range(0, len(list1)):
        diff = abs(list2[i] - list1[i])
        total += diff
    return total

def getSim(n, lista):
    count = 0
    for k in range(0, len(lista)):
        if n == lista[k]:
            count += 1
    return count * n 

def part2(data):
    list1 = []
    list2 = []
    for i in data:
        xplod = i.split()
        list1.append(int(xplod[0]))
        list2.append(int(xplod[1]))
    list1.sort()
    list2.sort()
    total = 0
    for i in range(0, len(list1)):
        finder = list1[i]
        sim = getSim(finder, list2)
        total += sim
    return total

entries = []
for line in sys.stdin:
    entries.append(line.strip())

print(part2(entries))