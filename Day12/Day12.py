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
#    ic(springs, orders)

    return springs, orders

def solve(spring, order, seq):
    global nr_of_solutions
    #ic(seq)
    seqs = []
    if len(seq) == len(order):
        #ic(seq)
        #seqs.append(seq)
        if is_matching(seq, order, spring):
            #solutions.append(seq)
            nr_of_solutions += 1
            ic(nr_of_solutions, seq)
            print(nr_of_solutions, seq)

    else:
        if not seq:
            first_start_next_seq = 0
            last_start_next_seq = len(spring) -1
            min_size_remaining_seq = 0
        else:
            first_start_next_seq = seq[-1] + order[len(seq)-1] + 1  # +1 because of the dot
            # calculate last start next seq that might be useful
            # Then calculate the minimum size of the remaining sequence
            min_size_remaining_seq = 0
            for i in range(len(seq)+1, len(order)):
                min_size_remaining_seq += order[i] + 1 # +1 because of the mandatory ?
            #ic(seq, min_size_remaining_seq)
            # Then calculate the last useful index:
            last_start_next_seq = len(spring) - min_size_remaining_seq - 1

        for i in range(first_start_next_seq, last_start_next_seq+1):
            #ic(i, seq, first_start_next_seq)
            extension_possible = True
            if i + order[len(seq)] > len(spring) - min_size_remaining_seq:
                extension_possible = False

            if extension_possible:
                # Solve for extended sequence
                if i==first_start_next_seq and verbose:
                    print("investigating", i, seq)
                solve(spring, order, seq + [i])

    #ic(seqs)
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
    global nr_of_solutions
    springs, orders = read_input(fname)
    total_nr_of_solutions = 0
    for i in range(len(springs)):
        nr_of_solutions = 0
        solve(springs[i], orders[i], [])
        total_nr_of_solutions += nr_of_solutions
        ic(i, nr_of_solutions)
    return total_nr_of_solutions


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

    total_nr_of_solutions = 0
    for i in range(len(springs)):
        nr_of_solutions = 0
        solve(springs2[i], orders2[i], [])
        total_nr_of_solutions += nr_of_solutions
        ic(i, nr_of_solutions)
    return total_nr_of_solutions


real = False
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
