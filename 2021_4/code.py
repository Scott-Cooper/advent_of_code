#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://adventofcode.com/2021/day/4
# Developed and tested with Python 3.8.2
# Scott Cooper <scottslongemailaddress@gmail.com
# Version 1.0, 2021/12/05

# Part 1, correct answer:  87456
# Part 2, correct answer:  15561
# The right way:  https://github.com/0x1010-dev/aoc/blob/main/2021/day4.ipynb

filename = "./input.csv"


def part1():
    for draw in draws:
        # print("Draw:", draw)
        for board_idx, val in enumerate(testboards):
            if not board_idx in board_win_order:
                for test_idx, val in enumerate(testboards[board_idx]):
                    if draw in testboards[board_idx][test_idx]:
                        # print("removed draw:", draw, " from board:", board_idx, "  test_idx:", test_idx, "   ", testboards[board_idx][test_idx])
                        testboards[board_idx][test_idx].remove(draw)
                for test_idx, val in enumerate(testboards[board_idx]):
                    if len(testboards[board_idx][test_idx]) == 0:
                        # print("Winning board:", board_idx)
                        calc_solution(board_idx, draw)


def calc_solution(board_idx, draw):
    total = 0
    for test_idx, val in enumerate(testboards[board_idx]):
        for testvalue_idx, val in enumerate(testboards[board_idx][test_idx]):
            total += testboards[board_idx][test_idx][testvalue_idx]

    if not board_idx in board_win_order:
        board_win_order.append(board_idx)
        # print("Board:", board_idx, "wins", len(board_win_order))

        if len(board_win_order) == 1:
            print("part1:", int(total / 2) * draw)
        if len(board_win_order) == 100:
            print("part2:", int(total / 2) * draw)


def transform_boards():
    for board in boards:
        tests = []
        for row in board:
            tests.append(row)
        for col in range(5):
            test = []
            for row in range(5):
                test.append(board[row][col])
            tests.append(test)
        testboards.append(tests)


if __name__=='__main__':
    r = 0
    drawstr = ""
    board = []
    boards = []
    testboards = []
    board_win_order = []

    with open(filename, 'r') as fin:
        for row in fin:
            if not drawstr:
                drawstr = row.strip()
                draws = drawstr.split(",")
                draws = list(map(int, draws))
                continue

            if row != "\n":
                rowlist = []
                for i in range(0, len(row), 3):
                    rowlist.append(int(row[i:i+3]))
                board.append(rowlist)
                r += 1
            
                if r == 5:
                    boards.append(board)
                    board = []
                    r = 0

    transform_boards()
    part1()
    # print("drawstr: ",drawstr)
    # print("draws: ",draws)
    # print(boards)
    # print(boards[0])
    # print("len of boards:", len(boards))
    # print(testboards[0])
