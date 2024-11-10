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


def flood_fill_dfs(img, x, y):
    # Base case: if the current pixel is not
    # the same as the previous color
    if img[x][y] != 0:
        return

    # Marking it as the new color
    img[x][y] = 1

    # Moving up, right, down, and left one by one
    n = len(img)
    m = len(img[0])
    if x - 1 >= 0:
        flood_fill_dfs(img, x - 1, y)
    if y + 1 < m:
        flood_fill_dfs(img, x, y + 1)
    if x + 1 < n:
        flood_fill_dfs(img, x + 1, y)
    if y - 1 >= 0:
        flood_fill_dfs(img, x, y - 1)


def flood_fill(image, x, y):
    # Create a copy of the image
    newimage = copy.deepcopy(image)
    # Create a queue and append the starting pixel
    queue = [(x, y)]
    # Get the color of the starting pixel
    color = 1
    # Get the number of rows and columns
    n = len(newimage)
    m = len(newimage[0])
    ic(n, m)
    # While the queue is not empty
    while queue:
        ic(queue)
        # Get the current pixel
        x, y = queue.pop(0)
        # If the current pixel is not the same as the starting pixel
        if newimage[x][y] == color:
            continue
        # Mark the current pixel as visited
        newimage[x][y] = 1
        # Append the neighbors of the current pixel
        if x - 1 >= 0:
            queue.append((x - 1, y))
        if y + 1 < m:
            queue.append((x, y + 1))
        if x + 1 < n:
            queue.append((x + 1, y))
        if y - 1 >= 0:
            queue.append((x, y - 1))
    # Return the modified image
    return newimage

def solve1(path, color):
    # Create a list of trenches
    trenches = []
    r = c = 0
    for trench in path:
        dir = trench[0]
        steps = trench[1]
        for i in range(steps):
            if dir == "U":
                r -= 1
            elif dir == "D":
                r += 1
            elif dir == "R":
                c += 1
            elif dir == "L":
                c -= 1
            trenches.append([r, c])
    ic(trenches)



    # Calculate the minimum row value of the trenches
    min_row = min(trenches, key=lambda x: x[0])[0]
    # Calculate the minimum column value of the trenches
    min_col = min(trenches, key=lambda x: x[1])[1]

    # Shift the trenches to the positive quadrant
    for trench in trenches:
        trench[0] -= min_row
        trench[1] -= min_col

    rows = max(trenches, key=lambda x: x[0])[0] + 1
    cols = max(trenches, key=lambda x: x[1])[1] + 1
    ic(rows, cols)
    grid = np.zeros((rows, cols), dtype=int)
    ic(grid)
    for trench in trenches:
        grid[trench[0], trench[1]] = 1
    ic(grid)
    ring = np.count_nonzero(grid == 1)

    # Add a ring with zeros around the grid
    grid = np.pad(grid, 1, mode="constant")
    ic(grid)

    # Flood fill the grid, with 1's, starting in [0, 0]
    grid[0, 0] = 0
    grid = flood_fill(grid, 0, 0)

    ic(grid)
    # Count the number of 1's in the grid
    ones = np.count_nonzero(grid == 1)
    zeros = np.count_nonzero(grid == 0)
    res = zeros + ring

    return res


def score():

    return 0

# The magic shoelace formula:
# https://en.wikipedia.org/wiki/Shoelace_formula
def shoelace(trenches):
    n = len(trenches)
    ic(n)
    sum1 = 0
    sum2 = 0
    for i in range(n):
        sum1 += trenches[i][0] * trenches[(i + 1) % n][1]
        sum2 += trenches[i][1] * trenches[(i + 1) % n][0]
    return abs(sum1 - sum2) / 2


def solve2(path, codes):
    # Create a list of trenches
    trenches = []
    ring = 0
    r = c = 0
    trenches.append([r, c])
    for i in range(len(codes)):
        code = codes[i]
        hexstring = code[1:-1]
        step = int(hexstring, 16)
        ring += step
        dirnum = int(code[-1])

        if dirnum == 0:
            dir = "R"
        elif dirnum == 1:
            dir = "D"
        elif dirnum == 2:
            dir = "L"
        elif dirnum == 3:
            dir = "U"

        # Calculate the coordinates of the trench endpoints, assuming a starting point of [0, 0]

        if dir == "U":
            r -= step
        elif dir == "D":
            r += step
        elif dir == "R":
            c += step
        elif dir == "L":
            c -= step
        trenches.append([r, c])

    ic(len(trenches))

    # Calculate the length of the ring


    area = shoelace(trenches)

    return area+ring/2+1



# Part 1

def part1(fname):
    res = 0
    path, color = read_input(fname)
    res = solve1(path, color)
    return res

# Part 2
def part2(fname):
    res = 0
    path, codes = read_input(fname)
    res = solve2(path, codes)
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
