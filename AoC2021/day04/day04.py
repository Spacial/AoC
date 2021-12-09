#!/usr/bin/env python3
# License: GPL3
# Day 4

import sys
import logging
import itertools


class Board():
    def __init__(self, raw_data):
        self.__raw_data = raw_data
        self.__data = None
        self.__rows = None
        self.__colunms = None
        self.__size = None
        self.__m = 0
        self.__n = 0
        self.__proccess(self)
    
    @staticmethod
    def __proccess(self):
        print("board:")
        print(self.__raw_data)


class Bingo():
    def __init__(self, raw_data):
        self.__raw_data = raw_data
        self.__ndraws = None
        self.__ndraws_curr = 0
        self.__ndraws_total = None
        self.__boards = []
        self.__boards_total = 0
        self.__proccess(self)

    @property
    def getRawData(self):
        return self.__raw_data

    @property
    def getDraws(self, element=None):
        if element is None:
            return self.__ndraws
        else:
            return self.__ndraws[element]

    @property
    def getBoardss(self, element=None):
        if element is None:
            return self.__boards
        else:
            return self.__boards[element]

    # @text.setter
    # def text(self, text):
    #     if isinstance(text, str) or isinstance(text, list):
    #         self._text = text
    #     else:
    #         raise TypeError("'text' must be string or a list of strings")

    # @staticmethod
    # def token_isstop(token):
    #     # return token.is_punct or token.is_space
    #     return token.is_stop or token.is_punct or token.is_space
    @staticmethod
    def __proccess(self):
        self.__ndraws = [d for d in self.__raw_data[0].split(',')]
        print("Draws:", self.__ndraws)
        for i in self.__raw_data[2:]:
            print(i)
        return


def part1(data):
    bin = Bingo(data)
    return


def part2(data):
    return


entries = []
for line in sys.stdin:
    entries.append(line.strip())


print(part1(entries))

