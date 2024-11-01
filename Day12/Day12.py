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

from functools import cache


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
#    ic(springs, orders)

    return springs, orders


@cache
def solve(spring: str, order: tuple) -> int:
    global nr_of_solutions

    # check all possible sequences of first element of order in spring, and then check if the rest fits
    seq = order[0]

    solutions = 0

    for i in range(len(spring)):
        # ic(i, seq, spring, order)
        # Check if the  seq fits for all places in the spring, but stop if it cannot be realized anymore
        will_fit = True
        for j in range(seq):
            if i+j >= len(spring):
                # Beyond the end of the springs
                will_fit = False
            elif spring[i+j] == '.':
                will_fit = False

        # ic("Will fit", will_fit)
        # If the sequence fits, we still must check if the next token is not a # (if the we are not at the end
        # of the spring), or if we arrived at the end of the springs
        if will_fit:
            # First check if the sequence is terminated with a '.' or a '?'
            if len(spring) > i+seq:
                # Check if the sequence is properly terminated
                if spring[i+seq] in ['.', '?']:
                    # The sequence is properly terminated
                    # ic("Allocated seq:", seq)
                    if len(order) > 1:
                        # We must allocate the next sequence
                        solutions += solve(spring[(i+seq+1):], order[1:])
                    else:
                        # We allocated all sequences.
                        # This only is a solution if the remainder of the springs does not contain a '#'
                        post_dash = False
                        for k in range(i+seq, len(spring)):
                            if spring[k] == '#':
                                # ic("no solution due to post-dash")
                                post_dash = True
                        if not post_dash:
                            # All sequences are allocated and the remainder of the spring does not contain a '#'
                            nr_of_solutions += 1
                            solutions += 1
                            # ic('Solution found, not at the end, but no trailing #')
                            # ic(nr_of_solutions)

            elif i+seq == len(spring):
                if len(order) == 1 :
                    # We are at the end of the sequences, and it fits!

                    nr_of_solutions += 1
                    solutions += 1
                    # ic("Allocated seq at end of spring:", seq, nr_of_solutions)
                    continue
                else:
                    # We are at the end of the spring, but not at the end of the sequences
                    # ic("no solution due to end of spring")
                    break

        if spring[i] == '#':
            # Do not shift if we create an unused '#'
            # ic("Cannot shift since that will create an unused #", spring, i)
            break

    return solutions


# Part 1

def part1(fname):
    global nr_of_solutions
    springs, orders = read_input(fname)
    nr_of_solutions = 0
    sols = 0
    ic(springs)
    ic(orders)
    # Find all possible allocation of first sequence in springs
    seq = orders[0]
    for i in range(len(springs)):
        sols += solve(springs[i], tuple(orders[i]))
        ic(i, nr_of_solutions, sols)
    return sols


# Part 2
def part2(fname):
    global nr_of_solutions
    springs, orders = read_input(fname)
    # ic(orders)
    springs2 = []
    orders2 = []
    for spring in springs:
        new_spring = spring+'?'+spring+'?'+spring+'?'+spring+'?'+spring
        springs2.append(new_spring)
    for order in orders:
        new_order = order+order+order+order+order
        orders2.append(new_order)
    # ic(orders2)

    sols = 0
    total_nr_of_solutions = 0
    for i in range(len(springs2)):
        order = orders2[i]
        spring = springs2[i]
        sols += solve(spring, tuple(order))
        ic(i, nr_of_solutions)
    return sols


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
