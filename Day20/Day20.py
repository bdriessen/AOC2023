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

    modules = []

    # Split the line in tokens
    for line in lines:
        # Firs, create all the modules
        tokens = line.split(" -> ")
        if tokens[0] == "broadcaster":
            module_type = "bc"
            module_name = "broadcaster"
        elif tokens[0][0] == "%":
            module_type = "ff"
            module_name = tokens[0][1:]
        elif tokens[0][0] == "&":
                module_type = "cj"
                module_name = tokens[0][1:]
        else:
            module_type = "other"
            module_name = tokens[0]
        #ic(module_name, module_type)
        module = Module(module_name, module_type, [], [], [])
        #ic(module.name, module.type)
        modules.append(module)
        #ic(str(module))

    # Now, add the connections
    for line in lines:
        tokens = line.split(" -> ")
        source = tokens[0]
        if source.startswith("%") or source.startswith("&"):
            source = source[1:]
        dest = tokens[1]
        # Split dest in tokens, containing the individual outputs
        dest_tokens = dest.split(", ")
        # Find the module with the name source
        for index, module in enumerate(modules):
            #ic(module.name)
            if module.name == source:
                for token in dest_tokens:
                    module.out.append(token)
                # ic(str(module))
                # Find the modules with the names in dest_tokens
                for dest_token in dest_tokens:
                    for module2 in modules:
                        if module2.name == dest_token:
                            module2.inp.append(source)
                            # ic(str(module2))

    # Finally, add the states
    for module in modules:
        for i in range(len(module.inp)):
            module.state.append("Low")
    for module in modules:
        ic(str(module))
    return modules


class Module:
    name = ""
    type = ""
    inp = []
    out = []
    state = []
    nlows = 0
    nhighs = 0

    def __init__(self, *args, **kwargs):
        if len(args) == 2:
            self.name = args[0]
            self.type = args[1]
            self.inp = []
            self.out = []
            self.state = []
            nlows = 0
            nhighs = 0
        elif len(args) == 5:
            self.name = args[0]
            self.type = args[1]
            self.inp = args[2]
            self.out = args[3]
            self.state = args[4]
            nlows = 0
            nhighs = 0
    def __str__(self):
        return f"Module: {self.name}, {self.type}, {self.inp}, {self.out}, {self.state}, {self.nlows}, {self.nhighs}"



def solve1(workflows, parts):

    return 0


def solve2():
    return 0

def score(part):

    return 0



# Part 1

def part1(fname):
    res = 0
    res = read_input(fname)
    # Convert workflows to a dictionary
    return res

# Part 2
def part2(fname):
    res = 0

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
