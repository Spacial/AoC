#!/usr/bin/env python3
# License: GPL3
# Day 1

import sys
import re
import inflect

def part1(data):
    sum = 0
    for i in data:
        if i != '':
            raw = re.sub('\D', '', i)
            valor = raw[0] + raw[-1]
            sum += int(valor)
    return sum


def part2(data):
    p = inflect.engine()
    numbers = dict()
    mapa = []
    for i in range(1,10):
        palavra = p.number_to_words(i)
        numbers[palavra.replace("-", "").replace(" ", "")]=i
        mapa.append(palavra)
    sum = 0
    for i in data:
        if i != '':
            s = []
            s = list(i)
            for n in numbers:
                points=[k for k in range(len(i)) if i.startswith(n, k)]
                if len(points) > 0:
                    for p in points:
                        s[p] = numbers[n]  
            new = "".join(str(element) for element in s)   
            raw = re.sub('\D', '', new)
            valor = raw[0] + raw[-1]
            sum += int(valor)
    return sum

entries = []
for line in sys.stdin:
    entries.append(line.strip())

# print("Parte 1:")
# print(part1(entries))

print("Parte 2:")
print(part2(entries))