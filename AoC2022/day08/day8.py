#!/usr/bin/env python3
# License: GPL3
# Day 8

import sys

def isVisible(dir, value, x, y, trees):
    if x == len(trees) or x == 0:
        return True
    if y == len(trees[0]) or y == 0:
        return True
      
    if dir == 'u':
        if x - 1 == len(trees):
            if trees[x][y] < trees[x - 1][y]:
                return True
            else:
                return False
        else:

    elif dir == 'd':
        if x + 1 < len(trees):
            if trees[x][y] < trees[x + 1][y]:
                return True
            else:
                return False
    elif dir == 'e':
    elif dir == 'w':



def part1(data):
    trees = [[0 for x in data[k]] for k in range(0, len(data))]
    for i in range(0, len(data)):
         for k in range(0, len(data[i])):
             trees[i][k] = data[i][k]
    for i in trees:
        print(i)
    return


def part2(data):
    return


entries = []
for line in sys.stdin:
    entries.append(line.strip())



print(part1(entries))

