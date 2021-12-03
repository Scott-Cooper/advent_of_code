#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://adventofcode.com/2021/day/2
# Developed and tested with Python 3.8.2
# Scott Cooper <scottslongemailaddress@gmail.com
# Version 1.0, 2021/12/02

# Part 1, correct answer:  1654760
# Part 2, correct answer:  1956047400

filename = "./input.csv"


def part1():
    horizontal = 0
    vertical = 0

    with open(filename, 'r') as fin:
        for row in fin:
            a, b = row.strip().split(" ")
            b = int(b)

            if a == 'forward':
                    horizontal += b
            if a == 'up':
                    vertical -= b
            if a == 'down':
                    vertical += b
    print("part1: ", vertical * horizontal)


def part2():
    horizontal = 0
    vertical = 0
    aim = 0

    with open(filename, 'r') as fin:
        for row in fin:
            a, b = row.strip().split(" ")
            b = int(b)

            if a == 'forward':
                    horizontal += b
                    vertical += aim * b
            if a == 'up':
                    aim -= b
            if a == 'down':
                    aim += b
    print("part2: ", vertical * horizontal)


if __name__=='__main__':
    part1()
    part2()
