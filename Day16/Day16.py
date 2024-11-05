# Test
# Advent of code 2023: Day 14
#
# Author: Bart Driessen
# Start date: 2024-11-04
# Part 1 done:
# Part 2 done:
#
import re
import numpy as np
import time
from icecream import ic

import copy
from map import Map
from foton import Foton


# Read input file
def read_input(fn):
    platform = []
    rollers = []

    with open(fn) as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]

    # Convert the lines to lists of characters
    pattern = [list(line) for line in lines]
    #ic(pattern)

    return pattern

def calc_score():

    return 0



def solve1():

    return 0


def score():

    return 0

def solve2():


    return res


# Part 1

def part1(fname):
    res = 0
    pattern = read_input(fname)
    mymap = Map(pattern)
    foton = Foton([0, 0], 'E')
    mymap.inject_foton(foton)
    # mymap.add_foton(foton)
    # mymap.visited[0][0] = 1
    # mymap.visited_east[0][0] = 1
    ic(mymap.map)
    ic(mymap.fotons[0].pos, mymap.fotons[0].direction)
    while len(mymap.fotons)!=0:
        mymap.move_fotons()
        ic(mymap.fotons)

    # Count the number of visited cells
    for row in mymap.visited:
        for cell in row:
            if cell == 1:
                res += 1
    return res

# Part 2
def part2(fname):
    res = 0
    pattern = read_input(fname)
    energized = 0
    most_energized = 0
    # Enter from the top
    for i in range(len(pattern[0])):
        foton = Foton([0, i], 'S')
        mymap = Map(pattern)
        mymap.inject_foton(foton)
        while len(mymap.fotons)!=0:
            mymap.move_fotons()
        # Count the number of visited cells
        energized = 0
        for row in mymap.visited:
            for cell in row:
                if cell == 1:
                    energized += 1
        if energized > most_energized:
            most_energized = energized
    # Enter from the bottom
    for i in range(len(pattern[0])):
        foton = Foton([len(pattern)-1, i], 'N')
        mymap = Map(pattern)
        mymap.inject_foton(foton)
        while len(mymap.fotons)!=0:
            mymap.move_fotons()
        # Count the number of visited cells
        energized = 0
        for row in mymap.visited:
            for cell in row:
                if cell == 1:
                    energized += 1
        if energized > most_energized:
            most_energized = energized
    # Enter from the left
    for i in range(len(pattern)):
        foton = Foton([i, 0], 'E')
        mymap = Map(pattern)
        mymap.inject_foton(foton)
        while len(mymap.fotons)!=0:
            mymap.move_fotons()
        # Count the number of visited cells
        energized = 0
        for row in mymap.visited:
            for cell in row:
                if cell == 1:
                    energized += 1
        if energized > most_energized:
            most_energized = energized
    # Enter from the right
    for i in range(len(pattern)):
        foton = Foton([i, len(pattern[0])-1], 'W')
        mymap = Map(pattern)
        mymap.inject_foton(foton)
        while len(mymap.fotons)!=0:
            mymap.move_fotons()
        # Count the number of visited cells
        energized = 0
        for row in mymap.visited:
            for cell in row:
                if cell == 1:
                    energized += 1
        if energized > most_energized:
            most_energized = energized
    return most_energized


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
