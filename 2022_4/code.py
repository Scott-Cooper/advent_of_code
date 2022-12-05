#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://adventofcode.com/2022/day/4
# Developed and tested with Python 3.8.2
# Scott Cooper <scottslongemailaddress@gmail.com

# Part 1 answer:  538
# Part 2 answer:  792

from pprint import pprint

filename = "./input.csv"


if __name__=='__main__':

    part1 = 0
    part2 = 0
    with open(filename, 'r') as fin:
        for row in fin:
            r = row.strip()
            (pair1, pair2) = r.split(',')
            (p1s, p1e) = map(int, pair1.split('-'))
            (p2s, p2e) = map(int, pair2.split('-'))

            if (p1s >= p2s and p1e <= p2e) or (p2s >= p1s and p2e <= p1e):
                part1 += 1

            if not (p1s > p2e or p2s > p1e):
                part2 += 1

    print()
    print(f'part1: {part1}')
    print(f'part2: {part2}')
