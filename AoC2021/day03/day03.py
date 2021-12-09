#!/usr/bin/env python3
# License: GPL3
# Day 3

import sys


def countBits(data, bit=None):
    if bit is None:
        size = len(data[0])
        start = 0
    else:
        if bit + 1 <= len(data[0]):
            size = bit+1
        else:
            size = len(data[0])
        start = bit
    gammas = []
    epss = []
    for i in range(start, size):
        count = [0, 0]
        for k in data:
            if int(k[i]) == 0:
                count[0] += 1
            if int(k[i]) == 1:
                count[1] += 1
        if count[0] > count[1]:
            gammas.append('0')
            epss.append('1')
        else:
            gammas.append('1')
            epss.append('0')
    return gammas, epss


def part1(data):
    gammas, epss = countBits(data)
    gamma = int(''.join([g for g in gammas]), 2)
    epsilon = int(''.join([e for e in epss]), 2)
    print("g:", gamma, "  e:", epsilon)
    return gamma * epsilon


def filterByBit(data, position, bit):
    new = []
    for i in data:
        if i[position] == bit:
            new.append(i)
    return new


def part2(data):
    # oxygen generator rating
    ogr = data.copy()
    # CO2 scrubber rating
    csr = data.copy()
    OxyGenR = ''
    CO2ScRat = ''
    for curr in range(len(data)):
        if len(ogr) == 1:
            OxyGenR = ogr[0]
        else:
            gammas, _ = countBits(ogr, curr)
            ogr = filterByBit(ogr, curr, gammas[0])
        if len(csr) == 1:
            CO2ScRat = csr[0]
        else:
            _, epss = countBits(csr, curr)
            csr = filterByBit(csr, curr, epss[0])
    print("oxygen generator rating: ", OxyGenR, " CO2 scrubber rating: ", CO2ScRat)
    ogr = int(''.join([g for g in OxyGenR]), 2)
    csr = int(''.join([e for e in CO2ScRat]), 2)
    print("oxygen generator rating: ", ogr, " CO2 scrubber rating: ", csr)
    return ogr * csr


entries = []
for line in sys.stdin:
    entries.append(line.strip())

print(part1(entries))

print(part2(entries))
