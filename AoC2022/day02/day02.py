#!/usr/bin/env python3
# License: GPL3
# Day 2

import sys


def part1(data):
    opponent = { 'A':1, 'B':2, 'C':3}
    myself = { 'X':1, 'Y':2, 'Z':3}
    matrix = [[3, 6, 0],
              [0, 3, 6],
              [6, 0, 3]]
    score = 0
    for i in data:
        op, me = i.split(' ')
        # print(op, me, ':', opponent[op],myself[me], end='')
        if matrix[opponent[op] - 1][myself[me] - 1] == 0:
            show = ' <- loss' 
            score += myself[me]
        elif matrix[opponent[op] - 1][myself[me] - 1] == 3:
            show = ' <- draw '
            score += myself[me] + 3
        elif matrix[opponent[op] - 1][myself[me] - 1] == 6:
            show = ' <- win '
            score += myself[me] + 6
        #print(show)      
    return score


def part2(data):
    opponent = { 'A':1, 'B':2, 'C':3}
    myself = { 'Z':1, 'Y':2, 'X':3}
    matrix = [['B', 'A', 'C'],
              ['C', 'B', 'A'],
              ['A', 'C', 'B']]
    score = 0
    for i in data:
        op, me = i.split(' ')
        comm = matrix[opponent[op] - 1][myself[me] - 1]
        #print(op, me, ':', comm, end='')
        if me == 'X':
            show = ' <- loss ' 
            score += opponent[comm]
        elif me == 'Y':
            show = ' <- draw'
            score += opponent[comm] + 3
        elif me == 'Z':
            show = ' <- win '
            score += opponent[comm] + 6
        #print(show)      
    return score


entries = []
for line in sys.stdin:
    entries.append(line.strip())

print(part2(entries))