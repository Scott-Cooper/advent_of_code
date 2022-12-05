#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://adventofcode.com/2022/day/3
# Developed and tested with Python 3.8.2
# Scott Cooper <scottslongemailaddress@gmail.com

# Part 1 answer:  8202
# Part 2 answer:  2864
# This feels like sad, sloppy, breaky type code.  There should be a better way.

from pprint import pprint

filename = "./input.csv"


if __name__=='__main__':

    part1 = 0
    part2 = 0
    group = 0
    with open(filename, 'r') as fin:
        for row in fin:
            ruck = row.strip()

            # part 1 --------------------------------------
            compartment1 = ruck[:int(len(ruck)/2)]
            compartment2 = ruck[int(len(ruck)/2):]
            items = {}
            for c1_item in compartment1:
                a = ord(c1_item)-64+26
                if a > 54: a -= 58
                items[c1_item] = a 

            for c2_item in compartment2:
                if c2_item in items:
                    part1 += items[c2_item]
                    break

            # part 2 --------------------------------------
            group += 1

            if group == 1:
                all_possible_items = ruck
            else:
                for item in all_possible_items:
                    if item not in ruck:
                        all_possible_items = all_possible_items.replace(item, '')

            if group >= 3:
                group = 0
                a = ord(all_possible_items[0])-64+26
                if a > 54: a -= 58
                part2 += a

    print()
    print(f'part1: {part1}')
    print(f'part2: {part2}')
