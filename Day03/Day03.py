#
# Advent of code 2023: Day 02
#
# Author: Bart Driessen
# Start date: 2023-01-23
# Part 1 done:
# Part 2 done:
#

import numpy as np
import time
from icecream import ic

# Read input file
def read_input(fn):
    with open(fn) as f:
        lines = f.readlines()
        # Remove '\n' from each line
        lines = [x.strip() for x in lines]
    ic(lines)

    return lines

def find_numbers(line, line_nr):
    nums = []
    num = {}

    in_num = False
    for i in range(len(line)):
        if line[i].isdigit():
            if not in_num:
                num['start'] = i
                num['line_nr'] = line_nr
                num['val'] = int(line[i])
                num['end'] = i
                in_num = True
                if i == len(line)-1:
                    nums.append(num)
            else:
                num['end'] = i
                num['val'] = 10*num['val'] + int(line[i])
                if i == len(line)-1:
                    nums.append(num)
        else:
            if in_num:
                nums.append(num)
                num = {}
            in_num = False

    return nums

def check_gear(loc, all_nums):
    # Count number of numbers touching star
    num_touch = 0
    val1 = val2 = 0
    for num in all_nums:
        touching = False
        if loc[0] == num['line_nr']:
            if loc[1]==num['start']-1 or loc[1] == num['end']+1:
                touching = True
        elif loc[0] == num['line_nr']-1:
            if loc[1]>=num['start']-1 and loc[1]<=num['end']+1:
                touching = True
        elif loc[0] == num['line_nr']+1:
            if loc[1]>=num['start']-1 and loc[1]<=num['end']+1:
                touching = True
        if touching:
            num_touch += 1
            #ic(loc,num_touch, num)

            if num_touch == 1:
                val1 = num['val']
            elif num_touch == 2:
                val2 = num['val']
    if num_touch != 2:
        return False, -1
    else:
        #ic(loc, val1, val2)
        return True, val1*val2


def check_part(num, lines):
    ic(num)
    start = num['start']
    end = num['end']
    line_nr = num['line_nr']
    len_line = len(lines[line_nr])
    is_part = False
    # Check symbol above line symbol above and below num['line_nr'] there is a symbol that is not a number or a '.'
    if line_nr > 0:
        line_above = lines[line_nr-1]
        for char in line_above[max(0,start-1):min(len_line, end+2)]:
            if char != '.' and not char.isdigit():
                is_part = True
                break
    # Check symbol below line symbol above and below num['line_nr'] there is a symbol that is not a number or a '.'
    if line_nr < len(lines)-1:
        line_below = lines[line_nr+1]
        for char in line_below[max(0,start-1):min(len_line, end+2)]:
            if char != '.' and not char.isdigit():
                is_part = True
                break
    # Check if symbol left num['start'] is not a number or a '.'
    if start > 0:
        if lines[line_nr][start-1] != '.':
            is_part = True
    # Check if symbol right num['end'] is not a number or a '.'
    if end < len_line-1:
        if lines[line_nr][end+1] != '.':
            is_part = True

    return is_part
# Part 1
def part1(fname):
    lines = read_input(fname)
    line_nr = 0
    sum_parts = 0
    for line in lines:
        nums = find_numbers(line, line_nr) # Nums is list of dicts. Dict has keys: 'num', 'start', 'end', 'line_nr'
        for num in nums:
            #is_part = False
            is_part = check_part(num, lines)
            if is_part:
                sum_parts += num['val']
        line_nr += 1
        ic(nums)
    return sum_parts


# Part 2
def part2(fname):
    lines = read_input(fname)
    line_nr = 0
    sum_parts = 0
    all_nums = []
    for line in lines:
        nums = find_numbers(line, line_nr) # Nums is list of dicts. Dict has keys: 'num', 'start', 'end', 'line_nr'
        for num in nums:
            all_nums.append(num)
        line_nr += 1
    ic(all_nums)

    sum_gear_ratios = 0
    for line_idx, line in enumerate(lines):
        for sym_idx, sym in enumerate(line):
            if sym=='*':
                loc = [line_idx, sym_idx]
                is_gear, gear_ratio = check_gear(loc, all_nums)
                if is_gear:
                    sum_gear_ratios += gear_ratio
                    ic(loc, gear_ratio, sum_gear_ratios)
    return sum_gear_ratios


def main():
    real = True
    part = 2

    print("Advent of code 2023: Day 03")

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

main()