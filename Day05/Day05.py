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

        # First line is seeds
        line = f.readline().strip()
        # Seperate by spaces
        line = line.split(" ")
        seeds = []
        for token in line:
            if token.isnumeric():
                seeds.append(int(token))
        ic(seeds)
        line = f.readline().strip() # empyt line

        seed2soil = []
        line = f.readline().strip() # header
        line = f.readline().strip() # First mapping line
        while (line != ""):
            line = line.split(" ") #values
            nums = []
            for token in line:
                if token.isnumeric():
                    nums.append(int(token))
            seed2soil.append(nums)
            ic(seed2soil)
            line = f.readline().strip()

        soil2fert = []
        line = f.readline().strip() # header
        line = f.readline().strip() # First mapping line
        while (line != ""):
            line = line.split(" ") #values
            nums = []
            for token in line:
                if token.isnumeric():
                    nums.append(int(token))
            soil2fert.append(nums)
            ic(soil2fert)
            line = f.readline().strip()

        fert2wat = []
        line = f.readline().strip() # header
        line = f.readline().strip() # First mapping line
        while (line != ""):
            line = line.split(" ") #values
            nums = []
            for token in line:
                if token.isnumeric():
                    nums.append(int(token))
            fert2wat.append(nums)
            ic(fert2wat)
            line = f.readline().strip()

        wat2light = []
        line = f.readline().strip() # header
        line = f.readline().strip() # First mapping line
        while (line != ""):
            line = line.split(" ") #values
            nums = []
            for token in line:
                if token.isnumeric():
                    nums.append(int(token))
            wat2light.append(nums)
            ic(wat2light)
            line = f.readline().strip()

        light2temp = []
        line = f.readline().strip() # header
        line = f.readline().strip() # First mapping line
        while (line != ""):
            line = line.split(" ") #values
            nums = []
            for token in line:
                if token.isnumeric():
                    nums.append(int(token))
            light2temp.append(nums)
            ic(light2temp)
            line = f.readline().strip()

        temp2hum = []
        line = f.readline().strip() # header
        line = f.readline().strip() # First mapping line
        while (line != ""):
            line = line.split(" ") #values
            nums = []
            for token in line:
                if token.isnumeric():
                    nums.append(int(token))
            temp2hum.append(nums)
            ic(temp2hum)
            line = f.readline().strip()

        hum2loc = []
        line = f.readline().strip()  # header
        line = f.readline().strip()  # First mapping line
        while (line != ""):
            line = line.split(" ")  # values
            nums = []
            for token in line:
                if token.isnumeric():
                    nums.append(int(token))
            hum2loc.append(nums)
            ic(hum2loc)
            line = f.readline().strip()

    return seeds, seed2soil, soil2fert, fert2wat, wat2light, light2temp, temp2hum, hum2loc

def mapit(inp, mapping):
    out = []
    for i in inp:
        found = False
        for row in mapping:
            if i >= row[1] and i<row[1]+row[2]:
                # We found a match
                found = True
                offset = i - row[1]
                out.append(row[0]+offset)
                break
        if not found:
            out.append(i)
    return out
# Part 1
def part1(fname):
    seeds, seed2soil, soil2fert, fert2wat, wat2light, light2temp, temp2hum, hum2loc = read_input(fname)

    soil = mapit(seeds, seed2soil)
    fert = mapit(soil, soil2fert)
    wat = mapit(fert, fert2wat)
    light = mapit(wat, wat2light)
    temp = mapit(light, light2temp)
    hum = mapit(temp, temp2hum)
    loc = mapit(hum, hum2loc)


    return min(loc)

def map2intervals(mapping):
    out = []
    for row in mapping:
        out.append([row[1], row[1]+row[2]-1, row[0], row[0]+row[2]-1])
    return out


