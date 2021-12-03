#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://adventofcode.com/2020/day/2
# Developed and tested with Python 3.8.2
# Scott Cooper <scottslongemailaddress@gmail.com
# Version 1.0, 2021/11/02

# Part 1, correct answer:  398
# Part 2, correct answer:  562

from parse import *
filename = "./input.csv"


def read_and_process_input():
    count_part1 = 0
    count_part2 = 0

    with open(filename, 'r') as fin:
        for row in fin:
            r = parse("{lowest}-{highest} {letter}: {password}", row.strip())
            lowest = int(r['lowest'])
            highest = int(r['highest'])
            letter = r['letter']
            password = r['password']
            count = password.count(letter)
            count_part1 += valid_passwords_part1(lowest, highest, letter, password, count)
            count_part2 += valid_passwords_part2(lowest, highest, letter, password, count)
    print("Count: ", count_part1)
    print("Count: ", count_part2)


def valid_passwords_part1(lowest, highest, letter, password, count):
    if count < lowest:
        pass
    elif count > highest:
        pass
    else:
        # print("Debug: ", lowest, highest, letter, password, count)
        return(1)
    return(0)


def valid_passwords_part2(lowest, highest, letter, password, count):
    if password[lowest-1] == letter or password[highest-1] == letter:
        if password[lowest-1] != password[highest-1]:
            # print("Debug: ", lowest, highest, letter, password, count)
            return(1)
    return(0)


if __name__=='__main__':
    read_and_process_input()
