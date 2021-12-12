#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://adventofcode.com/2021/day8
# Developed and tested with Python 3.8.2
# Scott Cooper <scottslongemailaddress@gmail.com
# Version 1.0, 2021/12/09

# Part 1, correct answer:  245
# Part 2, correct answer:  983026

filename = "./input.csv"


if __name__=='__main__':
    part1 = 0
    part2 = 0

    with open(filename, 'r') as fin:
        for row in fin:
            k = row.strip().split("|")
            sample = k[0]
            output = k[1]
            # print(f'{sample} | {output}')
            patterns = sample.split(" ")

            # make a histogram from left sample
            hist = {}
            for c in sample:
                if not c in hist.keys():
                    hist[c] = 1
                else:
                    hist[c] += 1

            # Decode the right side patterns
            decode = {}
            for pattern_idx in range(10):
                length = len(patterns[pattern_idx])

                segments = []
                for c in patterns[pattern_idx]:
                    segments.append(hist[c])

                if length == 2: n = 1
                if length == 3: n = 7
                if length == 4: n = 4
                if length == 7: n = 8
                
                if length == 5:
                    if 4 in segments:
                        n = 2
                    elif 6 in segments:
                        n = 5
                    else:
                        n = 3
                
                if length == 6:
                    if not 4 in segments:
                        n = 9
                    elif not segments.count(7) == 2:
                        n = 0
                    else:
                        n = 6

                key = ''.join(sorted(patterns[pattern_idx]))
                decode[key] = n

            # Decode the left side outputs
            outputs = output.strip().split(" ")
            part2_multiplyer = 1000
            for output_idx in range(4):
                key = ''.join(sorted(outputs[output_idx]))
                n = decode[key]
                # print(f'{n} ', end="")
                if n == 1 or n == 4 or n == 7 or n ==8:
                    part1 += 1
                part2 += part2_multiplyer * n
                part2_multiplyer /= 10

    print()
    print(f'part1: {part1}')
    print(f'part2: {part2}')
