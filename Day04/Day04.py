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
        # Remove '\n' from each line
        lines = [x.strip() for x in lines]
        # remove everything before the colon
        lines = [x.split(":")[1] for x in lines]
        # split all lines before and after the dash
        lines = [x.split("|") for x in lines]
        wins_str = []
        nums_str = []
        for line in lines:
            wins_str.append(line[0])
            nums_str.append(line[1])
        # convert to list of ints
        wins_np = np.array([list(map(int, x.split())) for x in wins_str])
        nums_np = np.array([list(map(int, x.split())) for x in nums_str])

        ic(wins_np, nums_np)

    return wins_np, nums_np

# Part 1
def part1(fname):
    wins, nums = read_input(fname)
    tot_score = 0

    rows, cols = wins.shape
    for i in range(rows):
        val = 0
        for j in range(cols):
            if wins[i][j] in nums[i][:]:
                val += 1
        if val == 0:
            score = 0
        else:
            score = 2**(val-1)
        tot_score += score
        ic(i, val, score, tot_score)
    return tot_score


# Part 2
def part2(fname):
    wins, nums = read_input(fname)

    rows, cols = wins.shape
    nr_cards = [1]*rows
    scores = [0]*rows

    for i in range(rows):
        val = 0
        for j in range(cols):
            if wins[i][j] in nums[i][:]:
                val += 1
        if val == 0:
            score = 0
        else:
            score = val
        scores[i] = score

    ic(nr_cards, scores)
    for i in range(rows):
        for step1 in range(1, scores[i]+1):
            if i+step1 < rows:
                nr_cards[i+step1] += nr_cards[i]
            ic(nr_cards)
    return sum(nr_cards)



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

main()