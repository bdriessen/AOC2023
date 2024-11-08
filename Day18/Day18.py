# Test
# Advent of code 2023: Day 17
#
# Author: Bart Driessen
# Start date: 2024-11-06
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

    with open(fn) as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]

    # Convert to a 2D numpy array where each element is the decimal value of 1 character
    pattern = np.array([[int(c) for c in line] for line in lines])
    # Print sizeof pattern
    print("Size of pattern: ", pattern.shape)
    ic(pattern)

    return pattern


def solve1():

    return 0


def score():

    return 0



def solve2():


    return 0



# Part 1

def part1(fname):
    res = 0
    pattern = read_input(fname)
    res = solve1()
    return res

# Part 2
def part2(fname):
    res = 0
    pattern = read_input(fname)
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
