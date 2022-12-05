#!/usr/bin/env python3
# License: GPL3
# Day 5

import sys


def part1(data):
    bkp = data
    comm = []
    readed = True
    s = 0
    for i in bkp:
        if '[' in i:
            s += 1
            continue
        elif '1' in i and readed:
            stks = int(max(i.split(' ')))
            readed = False
        elif i == '':
            continue
        else:
            comm.append(i)
    stacks = [[] for x in range(0, stks)]
    for i in range(0, s):
        for k in range(0, len(data[i])):
            if data[i][k] == '[':
                c = data[i][k + 1]
                print(i, k + 1, (k // 4) + 1 , c)
                stacks[(k//4)+1].append(c)
    print(stacks)
    
    return


def part2(data):
    return


entries = []
for line in sys.stdin:
    entries.append(line.strip())



print(part1(entries))