#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://adventofcode.com/2022/day/1
# Developed and tested with Python 3.8.2
# Scott Cooper <scottslongemailaddress@gmail.com

# Part 1 answer:  70720
# Part 2 answer:  207148

from pprint import pprint

filename = "./input.csv"


if __name__=='__main__':
    calories = []
    calories.append(0)
    elf = 0
    with open(filename, 'r') as fin:
        for row in fin:
            if row == "\n":
                calories.append(0)
                elf += 1
            else:
                calories[elf] += int(row.strip())

    calories.sort(reverse=True)

    print()
    print(f'part1: {max(calories)}')
    print(f'part2: {(calories[0] + calories[1] + calories[2])}')
