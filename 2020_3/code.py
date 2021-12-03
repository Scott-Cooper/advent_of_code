#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://adventofcode.com/2020/day/2
# Developed and tested with Python 3.8.2
# Scott Cooper <scottslongemailaddress@gmail.com
# Version 1.0, 2021/11/03

# Part 1, correct answer:  
# Part 2, correct answer:  

filename = "./input.csv"


def read_input():
    with open(filename, 'r') as fin:
        print(fin)
        for y, yval in enumerate(fin):
            # print(yval)
            for x, xval in enumerate(yval):
                # pass
                print("y: ", y)
                print("x: ", x)
                print("xval: ", xval)
                print("yval: ", yval)

                forest[x][y] = xval
            # for row in fin:
            #     for grid in row:
            #         forest[row])
    # print("Count: ", count_part1)
    # print("Count: ", count_part2)
    # print(forest)


def count_trees_part1(right, down):
    for entry in forest:
        if 2020 - entry in entries:
            print("part1, found matching entry:", entry * (2020 - entry))

def valid_passwords_part2(right, down):
    return(0)


if __name__=='__main__':
    rows, cols = (5,5)
    print(rows)
    # arr = [[rows * cols]*cols]*rows
    arr = [0]*5
    arr[3] = 4
    print(arr)
    # exit()
    # forest=[]
    forest = ['x']*100
    print(forest)
    read_input()
    count_trees_part1(3, 1)
