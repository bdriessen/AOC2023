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

    # ic(workflows, parts)



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


@dataclass
class Chunk():

    nxt_label: str
    def __init__(self, *args):
        if len(args) == 4:
            self.xmas = {}
            self.xmas["x"] = args[0]
            self.xmas["m"] = args[1]
            self.xmas["a"] = args[2]
            self.xmas["s"] = args[3]
            self.nxt_label = ""
        elif len(args) == 0:
            self.xmas = {}
            self.xmas["x"] = P.open(0,0)
            self.xmas["m"] = P.open(0,0)
            self.xmas["a"] = P.open(0,0)
            self.xmas["s"] = P.open(0,0)
            self.nxt_label = ""

def process(lbl, lblstore, workflows):
    # Process al the chunks for a single label
    labelstore = lblstore.copy()
    actions = workflows[lbl]
    chunks = labelstore[lbl]
    modified = False
    newchunks = []
    removelist = []

    # Process the actions
    while len(chunks) > 0:
        # Get the next chunk
        for action in actions:
            ic(action, len(action))
            # After processing this chunk, it will be removed from the list
            # New chunks will be created. A new chunk might apply for this label, but with different xmas values.
            #if len(chunks) == 0:
            #    continue
            ic(chunks)
            chunk = chunks.pop(0)
            ic(chunks)
            # Check if the action is a condition or an else
            if len(action) == 2:
                # This is the conditional statement
                dest = action[1]
                id = action[0][0]
                oper = action[0][1]
                value = int(action[0][2:])

                if oper == '<':
                    # Make a new chunk for the destination and update the current chunk
                    left = copy_chunk(chunk)
                    left[id] = chunk[id] & P.closed(-P.inf, value-1)
                    ic(left)
                    if not left[id].empty:
                        # The condition is true. So create a new chunk for the destination, and
                        # update the current chunk. Store both chunks in the newchunks list.
                        right = copy_chunk(chunk)
                        right[id] = chunk[id] & P.closed(value, P.inf)  # Here we update the remaining xmas value
                        ic(right)
                        newchunks.append([lbl, right])
                        newchunks.append([dest, left])
                        ic(newchunks)
                else: # oper == '>'
                    # Make a new chunk for the destination and update the current chunk
                    right = copy_chunk(chunk)
                    right[id] = chunk[id] & P.closed(value+1, P.inf)
                    if not right[id].empty:
                        # The condition is true. So create a new chunk for the destination, and
                        # update the current chunk. Store both chunks in the newchunks list.
                        left = copy_chunk(chunk)
                        left[id] = chunk[id] & P.closed(-P.inf, value)
                        newchunks.append([lbl, left])
                        newchunks.append([dest, right])
            else:
                # No if condition is true. So we have to send the chunk to the destination
                ic("removing chunk via else")
                dest = action[0]
                else_chunk = copy_chunk(chunk)
                id = ""
                oper = ""
                value = 0
                newchunks.append([dest, else_chunk])


            while len(newchunks) > 0:
                modified = True
                newchunk = newchunks.pop(0)
                loc = newchunk[0]
                ic(loc, newchunk[1], labelstore[loc])
                ic(labelstore)
                labelstore[loc].append(newchunk[1])
                ic(labelstore)
            newchunks = []

    return labelstore, modified

def copy_chunk(chunk):
    newchunk = {}
    newchunk["x"] = chunk["x"]
    newchunk["m"] = chunk["m"]
    newchunk["a"] = chunk["a"]
    newchunk["s"] = chunk["s"]
    return newchunk

def make_chunk(x, m, a, s):
    chunk = {}
    chunk["x"] = x
    chunk["m"] = m
    chunk["a"] = a
    chunk["s"] = s
    return chunk

def make_empty_chunk():
    chunk = {}
    chunk["x"] = P.open(0,0)
    chunk["m"] = P.open(0,0)
    chunk["a"] = P.open(0,0)
    chunk["s"] = P.open(0,0)
    return chunk

def solve2(workflows, parts):

    # Create a label store
    ic(workflows)
    labelstore = {}
    for workflow in workflows:
        labelstore[workflow[:]] = []
    chunk = make_chunk(P.closed(1, 4000), P.closed(1, 4000),
                       P.closed(1, 4000), P.closed(1, 4000))

    ic(chunk)

    labelstore['in'].append(chunk)

    ic(labelstore)
    # Find the workflow for 'in'
    lbl = 'in'
    modified = True

    while modified:
        labelstore, modified = process(lbl, labelstore, workflows)
        ic(labelstore)
    return 0

    groupindex = 0
    actions = workflows[lbl]
    ic(actions)

    # Now divide the parts in groups
    for action in actions:
        if len(action) == 2:
            dest = action[1]
            id = action[0][0]
            oper = action[0][1]
            value = int(action[0][2:])
            if oper == '<':
                if id == 's':
                    left = make_empty_chunk()
                    left["s"] = labelstore[lbl][groupindex]["s"] & P.closed(-P.inf, value-1)
                    left["m"] = labelstore[lbl][groupindex]["m"]
                    left["a"] = labelstore[lbl][groupindex]["a"]
                    left["x"] = labelstore[lbl][groupindex]["x"]
                    ic(left)
                    labelstore[dest].append(left)
                    right = make_empty_chunk()
                    right["s"] = labelstore[lbl][groupindex]["s"] & P.closed(value, P.inf)
                    right["m"] = labelstore[lbl][groupindex]["m"]
                    right["a"] = labelstore[lbl][groupindex]["a"]
                    right["x"] = labelstore[lbl][groupindex]["x"]
                    labelstore[lbl].pop(groupindex)
                    labelstore[lbl].append(right)
                    ic(right)
        else:
            dest = action[0]
            id = ""
            oper = ""
            value = 0
            chunk = labelstore[lbl][groupindex].copy()
            labelstore[dest].append(labelstore[lbl][groupindex])
            labelstore[lbl].pop(groupindex)
        ic(dest, id, oper, value)
        ic(labelstore)
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

part = 2


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
