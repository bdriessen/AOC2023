# Test
# Advent of code 2023: Day 02
#
# Author: Bart Driessen
# Start date: 2023-01-23
# Part 1 done:
# Part 2 done:
#
import re
import numpy as np
import time
from icecream import ic


# Read input file
def read_input(fn):
    with open(fn) as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]

    return lines



# Part 1
def part1(fname):
    res = read_input(fname)

    return 0


# Part 2
def part2(fname):
    res1 = part1(fname)
    return 0


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
        res1, visited = part1(fname)
        nr_v=0
        for i in range(len(visited)):
            for j in range(len(visited[0])):
                if visited[i][j]:
                    nr_v += 1
        print("Part 1: ", res1, nr_v)
    else:
        res2 = part2(fname)
        print("Part 2: ", res2)

    # Stop timer
    toc = time.perf_counter()
    print(f"Time elapsed: {toc - tic:0.4f} seconds")
    return

if __name__ == "__main__":
    main()
