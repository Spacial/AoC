#!/usr/bin/env python3
# License: GPL3
# Day 3

import sys


def getall(letter_array, word_list, rowCount = 5, colCount = 6):
    goRight     = [ [ row*colCount+col        for col in range(colCount) ] for row in range(rowCount) ]
    goLeft      = [ list(reversed(positions)) for positions in goRight ]
    goDown      = [ [ row*colCount+col        for row in range(rowCount) ] for col in range(colCount) ]
    goUp        = [ list(reversed(positions)) for positions in goDown ]
    goDownRight = [ [ row*colCount+row+col    for row in range(min(rowCount,colCount-col))] for col in range(colCount-1) ] \
                + [ [ (row+col)*colCount+col  for col in range(min(rowCount-row,colCount))] for row in range(1,rowCount-1) ]
    goUpLeft    = [ list(reversed(positions)) for positions in goDownRight ]
    goDownLeft  = [ [ row*colCount-row+col    for row in range(min(rowCount,col+1))] for col in range(1,colCount) ] \
                + [ [ (row+1+col)*colCount-1-col for col in range(min(rowCount-row,colCount))] for row in range(1,rowCount-1) ]
    goUpRight   = [ list(reversed(positions)) for positions in goDownLeft ]

    segments    = [ ("horizontally going right",    segment) for segment in goRight ] \
                + [ ("horizontally going left",     segment) for segment in goLeft  ] \
                + [ ("vertically going down",       segment) for segment in goDown  ] \
                + [ ("vertically going up",         segment) for segment in goUp    ] \
                + [ ("diagonally going down-right", segment) for segment in goDownRight ] \
                + [ ("diagonally going up-left",    segment) for segment in goUpLeft    ] \
                + [ ("diagonally going down-left",  segment) for segment in goDownLeft  ] \
                + [ ("diagonally going up-right",   segment) for segment in goUpRight   ]
    # transpose letter matrix into list of strings for each axis segment

    segmentStrings = [ (direction,positions,"".join(map(lambda i:letter_array[i],positions))) for direction,positions in segments ]

    # check for words ...
    ret = []
    for word in word_list:
        for direction,positions,segmentString in segmentStrings:
            startPos = segmentString.find(word) # see note below
            if startPos < 0: continue
            wordPositions = positions[startPos:][:len(word)]
            gridPositions = [ (position // colCount, position % colCount) for position in wordPositions ]
            print(word,"found\t starting at",wordPositions[0],direction,gridPositions)
            ret.append(word)
            break # don't break here if you want to find all matches
    return ret

def stoa(stringa):
    array = []
    for i in stringa:
        array.append(i.split())
    return array

def getXMAS(s, opr='XMAS'):
    return [i for i in range(len(s)) if s.startswith(opr, i)] 

def htov(s):
    for i in range(len(s[0])):
        r = ""
        for j in range(len(s)):
            r += s[j][i]
    return r

def part1(data):
    count = getall(data, ['XMAS'], len(data), len(data[0]))
    return count



def part2(data):

    return 


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
    
print(part1(entries))
