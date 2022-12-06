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

def parse(data):
    comm = []
    readed = True
    s = 0
    for i in data:
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
    return stacks, comm


def move(origin, to, stack, count=1):
    if count == 0:
        return stack 
    else:
        cargo = stack[origin].pop()
        stack[to].append(cargo)
    return move(origin, to, stack, count - 1)


def newmove(origin, to, stack, count=1):
    for i in stack[origin][len(stack[origin]) - count:len(stack[origin])]:
        stack[to].append(i)
    stack[origin] = stack[origin][0:len(stack[origin]) - count]
    return stack


def part1(data):
    stacks, comm = parse(data)
    for i in comm:
        _, count, _, origin, _, to = i.split(' ')
        move(int(origin) - 1, int(to) - 1, stacks, int(count))
    message = ''
    for i in stacks:
        message += i.pop()
    return message


def part2(data):
    stacks, comm = parse(data)
    for i in comm:
        _, count, _, origin, _, to = i.split(' ')
        newmove(int(origin) - 1, int(to) - 1, stacks, int(count))
    message = ''
    for i in stacks:
        message += i.pop()
    return message


entries = []
for line in sys.stdin:
    entries.append(line)

print(part2(entries))