def removeInterval(intervals, toBeRemoved):

    res = []

    for interval in intervals:
        if interval[0] > interval[1]:
            ic()
        if interval[1] < toBeRemoved[0] or interval[0] > toBeRemoved[1]:
            # Case 1 - Does not overlap
            res.append(interval)
        elif toBeRemoved[0] <= interval[0] and toBeRemoved[1] >= interval[1]:
            # Case 2 - Completely inside
            pass
        elif toBeRemoved[0] < interval[0] and toBeRemoved[1] <= interval[1]:
            # Case 3 - Partial overlap on right side
            res.append([toBeRemoved[1]+1, interval[1]])
        elif toBeRemoved[0] >= interval[0] and toBeRemoved[1] > interval[1]:
            # Case 3 - Partial overlap on left side
            res.append([interval[0], toBeRemoved[0]-1])
        elif toBeRemoved[0] > interval[0] and toBeRemoved[1] < interval[1]:
            # Case 3 - Interval completely surrounded
            res.append([interval[0], toBeRemoved[0]-1])
            res.append([toBeRemoved[1]+1, interval[1]])
        elif toBeRemoved[0] == interval[0] and toBeRemoved[1] < interval[1]:
            # Case 4 - Interval starts at same point
            res.append([toBeRemoved[1]+1, interval[1]])
        elif toBeRemoved[0] > interval[0] and toBeRemoved[1] == interval[1]:
            # Case 4 - Interval ends at same point
            res.append([interval[0], toBeRemoved[0]-1])

    return res

def convertinterval(intervals, imap):
    ic(intervals, imap)
    interval_out = []

    in_intervals = intervals
    intervals_to_remove = []
    for map in imap:
        # Check if interval is in range
        for interval in in_intervals:
            match = True
            if interval[1] < map[0]:
                match = False
            if interval[0] > map[1]:
                match = False
            out = []
            if match:
                # Case: interval is larger than map
                if interval[0] <= map[0] and interval[1] >= map[1]:
                    out = []
                    offset = map[2] - map[0]
                    # First part of interval is unchanged
                    segment2 = [map[0]+offset, map[1]+offset]        # Mapped
                    out.append(segment2)
                    intervals_to_remove.append([map[0], map[1]])

                # Case: interval in contained in map
                elif interval[0] >= map[0] and interval[1] <= map[1]:
                    out = []
                    offset = map[2] - map[0]
                    segment1 = [interval[0]+offset, interval[1]+offset]
                    out.append(segment1)
                    intervals_to_remove.append([interval[0], interval[1]])
                # Case: interval overlaps with top of map
                elif interval[0] < map[0]:
                    out = []
                    offset = map[2] - map[0]
                    segment2 = [map[0]+offset,interval[1]+offset] # Mapped
                    out.append(segment2)
                    intervals_to_remove.append([map[0], interval[1]])
                # Case: interval overlaps with bottom of map
                elif interval[1] > map[1]:
                    out = []
                    offset = map[2] - map[0]
                    segment1 = [interval[0]+offset, map[1]+offset] # Mapped
                    segment2 = [map[1]+1, interval[1]] # Unchanged
                    out.append(segment1)
                    intervals_to_remove.append([interval[0], map[1]])
            for o in out:
                interval_out.append(o)

    in_intervals = intervals
    for e in intervals_to_remove:
        in_intervals = removeInterval(in_intervals, e)
    for e in in_intervals:
        interval_out.append(e)
    ic(interval_out)
    return interval_out

# Part 2
def part2(fname):

    ic.disable()
    seeds, seed2soil, soil2fert, fert2wat, wat2light, light2temp, temp2hum, hum2loc = read_input(fname)

    # Convert seeds to intervals
    iseeds = []
    for i in range(int(len(seeds)/2)):
        s = [seeds[2*i], seeds[2*i]+seeds[2*i+1]]
        iseeds.append(s)

    iseeds2soil = map2intervals(seed2soil)
    isoil2fert = map2intervals(soil2fert)
    ifert2wat = map2intervals(fert2wat)
    iwat2light = map2intervals(wat2light)
    ilight2temp = map2intervals(light2temp)
    itemp2hum = map2intervals(temp2hum)
    ihum2loc = map2intervals(hum2loc)


    # Convert intervals
    intervals = iseeds
    intervals = convertinterval(intervals, iseeds2soil)
    intervals = convertinterval(intervals, isoil2fert)
    intervals = convertinterval(intervals, ifert2wat)
    intervals = convertinterval(intervals, iwat2light)
    intervals = convertinterval(intervals, ilight2temp)
    intervals = convertinterval(intervals, itemp2hum)
    intervals = convertinterval(intervals, ihum2loc)

    minloc = 10000000000000000
    for interval in intervals:
        if interval[0] < minloc:
            minloc = interval[0]

    return minloc



def main():
    real = True
    part = 2

    print("Advent of code 2023: Day 04")

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

ic.enable()
main()