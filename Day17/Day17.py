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

def calc_score():

    return 0

def find_neighbours(pattern, path):
    row = path[0]
    col = path[1]
    direction = path[2]
    pathlength = path[3]
    newpaths = []
    # Check if we are allowed to continue in the same direction
    if pathlength < 3:
        # We are allowed to continue in the same direction
        if direction == 'E':
            newrow = row
            newcol = col + 1
            if newcol < pattern.shape[1]:
                newheatloss = path[4] + pattern[newrow, newcol]
                newpath = [newrow, newcol, direction, pathlength+1, newheatloss]
                newpaths.append(newpath)
        elif direction == 'S':
            newrow = row + 1
            newcol = col
            if newrow < pattern.shape[0]:
                newheatloss = path[4] + pattern[newrow, newcol]
                newpath = [newrow, newcol, direction, pathlength+1, newheatloss]
                newpaths.append(newpath)
        elif direction == 'W':
            newrow = row
            newcol = col - 1
            if newcol >= 0:
                newheatloss = path[4] + pattern[newrow, newcol]
                newpath = [newrow, newcol, direction, pathlength+1, newheatloss]
                newpaths.append(newpath)
        elif direction == 'N':
            newrow = row - 1
            newcol = col
            if newrow >= 0:
                newheatloss = path[4] + pattern[newrow, newcol]
                newpath = [newrow, newcol, direction, pathlength+1, newheatloss]
                newpaths.append(newpath)

    # Check if we are allowed to turn right
    if direction == 'E':
        newrow = row + 1
        newcol = col
        if newrow < pattern.shape[0]:
            newheatloss = path[4] + pattern[newrow, newcol]
            newpath = [newrow, newcol, 'S', 1, newheatloss]
            newpaths.append(newpath)
    elif direction == 'S':
        newrow = row
        newcol = col - 1
        if newcol >= 0:
            newheatloss = path[4] + pattern[newrow, newcol]
            newpath = [newrow, newcol, 'W', 1, newheatloss]
            newpaths.append(newpath)
    elif direction == 'W':
        newrow = row - 1
        newcol = col
        if newrow >= 0:
            newheatloss = path[4] + pattern[newrow, newcol]
            newpath = [newrow, newcol, 'N', 1, newheatloss]
            newpaths.append(newpath)
    elif direction == 'N':
        newrow = row
        newcol = col + 1
        if newcol < pattern.shape[1]:
            newheatloss = path[4] + pattern[newrow, newcol]
            newpath = [newrow, newcol, 'E', 1, newheatloss]
            newpaths.append(newpath)

    # Check if we are allowed to turn left
    if direction == 'E':
        newrow = row - 1
        newcol = col
        if newrow >= 0:
            newheatloss = path[4] + pattern[newrow, newcol]
            newpath = [newrow, newcol, 'N', 1, newheatloss]
            newpaths.append(newpath)
    elif direction == 'S':
        newrow = row
        newcol = col + 1
        if newcol < pattern.shape[1]:
            newheatloss = path[4] + pattern[newrow, newcol]
            newpath = [newrow, newcol, 'E', 1, newheatloss]
            newpaths.append(newpath)
    elif direction == 'W':
        newrow = row + 1
        newcol = col
        if newrow < pattern.shape[0]:
            newheatloss = path[4] + pattern[newrow, newcol]
            newpath = [newrow, newcol, 'S', 1, newheatloss]
            newpaths.append(newpath)
    elif direction == 'N':
        newrow = row
        newcol = col - 1
        if newcol >= 0:
            newheatloss = path[4] + pattern[newrow, newcol]
            newpath = [newrow, newcol, 'W', 1, newheatloss]
            newpaths.append(newpath)

    return newpaths



