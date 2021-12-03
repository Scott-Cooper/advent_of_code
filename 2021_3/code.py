#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://adventofcode.com/2021/day/3
# Developed and tested with Python 3.8.2
# Scott Cooper <scottslongemailaddress@gmail.com
# Version 1.0, 2021/12/03

# Part 1, correct answer:  845186
# Part 2, correct answer:  4636702

import operator
filename = "./input.csv"


def read_input():
    with open(filename, 'r') as fin:
        for row in fin:
            rows.append(row.strip())


def part1():
    gamma = 0
    epsilon = 0
    for i in range(12):
        c = 0
        for row in rows:
            if row[i] == '1':
                c += 1
            else:
                c -= 1
        if c > 0:
            gamma = gamma << 1 | 1
            epsilon = epsilon << 1 | 0
        else:
            gamma = gamma << 1 | 0
            epsilon = epsilon << 1 | 1
    print("part1: ", gamma * epsilon)


def part2():
    oxy = part2_finder(rows, operator.ge)
    co2 = part2_finder(rows, operator.lt)
    print("part2: ", oxy * co2)


def part2_finder(xrows, op):
    for i in range(12):
        a = []
        b = []
        for row in xrows:
            if row[i] == '1':
                a.append(row)
            else:
                b.append(row)

        if op(len(a), len(b)):
            xrows = a
        else:
            xrows = b

        if len(xrows) == 1:
            # print("remaining value:", xrows[0], "or", int(xrows[0], 2))
            return(int(xrows[0], 2))


if __name__=='__main__':
    rows = []
    read_input()
    part1()
    part2()