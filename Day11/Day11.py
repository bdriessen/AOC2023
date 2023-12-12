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


    for i in range(len(rows)-1, -1, -1):
        # Shift all galaxies down
        for galaxy in galaxies:
            if galaxy[0] > rows[i]:
                galaxy[0] += 1
        rows = rows[:i] + [rows[i]] + [r+1 for r in rows[i:]]

    for j in range(len(cols)-1, -1, -1):
        # Shift all galaxies right
        for galaxy in galaxies:
            if galaxy[1] > cols[j]:
                galaxy[1] += 1
        cols = cols[:j] + [cols[j]] + [c+1 for c in cols[j:]]

    dist = 0
    for g1 in galaxies:
        for g2 in galaxies:
            dist += abs(g1[0]-g2[0]) + abs(g1[1]-g2[1])

    ic(int(dist/2))

    return int(dist/2)


# Part 2
def part2(fname):
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

    for size in range(1000000):
        for i in range(len(rows) - 1, -1, -1):
            # Shift all galaxies down
            for galaxy in galaxies:
                if galaxy[0] > rows[i]:
                    galaxy[0] += 1
            rows = rows[:i] + [rows[i]] + [r + 1 for r in rows[i:]]

        for j in range(len(cols) - 1, -1, -1):
            # Shift all galaxies right
            for galaxy in galaxies:
                if galaxy[1] > cols[j]:
                    galaxy[1] += 1
            cols = cols[:j] + [cols[j]] + [c + 1 for c in cols[j:]]

    dist = 0
    for g1 in galaxies:
        for g2 in galaxies:
            dist += abs(g1[0]-g2[0]) + abs(g1[1]-g2[1])

    ic(int(dist/2))

    return int(dist/2)


real = False
verbose = True
part = 2

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
