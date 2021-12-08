#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://adventofcode.com/2021/day/5
# Developed and tested with Python 3.8.2
# Scott Cooper <scottslongemailaddress@gmail.com
# Version 1.0, 2021/12/08

# Part 1, correct answer:  388419 fish
# Part 2, correct answer:  1740449478328 fish

# The right way:  

filename = "./input.csv"


if __name__=='__main__':
    fish_timer = [0] * 9

    with open(filename, 'r') as fin:
        for row in fin:
            fishes = row.strip().split(",")
            for fish in fishes:
                fish_timer[int(fish)] += 1

    for day in range(256):
        tmp_fish_timer = [0] * 9
        prego = fish_timer[0]
        for time in range(8):
            tmp_fish_timer[time] = fish_timer[time+1]
        tmp_fish_timer[8] = prego
        tmp_fish_timer[6] += prego

        total_fish = 0
        for x in range(9):
            total_fish += tmp_fish_timer[x]

        # print(f'day {day+1:2}  {fish_timer}  {tmp_fish_timer}  total fish {total_fish}')
        fish_timer = tmp_fish_timer


    total_fish = 0
    for x in range(9):
        total_fish += fish_timer[x]
    print(f'Total fish: {total_fish}')
