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


def find_vertical(pattern):
    rows = len(pattern)
    cols = len(pattern[0])
    mirror_solution = 0
    nsol= 0

    vresults = []

    for mirror in range(1,cols):
        mirror_found = True
        nsol = 0
        nr_of_solutions = 0

        # ic("Checking mirror: ", mirror)
        # The mirror is placed between col[mirror-1] and col[mirror]
        for row in range(rows):
            for right_index in range(mirror, cols):
                dist = right_index - mirror
                left_index = mirror - dist - 1
                if left_index >= 0:
                    if pattern[row][right_index] != pattern[row][left_index]:
                        mirror_found = False
                        break
            if not mirror_found:
                break
        if mirror_found:
            nsol += 1
            # ncols_left = mirror
            # ncols_right = cols - mirror
            # n = min(ncols_left, ncols_right)
            mirror_solution = mirror
        vresults.append([nsol, mirror])

    ic(vresults)

    return vresults



def find_horizontal(pattern):
    rows = len(pattern)
    cols = len(pattern[0])
    mirror_solution = 0
    nsol = 0

    mirror_found = True

    hresults = []

    for mirror in range(1,rows):
        mirror_found = True
        nsol = 0
        # ic("Checking mirror: ", mirror)
        # The mirror is placed between row[mirror-1] and row[mirror]
        for col in range(cols):
            for top_index in range(mirror, rows):
                dist = top_index - mirror
                bottom_index = mirror - dist - 1
                if bottom_index >= 0:
                    if pattern[top_index][col] != pattern[bottom_index][col]:
                        mirror_found = False
                        break
            if not mirror_found:
                break
        if mirror_found:
            nsol += 1
            # nrows_top = mirror
            # nrows_bottom = rows - mirror
            # n = min(nrows_top, nrows_bottom)
            mirror_solution = mirror
        hresults.append([nsol, mirror])

    ic(hresults)

    return hresults


def solve(pattern):
    # Store size of pattern in rows and cols
    rows = len(pattern)
    cols = len(pattern[0])

    vresults = find_vertical(pattern)
    hresults = find_horizontal(pattern)

    v = h = 0

    for res in vresults:
        if res[0] == 1:
            v = res[1]
            break
    for res in hresults:
        if res[0] == 1:
            h = res[1]
            break

    # ic(v, h)


    return vresults, hresults


def find_smudge(pattern):
    rows = len(pattern)
    cols = len(pattern[0])
    smudge = pattern.copy()

    vres_org, hres_org = solve(pattern)
    ic("Original: ", vres_org, hres_org)

    res = 0

    for row in range(rows):
        for col in range(cols):
            if pattern[row][col] == "#":
                # Change character in string to '.'
                smudge[row] = smudge[row][:col] + "." + smudge[row][col + 1:]
            else:
                # Change character in string to '#'
                smudge[row] = smudge[row][:col] + "#" + smudge[row][col + 1:]
            vres, hres = solve(smudge)

            # Now find the place of the new mirror
            v = h = 0
            for i in range(len(vres)):
                if vres[i][0] == 1 and vres_org[i][0] == 0:
                    v = vres[i][1]
                    break
            for i in range(len(hres)):
                if hres[i][0] == 1 and hres_org[i][0] == 0:
                    h = hres[i][1]
                    break

            ic("Smudge: ", v, h)

            # ic(smudge)
            # Change character back
            if pattern[row][col] == "#":
                # Change character in string to '.'
                smudge[row] = smudge[row][:col] + "#" + smudge[row][col + 1:]
            else:
                # Change character in string to '#'
                smudge[row] = smudge[row][:col] + "." + smudge[row][col + 1:]

            if (v==0) and (h==0):
                continue
            elif (v!=0):
                return v, 0
            elif (h!=0):
                return 0, h
            else:
                continue


    return 0, 0

# Part 1

def part1(fname):
    patterns = read_input(fname)
    ic(patterns)
    tot_res = 0
    for pattern in patterns:
        v = h = 0
        vresults, hresults = solve(pattern)
        for res in vresults:
            if res[0] == 1:
                v = res[1]
                break
        for res in hresults:
            if res[0] == 1:
                h = res[1]
                break

        res = h * 100 + v
        tot_res += res
    return tot_res

# Part 2
def part2(fname):
    patterns = read_input(fname)
    ic(patterns)
    tot_res = 0
    for pattern in patterns:
        v, h = find_smudge(pattern)
        res = h * 100 + v

        tot_res += res
    return tot_res


real = True
verbose = False

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
