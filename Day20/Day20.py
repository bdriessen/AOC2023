# Test
# Advent of code 2023: Day 19
#
# Author: Bart Driessen
# Start date: 2024-11-10
# Part 1 done:
# Part 2 done:
#
import re
import numpy as np
import time

import portion
from icecream import ic


import copy
import portion as P
from dataclasses import dataclass

# Read input file
def read_input(fn):


    parts = []
    workflows = []
    with open(fn) as f:
        lines = f.readlines()


    lines = [line.strip() for line in lines]

    # Split the line in tokens
    for line in lines:
        if line != "" and line[0] != '{':
            # The label is the text until the first { character
            label = line.split("{")[0] + "_"
            # WorkfloWs is the text between the { and the }
            workflow = line.split("{")[1].split("}")[0]

            # split the line in tokens seperated by comma
            tokens = workflow.split(",")
            # Split token on : to get condition and action
            for i in range(len(tokens)):
                tokens[i] = tokens[i].split(":")
                ic(tokens[i])
                if len(tokens[i]) == 2:
                    tokens[i][1] += "_"
                else:
                    tokens[i][0] += "_"
            workflows.append([label, tokens])

        elif line != "":
            exec_line = line.split("{")[1].split("}")[0]
            # change , to ; to make it a valid python line
            exec_line = exec_line.replace(",", ";")
            exec(exec_line, globals())
            part = {'x':x, 'm':m, 'a':a, 's':s}

            parts.append(part)

    # ic(workflows, parts)



    return workflows, parts



def solve1(workflows, parts):

    return 0


def solve2()
    return 0

def score(part):

    return 0



# Part 1

def part1(fname):
    res = 0
    workflows, parts = read_input(fname)
    # Convert workflows to a dictionary
    workflows = dict(workflows)
    res = solve1(workflows, parts)
    return res

# Part 2
def part2(fname):
    res = 0
    workflows, parts = read_input(fname)
    workflows = dict(workflows)
    res = solve2(workflows, parts)
    return res
#########################
# Global variables
#########################

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
