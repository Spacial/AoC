#!/usr/bin/env python3
# License: GPL3
# Day 3

import sys
import re

def showmap(mapa):
    for i in range(0, len(mapa)):
        for j in range(0, len(mapa[0])):
            print(mapa[i][j], end='')
        print("")
    # print(mapa)
    return

def listAlones(mapa):
    for i in range(1, len(mapa) - 1):
        for j in range(1, len(mapa[0]) - 1 ):
            if i > 0 and j > 0 and i < (len(mapa) - 1) and j < (len(mapa[0]) - 1):
                for x in range(-1, 1):
                    for y in range (-1, 1):
                        re.sub('\D', '', mapa[i + x][j + y])
        print("")

def part1(data):
    allnumbers = []
    mapa = []
    for l in data:
        mapa.append(l.split())
        justnumbers = l.split('.')
        for j in justnumbers:
            if j != '':
                number = re.sub('\D', '', j)
                if number != '':
                    allnumbers.append(number)
        print(justnumbers)
    print(allnumbers)
    # fazer o scan do mapa, tem que ser via chars
    showmap(mapa)

    return 


def part2(data):
    
    return 


entries = []
for line in sys.stdin:
    entries.append(line.strip())


print(part1(entries))