#!/usr/bin/env python3
# License: GPL3
# Day 2

import sys


def validate(color, count):
    cubes = { 'red': 12, 'green': 13, 'blue': 14}
    if cubes[color] <= count:
        return False
    else:
        return True

def update(color, count, cubes):
    if cubes[color] < count:
        cubes[color] = count
    return cubes

def part1(data):
    possibles = [x for x in range(1, len(data)+1)]
    for i in data:
        game, plays = i.split(':')
        for p in plays.split(';'):
            for k in p.split(','):
                count, color = k.strip().split(' ')
                j = int(game.split()[1])
                # if validate(color, int(count), j):
                if validate(color, int(count)):
                    # print(game, plays)
                    if j in possibles:
                        possibles.remove(j)
        # print(possibles, sum(possibles))
    return sum(possibles)


def part2(data):
    soma = 0
    for i in data:
        game, plays = i.split(':')
        cubes = { 'red': 0, 'green': 0, 'blue': 0}
        for p in plays.split(';'):
            for k in p.split(','):
                count, color = k.strip().split(' ')
                cubes = update(color, int(count), cubes)
        localsum = 1
        # print(game, cubes)
        for c in cubes:
            localsum *= cubes[c]
        soma += localsum
        # print(soma)
    return soma
    return 


entries = []
for line in sys.stdin:
    entries.append(line.strip())

print(part1(entries))

print(part2(entries))
