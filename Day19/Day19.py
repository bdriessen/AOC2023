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
from icecream import ic


import copy

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
            label = line.split("{")[0]
            # WorkfloWs is the text between the { and the }
            workflow = line.split("{")[1].split("}")[0]

            # split the line in tokens seperated by comma
            tokens = workflow.split(",")
            # Split token on : to get condition and action
            for i in range(len(tokens)):
                tokens[i] = tokens[i].split(":")
            workflows.append([label, tokens])

        elif line != "":
            exec_line = line.split("{")[1].split("}")[0]
            # change , to ; to make it a valid python line
            exec_line = exec_line.replace(",", ";")
            exec(exec_line, globals())
            part = {'x':x, 'm':m, 'a':a, 's':s}

            parts.append(part)

    ic(workflows, parts)



    return workflows, parts


def evaluate(workflows, part):
    # Evaluate the workflow
    x = part['x']
    m = part['m']
    a = part['a']
    s = part['s']

    ic(workflows)
    label = 'in'
    ready = False
    fires = False
    while not ready:
        actions = workflows[label]
        for i in range(len(actions)-1):

            ic(actions[i])
            fires = eval(actions[i][0])

            if fires:
                label = actions[i][1]
                ic(fires, label)
                break
        if not fires:
            label = actions[-1][0]
        if label == 'A' or label == 'R':
            ready = True
    return label


def solve1(workflows, parts):

    total_score = 0
    for part in parts:
        check = evaluate(workflows, part)
        if check == 'A':
            total_score += score(part)

    return total_score


def score(part):

    return part['x'] + part['m'] + part['a'] + part['s']


def solve2(path, codes):

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
    res = solve2(workflows, parts)
    return res
#########################
# Global variables
#########################

real = True
verbose = False

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
