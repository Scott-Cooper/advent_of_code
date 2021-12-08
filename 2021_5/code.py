#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://adventofcode.com/2021/day/5
# Developed and tested with Python 3.8.2
# Scott Cooper <scottslongemailaddress@gmail.com
# Version 1.0, 2021/12/07

# Part 1, correct answer:  8060
# Part 2, correct answer:  

# The right way:  

filename = "./input.csv"

class Line():
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __str__(self): 
        return(f'{self.x1},{self.y1}  {self.x2},{self.y2}') 

    def is_between_without_diags(self, x, y):
        if self.x1 == self.x2 or self.y1 == self.y2:
            if (x >= min(self.x1, self.x2)) and (x <= max(self.x1, self.x2)) and (y >= min(self.y1, self.y2)) and (y <= max(self.y1, self.y2)):
                # print(f'{x},{y} is between {self.x1},{self.y1} -> {self.x2},{self.y2}')
                return(1)
        return(0)

    def is_between_with_diags(self, x, y):
        if (x >= min(self.x1, self.x2)) and (x <= max(self.x1, self.x2)) and (y >= min(self.y1, self.y2)) and (y <= max(self.y1, self.y2)):
            # print(f'{x},{y} is between {self.x1},{self.y1} -> {self.x2},{self.y2}')
            return(1)
        return(0)


################################################################################
# Algorithm was developed by Jack Elton Bresenham in 1962
# http://en.wikipedia.org/wiki/Bresenham's_line_algorithm
# Traslated from pseudocode labled "Simplification" from the link above.
################################################################################
def bresenham(x0, y0, x1, y1):
    all_points = []
    dx = abs(x1-x0)
    dy = abs(y1-y0) 
    if (x0 < x1):
        sx = 1
    else:
        sx = -1
    if (y0 < y1):
        sy = 1
    else:
        sy = -1
    err = dx-dy
    while (1):
        all_points.append([x0, y0])
        if ((x0 == x1) and (y0 == y1)):
            break
        e2 = 2*err
        if (e2 > -dy): 
            err = err - dy
            x0 = x0 + sx
        if ((x0 == x1) and (y0 == y1)): 
            all_points.append([x0, y0])
            break
        if (e2 < dx): 
            err = err + dx
            y0 = y0 + sy 
    return(all_points)


if __name__=='__main__':
    lines = []

    with open(filename, 'r') as fin:
        for row in fin:
            parts1 = row.strip().split(",")
            parts2 = parts1[1].split(" -> ")
            x1 = int(parts1[0])
            y1 = int(parts2[0])
            x2 = int(parts2[1])
            y2 = int(parts1[2])
            aline = Line(int(parts1[0]), int(parts2[0]), int(parts2[1]), int(parts1[2]))
            lines.append(aline)

    n = 1000
    m = 1000
    totalpart1 = [0] * n
    totalpart2 = [0] * n
    for i in range(n):
        totalpart1[i] = [0] * m
        totalpart2[i] = [0] * m

    for line in lines:
        for pnt in bresenham(line.x1, line.y1, line.x2, line.y2):
            totalpart1[pnt[0]][pnt[1]] += line.is_between_without_diags(pnt[0], pnt[1])
            totalpart2[pnt[0]][pnt[1]] += line.is_between_with_diags(pnt[0], pnt[1])

    totalsum1 = 0
    totalsum2 = 0
    for y in range(m):
        for x in range(n):
            if totalpart1[x][y] >=2:
                totalsum1 += 1
            if totalpart2[x][y] >=2:
                totalsum2 += 1
    print(f'part1: {totalsum1}')
    print(f'part2: {totalsum2}')

    # for y in range(m):
    #     print()
    #     for x in range(n):
    #         print(total[x][y], end =" ")
    # print()
