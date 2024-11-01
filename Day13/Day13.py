# Test
# Advent of code 2023: Day 13
#
# Author: Bart Driessen
# Start date: 2024-11-01
# Part 1 done:
# Part 2 done:
#
import re
import numpy as np
import time
from icecream import ic


# Read input file
def read_input(fn):
    springs = []
    orders = []

    with open(fn) as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]

    patterns = []
    pattern = []
    for line in lines:
        if line == "":
            patterns.append(pattern)
            pattern = []
        else:
            pattern.append(line)

    patterns.append(pattern)

    return patterns

def solve(pattern):
    # Store size of pattern in rows and cols
    rows = len(pattern)
    cols = len(pattern[0])


    return 0

# Part 1

def part1(fname):
    patterns = read_input(fname)
    ic(patterns)
    for pattern in patterns:
        solve(pattern)
    return 0

# Part 2
def part2(fname):
    return 0

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
