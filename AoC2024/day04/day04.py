#!/usr/bin/env python3
# License: GPL3
# Day 3

import sys
import numpy as np


def pprint(data):
    for i in data:
        print("".join(i))
    return

def stoa(input,  rowCount=None, colCount=None):
    if rowCount is None:
        rowCount = len(input)
    if colCount is None:
        colCount = len(input[0])
    outp=[[]]
    x = 0
    y = 0
    for char in input:
        if x == colCount:
            outp.append([])
            y += 1
            x = 0
        x += 1
        outp[y].append(char)
    return outp

# all from here: https://stackoverflow.com/questions/54657236/find-letter-of-words-in-a-matrix-diagonally
def getGoR(input):
    rowCount = len(input)
    colCount = len(input[0])
    goRight  = [ [ input[row][col]       for col in range(colCount) ] for row in range(rowCount) ]
    return goRight

def getGoL(input):
    rowCount = len(input)
    colCount = len(input[0])
    goLeft   = [ list(reversed(positions)) for positions in input ]
    return goLeft

def getGoD(input):
    rowCount = len(input)
    colCount = len(input[0])
    goDown   = [ [ input[row][col]       for row in range(rowCount) ] for col in range(colCount) ]
    return goDown


def getGoU(input):
    rowCount = len(input)
    colCount = len(input[0])
    godown = getGoD(input)
    goUp        = [ list(reversed(positions)) for positions in godown ]
    return goUp

def getGoDownR(input):
    rowCount = len(input)
    colCount = len(input[0])            
    stream = "".join(["".join(i) for i in input])
    goDownRight = [ [  stream[row*colCount+row+col]  for row in range(min(rowCount,colCount-col))] for col in range(colCount-1) ] \
                + [ [   stream[(row+col)*colCount+col] for col in range(min(rowCount-row,colCount))] for row in range(1,rowCount-1) ]
    return goDownRight

def getGoUpL(input):
    rowCount = len(input)
    colCount = len(input[0])
    goDownRight = getGoDownR(input)
    goUpLeft    = [ list(reversed(positions)) for positions in goDownRight ]
    return goUpLeft

def getGoDownL(input):
    rowCount = len(input)
    colCount = len(input[0])   
    stream = "".join(["".join(i) for i in input])
    goDownLeft  = [ [ stream[row*colCount-row+col]    for row in range(min(rowCount,col+1))] for col in range(1,colCount) ] \
                + [ [ stream[(row+1+col)*colCount-1-col] for col in range(min(rowCount-row,colCount))] for row in range(1,rowCount-1) ]
    return goDownLeft

def getGoUpR(input):
    rowCount = len(input)
    colCount = len(input[0])
    goDownLeft = getGoDownL(input)
    goUpRight   = [ list(reversed(positions)) for positions in goDownLeft ]
    return goUpRight

def getXMAS(s, opr='XMAS', p=False):
    total = 0
    for i in s:
        if p:
            print(len(i), i)
        count =[k for k in range(len(i)) if i.startswith(opr, k)]
        total += len(count)
    return  total

def part1(data):
    #count = getall(string_to_list("".join(data), len(data), len(data[0])), ['XMAS'], len(data), len(data[0]))
    arr = stoa("".join(data), len(data), len(data[0]))
    #pprint(arr)
    gor = getGoR(arr)
    gol = getGoL(arr)
    god = getGoD(arr)
    gou = getGoU(arr)
    godr = getGoDownR(arr)
    godl = getGoDownL(arr)
    goul = getGoUpL(arr)
    gour = getGoUpR(arr)
    total = 0
    tright = getXMAS(["".join(i) for i in gor])
    tleft = getXMAS(["".join(i) for i in gol])
    tdown = getXMAS(["".join(i) for i in god])
    tup = getXMAS(["".join(i) for i in gou])
    print("")
    print(tright, tleft, tdown, tup)
    print("")
    tdr = getXMAS(["".join(i) for i in godr])
    tdl = getXMAS(["".join(i) for i in godl])
    tur = getXMAS(["".join(i) for i in goul])
    tul = getXMAS(["".join(i) for i in gour])
    print(tdr, tdl, tur, tul)
    total = tright + tleft + tdown + tup + tdr + tdl + tur + tul
    return total

def getMAS(s, opr='MAS', p=False, dx=0, dy=0, lines=None):
    total = []
    line = 0
    if lines is None:
        tamanho = len(s[0])
    else:
        tamanho = lines
    for i in s:
        a = []
        count = [k for k in range(len(i)) if i.startswith(opr, k)]
        if p:
            print(len(i), i, len(count), count)
        for c in count:
            if c != '':
                a.append([line + dy , c + dx])
        line += 1
        if line == tamanho:
            line = 0
        if a != []:
            total.append(a)
    return  total

def part2old(data):
    arr = stoa("".join(data), len(data), len(data[0]))
    #pprint(arr)
    godr = getGoDownR(arr)
    godl = getGoDownL(arr)
    goul = getGoUpL(arr)
    gour = getGoUpR(arr)
    total = 0
    print(":::::", len(data))
    print("::::: down right" )
    tdr = getMAS(["".join(i) for i in godr], dx=1, dy=1, lines=len(data))
    print(">", tdr)
    print("::::: down left" )
    tdl = getMAS(["".join(i) for i in godl], dx=1, dy=-1, lines=len(data))
    print(">", tdl)
    print("::::: up right" )
    tur = getMAS(["".join(i) for i in gour], dx=-1, dy=1, lines=len(data))
    print(">", tur)
    print("::::: up  left" )
    tul = getMAS(["".join(i) for i in goul], dx=-1, dy=-1, lines=len(data))
    print(">", tul)
    print("::::: Testing")
    drdl = []
    drur = []
    for r in tdr:
        for l in tdl:
            if type(r) == type(tdr):
                for k in r:
                    if type(l) == type(tdl):
                        for z in l:
                            print(k, z)
                            if k == z:
                                drdl.append(k)
                    else:
                        print(":", l)                    
            else:
                print(":",r)          
    print(drdl)

    return 

def gotX(arr, x, y):
    tests = [[[-1, -1], [1, 1]], [[1, -1], [-1, 1]]]
    total = 0
    for t in tests:
        ul = t[0]
        dr = t[1]
        if (arr[x + ul[0]][y + ul[1]] == 'M' and arr[x + dr[0]][y + dr[1]] == 'S') or \
           (arr[x + dr[0]][y + dr[1]] == 'S' and arr[x + ul[0]][y + ul[1]] == 'M'):
            total += 1
    if total > 1:
        return True
    return False

def part2(data):
    i = len(data)
    j = len(data[0])
    arr = stoa("".join(data), i, j)
    total = 0
    for x in range(1, i - 1):
        for y in range(1, j - 1):
            if arr[x][y] == 'A':
                found = gotX(arr, x, y)
                if  found:
                    total += 1
    return total

entries = ['MMMSXXMASM', 
'MSAMXMSMSA',
'AMXSXMAAMM',
'MSAMASMSMX',
'XMASAMXAMM',
'XXAMMXXAMA',
'SMSMSASXSS',
'SAXAMASAAA',
'MAMMMXMMMM',
'MXMXAXMASX']

# entries = []
# for line in sys.stdin:
#     entries.append(line.strip())
    
print(part2(entries))


