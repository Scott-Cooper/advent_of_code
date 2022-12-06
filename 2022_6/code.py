#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://adventofcode.com/2022/day/6
# Developed and tested with Python 3.8.2
# Scott Cooper <scottslongemailaddress@gmail.com

# Part 1 answer:  1766
# Part 2 answer:  2383

from pprint import pprint
from itertools import combinations

filename = "./input.csv"


def duplicate_letters(str):
    combList = list(combinations(str, 2))
    for i in range(0, len(combList)):
        if combList[i][0] == combList[i][1]:
            return False
    return True


if __name__=='__main__':

    with open(filename, 'r') as fin:
        for row in fin:
            r = row.strip()

            for i in range(0, len(r)-3):
                sequence = r[i:i+4]
                if duplicate_letters(sequence):
                    print(f'part1 {i+4}')
                    break

            for i in range(0, len(r)-13):
                sequence = r[i:i+14]
                if duplicate_letters(sequence):
                    print(f'part2 {i+14}')
                    break
