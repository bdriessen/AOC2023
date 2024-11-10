# Test
# Advent of code 2023: Day 19
#
# Author: Bart Driessen
# Start date: 2024-11-10
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


    path = []
    color = []
    with open(fn) as f:
        lines = f.readlines()


    lines = [line.strip() for line in lines]
    # Split the line in tokens
    for line in lines:
        # Split the line in tokens seperated by space
        tokens = line.split(" ")
        path.append([tokens[0], int(tokens[1])])
        color.append(tokens[2][1:-1])
    ic(path, color)



    return path, color


def solve1(path, color):
    res = 0
    return res


def score():

    return 0


def solve2(path, codes):

    return 0



# Part 1

def part1(fname):
    res = 0
    workflows, parts = read_input(fname)
    res = solve1(workflows, parts)
    return res

# Part 2
def part2(fname):
    res = 0
    workflows, parts = read_input(fname)
    res = solve2(workflows, parts)
    return res
#########################
# Global variables
#########################

real = False
verbose = True

part = 1


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
