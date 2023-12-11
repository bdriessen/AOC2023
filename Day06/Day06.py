#
# Advent of code 2023: Day 02
#
# Author: Bart Driessen
# Start date: 2023-01-23
# Part 1 done:
# Part 2 done:
#

import numpy as np
import time
from icecream import ic

# Read input file
def read_input(fn):
    with open(fn) as f:
        lines = f.readlines()
    return lines

# Part 1
def part1(fname):
    if fname == "testinput.txt":
        t = [7, 15, 30]
        d = [9, 40, 200]
        ic(t,d)
    else:
        t = [54, 81, 70, 88]
        d = [446, 1292, 1035, 1007]

    totsol = 1
    for i in range(len(t)):
        sol = 0
        for k in range(t[i]):
            if (t[i]-k)*k > d[i]:
                sol += 1
        totsol *= sol
    return totsol



# Part 2
def part2(fname):
    if fname == "testinput.txt":
        t = [71530]
        d = [940200]
        ic(t,d)
    else:
        t = [54817088]
        d = [446129210351007]

    totsol = 1
    for i in range(len(t)):
        sol = 0
        for k in range(t[i]):
            if (t[i]-k)*k > d[i]:
                sol += 1
        totsol *= sol
    return totsol



def main():
    real = True
    part = 2

    print("Advent of code 2023: Day 04")

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

ic.enable()
main()