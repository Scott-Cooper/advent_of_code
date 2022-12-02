#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://adventofcode.com/2022/day/2
# Developed and tested with Python 3.8.2
# Scott Cooper <scottslongemailaddress@gmail.com

# Part 1 answer:  15523
# Part 2 answer:  15702

from pprint import pprint

filename = "./input.csv"


if __name__=='__main__':
    part1 = {
        "A X": 4,
        "A Y": 8,
        "A Z": 3,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 7,
        "C Y": 2,
        "C Z": 6,
    }

    part2 = {
        "A X": 3,
        "A Y": 4,
        "A Z": 8,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 2,
        "C Y": 6,
        "C Z": 7,
    }

    score_part1 = 0
    score_part2 = 0
    with open(filename, 'r') as fin:
        for row in fin:
            score_part1 += part1[row.strip()]
            score_part2 += part2[row.strip()]

    print()
    print(f'part1: {score_part1}')
    print(f'part2: {score_part2}')
