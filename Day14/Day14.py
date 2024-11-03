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

def calc_score(platform, rollers):
    max_score = len(platform)
    score = 0
    for roller in rollers:
        score += max_score - roller[0]
    return score


def north(pltfrm, rllrs):
    # Deepcopy the platform using deepcopy of copy
    platform = copy.deepcopy(pltfrm)
    rollers = copy.deepcopy(rllrs)

    changed_roller = True
    while changed_roller:
        changed_roller = False
        for roller in rollers:
            i = roller[0]
            j = roller[1]
            if (i > 0) and (platform[i - 1][j] == '.'):
                platform[i - 1][j] = 'O'
                platform[i][j] = '.'
                roller[0] = i - 1
                roller[1] = j
                changed_roller = True

    # ic(platform)
    # Calculate the score

    return platform, rollers

def south(pltfrm, rllrs):
    # Deepcopy the platform using deepcopy of copy
    platform = copy.deepcopy(pltfrm)
    rollers = copy.deepcopy(rllrs)

    changed_roller = True
    while changed_roller:
        changed_roller = False
        for roller in rollers:
            i = roller[0]
            j = roller[1]
            if (i < len(platform) - 1) and (platform[i + 1][j] == '.'):
                platform[i + 1][j] = 'O'
                platform[i][j] = '.'
                roller[0] = i + 1
                roller[1] = j
                changed_roller = True

    return platform, rollers


def east(pltfrm, rllrs):
    # Deepcopy the platform using deepcopy of copy
    platform = copy.deepcopy(pltfrm)
    rollers = copy.deepcopy(rllrs)

    changed_roller = True
    while changed_roller:
        changed_roller = False
        for roller in rollers:
            i = roller[0]
            j = roller[1]
            if (j < len(platform[0]) - 1) and (platform[i][j + 1] == '.'):
                platform[i][j + 1] = 'O'
                platform[i][j] = '.'
                roller[0] = i
                roller[1] = j + 1
                changed_roller = True

    return platform, rollers


def west(pltfrm, rllrs):
    # Deepcopy the platform using deepcopy of copy
    platform = copy.deepcopy(pltfrm)
    rollers = copy.deepcopy(rllrs)

    changed_roller = True
    while changed_roller:
        changed_roller = False
        for roller in rollers:
            i = roller[0]
            j = roller[1]
            if (j > 0) and (platform[i][j - 1] == '.'):
                platform[i][j - 1] = 'O'
                platform[i][j] = '.'
                roller[0] = i
                roller[1] = j - 1
                changed_roller = True

    return platform, rollers


def solve1(pltfrm, rllrs):
    platform, rollers = north(pltfrm, rllrs)


    score = calc_score(platform, rollers)
    return score

def solve2(platform, rollers):
    new_platform = copy.deepcopy(platform)
    new_rollers = copy.deepcopy(rollers)

    for cycle in range(1000):
        new_platform, new_rollers = north(new_platform, new_rollers)
        #ic(new_platform)

        new_platform, new_rollers = west(new_platform, new_rollers)
        #ic(new_platform)

        new_platform, new_rollers = south(new_platform, new_rollers)
        #ic(new_platform)

        new_platform, new_rollers = east(new_platform, new_rollers)
        #ic(new_platform)

        score = calc_score(new_platform, new_rollers)
        ic(cycle+1, score)
    return 0


# Part 1

def part1(fname):
    res = 0
    platform, rollers = read_input(fname)
    res = solve1(platform, rollers)
    print("Result: ", res)
    return res

# Part 2
def part2(fname):
    res = 0
    platform, rollers = read_input(fname)
    res = solve2(platform, rollers)

    return res


real = True
verbose = True

part = 2

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
