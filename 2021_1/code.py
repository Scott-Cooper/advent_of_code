#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://adventofcode.com/2021/day/1
# Developed and tested with Python 3.8.2
# Scott Cooper <scottslongemailaddress@gmail.com
# Version 1.0, 2021/12/01

# Part 1, correct answer:  1502
# Part 2, correct answer:  1538
# https://www.reddit.com/r/adventofcode/comments/r66vow/2021_day_1_solutions/

filename = "./input.csv"


def read_input():
    with open(filename, 'r') as fin:
        for row in fin:
            entries.append(int(row.strip()))


def part1():
    count = 0
    prev = 0
    for entry in entries:
        if entry > prev:
            count += 1
        prev = entry
    print("part1, count of increases:", count - 1)


def part2():
    print("part2, count of increases:",sum(a < b for a, b in zip(entries, entries[3:])))


if __name__=='__main__':
    entries=[]
    read_input()
    part1()
    part2()
