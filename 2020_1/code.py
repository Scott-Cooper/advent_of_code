#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://adventofcode.com/2020/day/1
# Developed and tested with Python 3.8.2
# Scott Cooper <scottslongemailaddress@gmail.com
# Version 1.0, 2021/10/29

# Part 1, correct answer:  259716
# Part 2, correct answer:  120637440

filename = "./input.csv"


def read_input():
    with open(filename, 'r') as fin:
        for row in fin:
            entries.append(int(row.strip()))


def find_matching_part1():
    for entry in entries:
        if 2020 - entry in entries:
            print("part1, found matching entry:", entry * (2020 - entry))


def find_matching_part2():
    for entry1 in entries:
        for entry2 in entries:
            if 2020 - entry1 - entry2 in entries:
                print("part2, found matching entry:", entry1 * entry2 * (2020 - entry1 - entry2))


if __name__=='__main__':
    entries=[]
    read_input()
    find_matching_part1()
    find_matching_part2()
