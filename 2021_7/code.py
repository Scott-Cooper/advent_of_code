#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://adventofcode.com/2021/day/7
# Developed and tested with Python 3.8.2
# Scott Cooper <scottslongemailaddress@gmail.com
# Version 1.0, 2021/12/09

# Part 1, correct answer:  354129
# Part 2, correct answer:  98905973

filename = "./input.csv"


if __name__=='__main__':
    crabs = []
    fuelcost1 = []
    fuelcost2 = []
    with open(filename, 'r') as fin:
        for row in fin:
            crabs = row.strip().split(",")
    crabs = list(map(int, crabs))

    for pos in range(max(crabs)):
        fuel1 = 0
        fuel2 = 0
        for crab in crabs:
            fuel1 += abs(crab - pos)
            fuel2 += int((abs(crab - pos) * (abs(crab - pos)+1)) / 2)
        fuelcost1.append(fuel1)
        fuelcost2.append(fuel2)
        print(f'pos {pos+1:-4} {fuel1:7} {fuel2:8}')

    print()
    print(f'part1: {min(fuelcost1)}')
    print(f'part2: {min(fuelcost2)}')