def solve1(pattern):
    # A path is a list [row, col, direction, pathlenght, heatloss]. The pathlenght is the number of steps taken so far.
    paths = []
    visited  = {}
    path = [0, 0, 'E', 0, 0*pattern[0, 0]]  # Start at row 0, col 0, direction East, pathlenght 0, heatloss defined in pattern[0,0]
    paths.append(path)
    visited[(0, 0, 'E', 0)] = pattern[0, 0]

    path = [0, 0, 'S', 0, 0*pattern[0, 0]]  # Start at row 0, col 0, direction South, pathlenght 0, heatloss defined in pattern[0,0]
    paths.append(path)
    visited[(0, 0, 'S', 0)] = pattern[0, 0]

    # First find the cutoff value for the heatloss
    row = col = 0
    heatloss = pattern[row, col]
    destination_reached = False
    destination = [pattern.shape[0]-1, pattern.shape[1]-1]
    while not destination_reached:
        # One step to the right
        col += 1
        heatloss += pattern[row, col]
        row += 1
        heatloss += pattern[row, col]
        if row == destination[0] and col == destination[1]:
            destination_reached = True
        if row >= pattern.shape[0] or col >= pattern.shape[1]:
            ic("Destination not reached, because we are outside the pattern")
            exit(1)
    cutoff_heatloss = heatloss
    ic(cutoff_heatloss)

    # Now start the search
    search_finished = False
    min_heatloss = cutoff_heatloss
    while not search_finished:
        newpaths = []
        for path in paths:
            neighbours = find_neighbours(pattern, path)
            ic(neighbours)
            for neighbour in neighbours:
                if (neighbour[4] <= cutoff_heatloss):
                    if ((neighbour[0], neighbour[1], neighbour[2], neighbour[3]) not in visited):
                        newpaths.append(neighbour)
                        visited[(neighbour[0], neighbour[1], neighbour[2], neighbour[3])] = neighbour[4]
                    elif visited[(neighbour[0], neighbour[1], neighbour[2], neighbour[3])] > neighbour[4]:
                            newpaths.append(neighbour)
                            visited[(neighbour[0], neighbour[1], neighbour[2], neighbour[3])] = neighbour[4]
            if path[0] == pattern.shape[0]-1 and path[1] == pattern.shape[1]-1:
                ic("Destination reached with heatloss: ", path[4])
                #paths.remove(neighbour)
                if path[4] < min_heatloss:
                    min_heatloss = path[4]
                    ic("New min_heatloss: ", min_heatloss)
        if len(newpaths) == 0:
            search_finished = True
        paths = newpaths
        #ic(paths)

    return min_heatloss


def score():

    return 0


def find_steps(pattern, step):
    row = step[0]
    col = step[1]
    prev_dir = step[2]
    ic(step, prev_dir)
    newsteps = []
    newheatloss = step[4]
    ic(newheatloss)
    # Create steps for right turns
    if prev_dir == 'E' or prev_dir == 'Y':
        new_dir = 'S'
        for i in range(1, 11):
            newrow = row + i
            newcol = col
            if newrow < pattern.shape[0]:
                if i < 4:
                    newheatloss += pattern[newrow, newcol]
                else:
                    newheatloss += pattern[newrow, newcol]
                    newstep = [newrow, newcol, new_dir, i, newheatloss]
                    newsteps.append(newstep)
    elif prev_dir == 'S':
        new_dir = 'W'
        for i in range(1, 11):
            newrow = row
            newcol = col - i
            if newcol >= 0:
                if i < 4:
                    newheatloss += pattern[newrow, newcol]
                else:
                    newheatloss += pattern[newrow, newcol]
                    newstep = [newrow, newcol, new_dir, i, newheatloss]
                    newsteps.append(newstep)
    elif prev_dir == 'W':
        new_dir = 'N'
        for i in range(1, 11):
            newrow = row - i
            newcol = col
            if newrow >= 0:
                if i < 4:
                    newheatloss += pattern[newrow, newcol]
                else:
                    newheatloss += pattern[newrow, newcol]
                    newstep = [newrow, newcol, new_dir, i, newheatloss]
                    newsteps.append(newstep)
    elif prev_dir == 'N' or prev_dir == 'X':
        new_dir = 'E'
        for i in range(1, 11):
            newrow = row
            newcol = col + i
            if newcol < pattern.shape[1]:
                if i < 4:
                    newheatloss += pattern[newrow, newcol]
                else:
                    newheatloss += pattern[newrow, newcol]
                    newstep = [newrow, newcol, new_dir, i, newheatloss]
                    newsteps.append(newstep)

    # Create steps for left turns
    newheatloss = step[4]
    if prev_dir == 'E':
        new_dir = 'N'
        for i in range(1, 11):
            newrow = row - i
            newcol = col
            if newrow >= 0:
                if i < 4:
                    newheatloss += pattern[newrow, newcol]
                else:
                    newheatloss += pattern[newrow, newcol]
                    newstep = [newrow, newcol, new_dir, i, newheatloss]
                    newsteps.append(newstep)
    elif prev_dir == 'S':
        new_dir = 'E'
        for i in range(1, 11):
            newrow = row
            newcol = col + i
            if newcol < pattern.shape[1]:
                ic(newrow, newcol, pattern[newrow, newcol], newheatloss)
                if i < 4:

                    newheatloss += pattern[newrow, newcol]
                else:
                    newheatloss += pattern[newrow, newcol]
                    newstep = [newrow, newcol, new_dir, i, newheatloss]
                    newsteps.append(newstep)
                ic(newrow, newcol, newheatloss)
    elif prev_dir == 'W':
        new_dir = 'S'
        for i in range(1, 11):
            newrow = row + i
            newcol = col
            if newrow < pattern.shape[0]:
                if i < 4:
                    newheatloss += pattern[newrow, newcol]
                else:
                    newheatloss += pattern[newrow, newcol]
                    newstep = [newrow, newcol, new_dir, i, newheatloss]
                    newsteps.append(newstep)
    elif prev_dir == 'N':
        new_dir = 'W'
        for i in range(1, 11):
            newrow = row
            newcol = col - i
            if newcol >= 0:
                if i < 4:
                    newheatloss += pattern[newrow, newcol]
                else:
                    newheatloss += pattern[newrow, newcol]
                    newstep = [newrow, newcol, new_dir, i, newheatloss]
                    newsteps.append(newstep)
    return newsteps


