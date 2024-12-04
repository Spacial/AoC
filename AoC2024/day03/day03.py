#!/usr/bin/env python3
# License: GPL3
# Day 3

import sys

def push(lista, item):
    lista.append(item)
    return lista

def pop(lista):
    return lista[:-1]

def getPos(cmd, opr='mul'):
    return [i for i in range(len(cmd)) if cmd.startswith(opr, i)] 

def getNumbers(cmd, stack):
    work = []
    i = 0
    ret = ''
    try:
        while True:
            if cmd[i:i+3] == 'mul':
                i += 3
            if cmd[i] == '(':
                stack = push(stack,'mul')
                i += 1
                work = getNumbers(cmd[i:], stack)
                break
            elif cmd[i] == ')':              
                stack = pop(stack)
                i += 1
                work.append(ret)
                break
            elif not (cmd[i].isdigit() or cmd[i] == ','):
                break
            else:
                ret += cmd[i]
                i += 1
            if len(stack) == 0 or i >= len(cmd):
                break
    except:
        print("[E]", i, stack)
    return work

def getWork(cmd, stops):
    work = []
    for s in range(0, len(stops)):
        if s + 1 < len(stops):
            start = stops[s]
            finish = stops[s + 1]
        else:
            start = stops[s]
            finish = len(cmd)
        work.append(getNumbers(cmd[start:finish], []))
    return work

def sumTotal(work):
    total = 0
    for w in work:
        if len(w) > 0:
            numbers = w[0].split(',')
            if len(numbers) > 1:
                if numbers[0].isdigit() and numbers[1].isdigit():
                    total += (int(numbers[0]) * int(numbers[1]))
    return total

def part1(data):
    cmd = ''.join(data)
    stops = getPos(cmd)
    work = getWork(cmd, stops)
    total = sumTotal(work)
    return total

def cleanStops(stops, dos, donts):
    d = 0
    n = 0
    do = True
    ret = []
    for s in stops:
        if s > dos[d] and s > donts[n]:
            if dos[d] < donts [n]:
                do = False
            else:
                do = True
        elif s > dos[d]:
            do = True
            if n < (len(donts) - 1) and s > donts[n]:
                do = False
                n += 1
            if d < (len(dos) - 1):
                d += 1           
        elif s > donts[n]:
            do = False
            if d < (len(dos) - 1) and s > dos[d]:
                do = True
                d += 1
            if n < (len(donts) - 1):
                n += 1
        if do:
            ret.append(s)
    return ret


def part2(data):
    cmd = ''.join(data)
    stops = getPos(cmd)
    donts = getPos(cmd, 'don\'t()')
    dos = getPos(cmd, 'do()')
    cleaned = cleanStops(stops, dos, donts)
    work = getWork(cmd, cleaned)
    total = sumTotal(work)
    return total


entries = []
for line in sys.stdin:
    entries.append(line.strip())
    
print(part2(entries))