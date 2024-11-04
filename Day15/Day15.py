# Test
# Advent of code 2023: Day 14
#
# Author: Bart Driessen
# Start date: 2024-11-03
# Part 1 done:
# Part 2 done:
#
import re
import numpy as np
import time
from icecream import ic

import copy

# Read input file
def read_input(fn):
    platform = []
    rollers = []

    with open(fn) as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]

    # Convert the lines to an array of an array of characters
    for line in lines:
        platform.append(list(line))

    # Create a list rollers with the coordinates of the 'O' characeters

    for i in range(len(platform)):
        for j in range(len(platform[i])):
            if platform[i][j] == 'O':
                rollers.append([i,j])

    # ic(platform, rollers)
    return platform, rollers

def calc_score():

    return 0



def solve1():
    return 0

def solve2():
    return 0


# Part 1

def part1(fname):
    res = 0
    read_input(fname)
    res = solve1()
    return res

# Part 2
def part2(fname):
    res = 0
    read_input(fname)
    res = solve2()

    return res


real = False
verbose = True

part = 1

solutions = []
nr_of_solutions = 0


def main():
    if verbose:
        ic.enable()
    else:
        ic.disable()

    # Start timer
    tic = time.perf_counter()

    if real:
        fname = "input.txt"
    else:
        fname = "testinput.txt"

    if part == 1:
        res1 = part1(fname)
        print("Part 1: ", res1)
    else:
        res2 = part2(fname)
        print("Part 2: ", res2)

    # Stop timer
    toc = time.perf_counter()
    print(f"Time elapsed: {toc - tic:0.4f} seconds")
    return


if __name__ == "__main__":
    main()
