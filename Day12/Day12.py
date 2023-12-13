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


def solve(spring, order, seq):
    seqs = []
    if len(seq) == len(order):
        #ic(seq)
        seqs.append(seq)
    else:
        if not seq:
            first_start_next_seq = 0
        else:
            first_start_next_seq = seq[-1] + order[len(seq)-1] + 1  # +1 because of the dot

        for i in range(first_start_next_seq, len(spring)):
            #ic(i, seq, first_start_next_seq)
            extension_possible = True
            len_spring = len(spring)
            if i + order[len(seq)] > len(spring):
                extension_possible = False

            if extension_possible:
                # Solve for extended sequence
                solve(spring, order, seq + [i])

    ic(seqs)
    return seqs


def is_matching(seq, order, spring):
    sol_spring = ['.' for i in range(len(spring))]
    for i in range(len(seq)):
        start = seq[i]
        for j in range(order[i]):
            sol_spring[start+j] = '#'

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

        # Find all possible matches
        # Start with allocating first order to first slot
        for j in range(len(springs[i])):
            start = [j]
            seqs = solve(springs[i], orders[i], start)
            ic("returned seqs", seqs)

            for seq in seqs:
                if is_matching(seq, orders[i], springs[i]):
                    ic('match')
                    matches.append(seq)
                    ic(seq)
            nr_matches = len(matches)
            #ic(matches)
            total_nr_matches += nr_matches
    return total_nr_matches


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
