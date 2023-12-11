#
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
from math import lcm

# Read input file
def read_input(fn):
    with open(fn) as f:
        RL = f.readline().strip()
        f.readline()  # empty line
        nodes = {}
        line = f.readline().strip()
        while line:
            l = {line[0:3]:[line[7:10],line[12:15]]}
            nodes.update(l)
            line = f.readline().strip()

    return RL, nodes

# Part 1
def part1(fname):
    RL, nodes = read_input(fname)

    k = 0
    node = 'AAA'
    while node != 'ZZZ':
        if RL[k%len(RL)] == 'R':
            node = nodes[node][1]
        else:
            node = nodes[node][0]
        k += 1
    return k


# Part 2
def part2(fname):
    RL, nodes = read_input(fname)

    k = 0
    # collect all nodes ending with A
    all_keys = nodes.keys()
    keysA = []
    for key in all_keys:
        if key[2] == 'A':
            keysA.append(key)
    test = []
    cycles = [0]*len(keysA)
    ic(cycles)
    ready = False
    while not ready:
        if RL[k%len(RL)] == 'R':
            dir = 1
        else:
            dir = 0


        for idx, key in enumerate(keysA):
            keysA[idx] = nodes[key][dir]
            if key[2] == 'Z':
                if cycles[idx] == 0:
                    cycles[idx] = k
                ic(idx, k)

        ready = True
        # if any element of cycle is zero, not ready
        for cycle in cycles:
            if cycle == 0:
                ready = False
        k += 1

    ic(cycles)
    prod = 1
    for cycle in cycles:
        prod *= cycle
    res = lcm(cycles[0], cycles[1],cycles[2],cycles[3],cycles[4],cycles[5])
    return res




def main():
    real = True
    part = 2


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
