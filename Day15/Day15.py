# Test
# Advent of code 2023: Day 14
#
# Author: Bart Driessen
# Start date: 2024-11-03
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
    platform = []
    rollers = []

    with open(fn) as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]

    # Convert the line to a list of comma separated strings
    strlist = [re.split(r',', line) for line in lines]

    ic(strlist)

    return strlist

def calc_score():

    return 0

def hash(codestring, currentvalue):
    for i in range(len(codestring)):
        token = codestring[i]
        currentvalue = currentvalue + ord(token)
        currentvalue = currentvalue * 17
        currentvalue = currentvalue % 256
    return currentvalue

def solve1(strlist):
    total = 0
    for codestring in strlist:
        ic(codestring)
        currentvalue = 0
        currentvalue = hash(codestring, currentvalue)
        ic(currentvalue)
        total += currentvalue
    return total


def score(hashlist):
    total = 0
    for i in range(256):
        for j in range(len(hashlist[i])):
            total += (i+1) * (j+1) * hashlist[i][j][1]
    return total

def solve2(strlist):
    # Create a list of 256 elements, each element can contain a list of [string, value]
    # The list is initially empty
    hashlist = [[] for i in range(256)]
    for codestring in strlist:
        # Split the codestring into label, operator and value, where label is the first characters not in ["=", "-"]
        for i in range(len(codestring)):
            if codestring[i] in ["=", "-"]:
                break
        label = codestring[0:i]
        ic(label)
        operator = codestring[i]
        ic(operator)
        value = 0
        if operator == '=':
            value = int(codestring[i+1:])

        box = hash(label, 0)
        ic(box, label, operator, value)
        if operator == '-':
            # Check if the label is in the hashlist[box] list. If so, remove it
            for i in range(len(hashlist[box])):
                if hashlist[box][i][0] == label:
                    hashlist[box].pop(i)
                    break
        elif operator == '=':
            # Check if the label is in the hashlist[box] list. If so, update the value
            label_found = False
            for i in range(len(hashlist[box])):
                if hashlist[box][i][0] == label:
                    hashlist[box][i][1] = value
                    label_found = True
                    break
            # If the label is not in the hashlist[box] list, add it
            if not label_found:
                hashlist[box].append([label, value])
        else:
            continue

        ic(hashlist[0])
        ic(hashlist[1])
        ic(hashlist[3])

    # Calculate the total score
    res = score(hashlist)

    return res


# Part 1

def part1(fname):
    res = 0
    strlist = read_input(fname)
    res = solve1(strlist[0])
    return res

# Part 2
def part2(fname):
    res = 0
    strlist = read_input(fname)
    res = solve2(strlist[0])

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
