#
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
from math import lcm

# Read input file
def read_input(fn):
    with open(fn) as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]

    res = []
    for line in lines:
        row = [int(x) for x in line.split(" ")]
        res.append(row)
    return res


def extrapolate(mat):
    # Get last nonzero row
    extra_mat = mat
    nr_rows = np.size(mat, 0)
    nr_cols = np.size(mat, 1)
    for r in range(nr_rows - 2, 0, -1):
        extra_mat[r, nr_cols-1] = extra_mat[r + 1, nr_cols-1] + extra_mat[r, nr_cols-r-1]
        ic(extra_mat)

    return extra_mat[0, nr_cols-1]+extra_mat[1, nr_cols-1]

def extrapolate_front(mat):
    # Get last nonzero row
    extra_mat = mat
    nr_rows = np.size(mat, 0)
    nr_cols = np.size(mat, 1)
    for r in range(nr_rows - 2, 0, -1):
        extra_mat[r, nr_cols-1] = -extra_mat[r + 1, nr_cols-1] + extra_mat[r, 0]
        ic(extra_mat)

    return -extra_mat[1, nr_cols-1]+extra_mat[0, 0]

# Part 1
def part1(fname):
    rows = read_input(fname)
    ic.disable()
    total = 0
    for row in rows:
        # Copy row into numpy array
        mat = np.matrix(row, dtype=int)
        r = 0
        # while not all elements of lat row of matrix are 0
        while not np.all(mat[r] == 0):
            # add extra row with zeros
            r += 1
            mat = np.vstack((mat, np.zeros(len(row), dtype=int)))
            for i in range(len(row)-r):
                mat[r, i] = mat[r-1, i+1] - mat[r-1, i]
        ic(mat)

        n = extrapolate(mat)
        ic(n)
        total += n
    return total


# Part 2
def part2(fname):
    rows = read_input(fname)
    ic.disable()
    total = 0
    for row in rows:
        # Copy row into numpy array
        mat = np.matrix(row, dtype=int)
        r = 0
        # while not all elements of lat row of matrix are 0
        while not np.all(mat[r] == 0):
            # add extra row with zeros
            r += 1
            mat = np.vstack((mat, np.zeros(len(row), dtype=int)))
            for i in range(len(row)-r):
                mat[r, i] = mat[r-1, i+1] - mat[r-1, i]
        ic(mat)

        n = extrapolate_front(mat)
        ic(n)
        total += n
    return total




def main():
    real = True
    part = 2


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
