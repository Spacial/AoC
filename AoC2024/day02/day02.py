#!/usr/bin/env python3
# License: GPL3
# Day 2

import sys

def getSafeness(lista):
    up = False
    down = False
    for k in range(0, len(lista) - 1):
        diff = int(lista[k + 1]) - int(lista[k])
        if diff > 0:
            up = True
        elif diff < 0:
            down = True
        else:
            return False
        if up and down:
            return False
        if abs(diff) > 3:
            return False
    return True

def part1(data):
    total = 0
    for i in data:
        if getSafeness(i.split()):
            total += 1
    return total

def getTolerate(data):
    if getSafeness(data):
        return True
    for k in range(0, len(data)):
        first = data[0:k]
        last = data[k+1:len(data)+1]
        if getSafeness(first + last):
            return True
    if getSafeness(data[0:len(data)]):
        return True    
    return False

def part2(data):
    total = 0
    count = 0
    for i in data:
        if getTolerate(i.split()):
            total += 1
        count += 1
    return total

entries = []
for line in sys.stdin:
    entries.append(line.strip())

print(part2(entries))