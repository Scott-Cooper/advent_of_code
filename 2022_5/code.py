#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://adventofcode.com/2022/day/5
# Developed and tested with Python 3.8.2
# Scott Cooper <scottslongemailaddress@gmail.com

# Part 1 answer:  FRDSQRRCD
# Part 2 answer:  HRFTQVWNN

from pprint import pprint


def move_crates(crane_model):
    setup = True
    firstRow = True

    with open(filename, 'r') as fin:
        for row in fin:

            if firstRow:
                npile = int(len(row)/4)
                pile = []
                for col in range(0, npile):
                    pile.append(list())
                firstRow = False

            if row == "\n":
                setup = False
                continue

            if setup:
                layer = []
                for col in range(0, npile):
                    layer.append(row[col*4+1:col*4+2])
                    if layer[col] != ' ' and row[0:4] != ' 1  ':
                        pile[col].append(layer[col])
            else:
                cmd = row.strip().split(' ')
                qty = int(cmd[1])
                fromCol = int(cmd[3])
                toCol = int(cmd[5])
  
                for col in range(0, qty):
                    tmp = pile[fromCol-1].pop(0)
                    if crane_model == '9000':
                        pile[toCol-1].insert(0, tmp)
                    else:
                        pile[toCol-1].insert(col, tmp)

                # print(row.strip())
                # pprint(pile)

        part = ''
        for col in range(0, npile):
            part += pile[col][0]
        return part


if __name__=='__main__':
    filename = "./input.csv"
    print(f'part1: {move_crates("9000")}')
    print(f'part2: {move_crates("9001")}')
