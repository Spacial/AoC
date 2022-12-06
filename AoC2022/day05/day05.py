#!/usr/bin/env python3
# License: GPL3
# Day 5

import sys


def showstack(stack):
    k = 1
    for i in stack:
        print(k, i)
        k += 1
    return


def move(origin, to, stack, count=1):
    if count == 0:
        return stack 
    else:
        cargo = stack[origin].pop() # ou pop(0)
        stack[to].append(cargo)
    return move(origin, to, stack, count - 1)

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
            if i.strip() != '': 
                comm.append(i.strip())
    stacks = [[] for x in range(0, stks)]
    for i in range(0, s):
        for k in range(0, len(data[i])):
            if data[i][k] == '[':
                c = data[i][k + 1]
                stacks[(k//4)].insert(0, c)
    #showstack(stacks)
    for i in comm:
        # print('---', i)
        _, count, _, origin, _, to = i.split(' ')
        move(int(origin) - 1, int(to) - 1, stacks, int(count))
    #showstack(stacks)
    message = ''
    for i in stacks:
        message += i.pop()
    return message


def part2(data):
    return


entries = []
for line in sys.stdin:
    entries.append(line)



print(part1(entries))