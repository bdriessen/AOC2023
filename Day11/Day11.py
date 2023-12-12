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

    universe = np.array([list(line) for line in res])

    ic(universe)
    galaxies = []
    for i in range(0, len(universe)):
        for j in range(0, len(universe[0])):
            if universe[i,j] == '#':
                galaxies.append([i,j])

    # Find rows and columns containing only '.'
    rows = []
    cols = []
    for i in range(0, len(universe)):
        if np.all(universe[i,:] == '.'):
            rows.append(i)
    for j in range(0, len(universe[0])):
        if np.all(universe[:,j] == '.'):
            cols.append(j)

    ic(galaxies, rows, cols)

    for row in rows:
        # Shift all galaxies below row one down
        galaxies = [[i+1,j] if i >= row else [i,j] for i,j in galaxies]

    new_rows
    for i in range(len(rows), 0, -1):
        for j in range(i+1, len(rows)):
            rows[j] += 1

        rows = rows[:i] + [i] + rows[i:]

    for i in range(len(cols)):
        cols[i:] += 1
        cols = cols[:i] + [i] + cols[i:]

    ic(galaxies, rows, cols)

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
