#!/usr/bin/env python3
# License: GPL3
# Day 7

import sys


def getRevPath(path):
    new = []
    if len(path) == 1:
        return [path[0]]
    else:
        return [path[:1], [getRevPath(path[1:])]]


def part1(data):
    lfs = {}
    curdir = ''
    path =  []
    for i in data:
        if i[0] == '$':
            #print('comando:', i)
            com = i.split(' ')[1]
            if com == 'cd':
                args = i.split(' ')[2]
                if args == '..':
                    print(getRevPath(path))

                    path.pop()
                elif args == '/':
                    path = []
                    path.append(args)
                    curdir = args
                else:
                    curdir = args
                    path.append(args)
                print(*path, ":$", com, "args:", args)
            elif com == 'ls':
                args = ''
                print(*path, ":$", com)
        else:
            size, file = i.split(' ')
            espaco = [" " for x in path]
            if size[0] != 'd':
                #print('} size:', int(size), 'file:', file)
                print(*espaco,' |--- ', file, ':', int(size))

            else:
                #print('} dir:', file)
                          
                print(*espaco,' |--- ', file)

    return


def part2(data):
    return


entries = []
for line in sys.stdin:
    entries.append(line.strip())



print(part1(entries))