def solve2(pattern):
    # A path is a list [row, col, direction, pathlenght, heatloss]. The pathlenght is the number of steps taken so far.
    steps = []
    visited  = {}
    step = [0, 0, 'X', 0, pattern[0, 0]]  # Start at row 0, col 0, direction East, pathlenght 0, heatloss defined in pattern[0,0]
    steps.append(step)
    visited[(0, 0, 'E', 0)] = pattern[0, 0]

    step = [0, 0, 'Y', 0, pattern[0, 0]]  # Start at row 0, col 0, direction South, pathlenght 0, heatloss defined in pattern[0,0]
    steps.append(step)
    visited[(0, 0, 'S', 0)] = pattern[0, 0]

    # First find the cutoff value for the heatloss
    cutoff_heatloss = 10000000  # This is the value found in part 1

    # Now start the search
    search_finished = False
    min_heatloss = cutoff_heatloss

    test = find_steps(pattern, steps[0])
    ic(test)
    test = find_steps(pattern, test[4])
    ic(test)
    test = find_steps(pattern, test[0])
    ic(test)
    test = find_steps(pattern, test[5])
    ic(test)

    while not search_finished:
        new_steps = []  # This is the list of steps that will be taken in the next iteration
        for step in steps:
            targets = find_steps(pattern, step)
            for target in targets:
                if target[4] <= cutoff_heatloss:
                    if ((target[0], target[1], target[2], 0*target[3]) not in visited):
                        new_steps.append(target)
                        visited[(target[0], target[1], target[2], 0*target[3])] = target[4]
                    elif target[4] < visited[(target[0], target[1], target[2], 0*target[3])]:
                        new_steps.append(target)
                        visited[(target[0], target[1], target[2], 0*target[3])] = target[4]
                if target[0] == pattern.shape[0]-1 and target[1] == pattern.shape[1]-1:
                    ic("Destination reached with heatloss: ", target[4])
                    #paths.remove(neighbour)
                    if target[4] < min_heatloss:
                        min_heatloss = target[4]
                        ic("New min_heatloss: ", min_heatloss)

        if len(new_steps) == 0:
            search_finished = True
        steps = new_steps
        #ic(paths)
    ic(visited)

    return min_heatloss - pattern[0, 0]



# Part 1

def part1(fname):
    res = 0
    pattern = read_input(fname)
    res = solve1(pattern)
    return res

# Part 2
def part2(fname):
    res = 0
    pattern = read_input(fname)
    res = solve2(pattern)
    return res


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
