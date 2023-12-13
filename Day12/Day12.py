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
    springs = []
    orders = []

    with open(fn) as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]

    for line in lines:
        # Split string in tokens
        tokens = re.split(" ", line)

        springs.append(tokens[0])
        for token in tokens[1:]:
            num = [int(i) for i in re.findall(r'\d+', token)]
            orders.append(num)
    ic(springs, orders)

    return springs, orders

def solve(spring, seq, k): # k is the index of the current element in the sequence
    if len(seq) == len(spring):
        return seq
    else:
        idx_last_segment = len(seq)-1
        if extension_possible:
            # Extend the sequence
            return solve(spring, seq + [0], k+1)
        else:
            # Find next element in sequence
            if successor_possible:
                return solve(spring, successor, k)
            else:
                return []


def find_all_seqs(spring, orders):
    seqs = []
    return seqs

def is_matching(seq, l, spring):
    ####
    # NOT TESTED YET
    #####
    sol_spring = ['.' for i in range(len(spring))]
    for i in range(len(seq)):
        for j in range(l[i]):
            sol_spring[i+j] = '#'

    is_ok = True
    for i in range(len(spring)):
        if sol_spring[i] == '.' and spring[i] == '.':
            continue
        elif sol_spring[i] == '.' and spring[i] == '?':
            continue
        elif sol_spring[i] == '#' and spring[i] == '#':
            continue
        elif sol_spring[i] == '#' and spring[i] == '?':
            continue
        else:
            is_ok = False
            break
    return is_ok
# Part 1
def part1(fname):
    springs, orders = read_input(fname)

    total_nr_matches = nr_matches = 0
    for i in range(len(springs)):
        matches = [] # List of all possible matches

        seq = orders[i][0] # First order
        # Find all possible matches
        # Start with allocating first order to first slot
        seqs = find_all_seqs(springs[i], orders[i])
        for seq in seqs:
            # Find all possible matches
            if is_matching(seq, orders[i], springs[i]):
                matches.append(seq)
        nr_matches = len(matches)
    total_nr_matches += nr_matches
    return 0


# Part 2
def part2(fname):
    springs = read_input(fname)
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
