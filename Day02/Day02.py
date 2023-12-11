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
        # Remove everything before colon
        lines = [line.split(":")[1] for line in lines]
        # Remove newlines
        lines = [line.strip() for line in lines]
        # Split on semicolon
        lines = [line.split(";") for line in lines]
        # Remove commas
        lines = [[entry.replace(',', '') for entry in line] for line in lines]
        ic(lines)

        game_index = 0
        games = []
        for line in lines:
            grabs = []
            game = [] # List of grabs
            grab_index = 0
            for grab_string in line:
                #ic(grab_string)
                # A grab is a string containing the number of stones of each color
                grabs.append({'red': 0, 'green': 0, 'blue': 0}) # Default add an empty grab
                #ic(grabs[-1])

                grab_entry = grab_string.strip().split(' ')
                #ic(grab_entry)

                for i in range(int(len(grab_entry)/2)):
                    # Store grab_entry in dictionary with key = grab_entry[1,3,...] and value = grab_entry[0,2,...]

                    grabs[-1][grab_entry[2*i+1]] = int(grab_entry[2*i])
                
            #ic(grabs)
            games.append(grabs)
        ic(games)
    return games



# Part 1
def part1(fname):
    max_red = 12
    max_green = 13
    max_blue = 14

    games = read_input(fname)
    game_nr = 1
    sum = 0
    for game in games:
        possible = True
        for grab in game:
            if grab['red'] > max_red or grab['green'] > max_green or grab['blue'] > max_blue:
                possible = False
                break
        if possible:
           sum += game_nr
        game_nr += 1

    return -1


# Part 2
def part2(fname):
    games = read_input(fname)
    game_nr = 1
    sum = 0

    for game in games:
        min_red = min_green = min_blue = 0
        for grab in game:
            min_red = max(min_red, grab['red'])
            min_green = max(min_green, grab['green'])
            min_blue = max(min_blue, grab['blue'])
        sum += min_red*min_green*min_blue
    return sum

def main():
    real = True
    part = 2

    print("Advent of code 2023: Day 02")

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