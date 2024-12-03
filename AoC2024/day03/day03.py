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
                # print('[I] S:', stack)
                # print('[I] push', stack)
                stack = push(stack,'mul')
                # print('[I] S:', stack)
                i += 1
                work = getNumbers(cmd[i:], stack)
                break
            elif cmd[i] == ')':              
                # print('[I] S:', stack)
                # print('[I] pop', stack)
                stack = pop(stack)
                # print('[I] S:', stack)
                i += 1
                work.append(ret)
                break
            elif not (cmd[i].isdigit() or cmd[i] == ','):
                break
            else:
                ret += cmd[i]
                i += 1
            # print('.', end='')
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
        # print('[I] stops:', start, finish, cmd[start:finish])
        work.append(getNumbers(cmd[start:finish], []))
    return work

def sumTotal(work):
    total = 0
    for w in work:
        if len(w) > 0:
            numbers = w[0].split(',')
            # print('[I] Numbers:', numbers, w)
            if len(numbers) > 1:
                if numbers[0].isdigit() and numbers[1].isdigit():
                    total += (int(numbers[0]) * int(numbers[1]))
    return total

def part1(data):
    cmd = ''.join(data)
    print("[I] total size :", len(cmd))
    stops = getPos(cmd)
    work = getWork(cmd, stops)
    total = sumTotal(work)
    print('total work:', len(work))
    return total

def cleanStops(stops, dos, donts):
    print("[I] stops:", len(stops), stops)
    print("[I] DO's:", len(dos), dos)
    print("[I] DONT's:", len(donts), donts)
    d = 0
    n = 0
    for s in stops:
        if s > dos[d] and s > donts[n]:
            
        if s > dos[d] and s < donts[n]:

    return 


def part2(data):
    cmd = ''.join(data)
    print("[I] total size :", len(cmd))
    stops = getPos(cmd)
    donts = getPos(cmd, 'don\'t()')
    dos = getPos(cmd, 'do()')
    # dos.insert(0, 0)
    cleaned = cleanStops(stops, dos, donts)
    # work = getWork(cmd, stops)
    #total = sumTotal(work)
    #print('total work:', len(work))
    total = 0 
    return total


entries1 = 'xmul(2,4)%&mul[3,7]!@^don\'t_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))mul(215,630/\')'
entries = 'xmul(2,4)&mul[3,7]!^don\'t()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'
entries = []
for line in sys.stdin:
    entries.append(line.strip())
    
print(part2(entries))