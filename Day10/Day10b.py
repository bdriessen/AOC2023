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
    with open(fn) as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]

    return lines


def accessible(n1, n2, map):
    if n1[0] < 0 or n1[0] >= len(map) or n1[1] < 0 or n1[1] >= len(map[0]):
        return False
    if n2[0] < 0 or n2[0] >= len(map) or n2[1] < 0 or n2[1] >= len(map[0]):
        return False

    if not real:
        if map[n1[0]][n1[1]] == 'S' and map[n2[0]][n2[1]] != '.':
            return True
        if map[n1[0]][n1[1]] != '.' and map[n2[0]][n2[1]] == 'S':
            return True
    else:
        if map[n1[0]][n1[1]] == 'S' or map[n2[0]][n2[1]] == 'S':
            if n1[0] == n2[0]+1 or n1[0] == n2[0]-1:
                return True

    # Find relative position of n1 to n2
    if n1[0] == n2[0]:
        if n1[1] == n2[1] - 1:
            # n1 is west of n2
            return map[n1[0]][n1[1]] in ['-', 'L', 'F'] and map[n2[0]][n2[1]] in ['-', 'J', '7']
        elif n1[1] == n2[1] + 1:
            # n1 is east of n2
            return map[n2[0]][n2[1]] in ['-', 'L', 'F'] and map[n1[0]][n1[1]] in ['-', 'J', '7']

    elif n1[1] == n2[1]:
        if n1[0] == n2[0] - 1:
            # n1 is north of n2
            return map[n1[0]][n1[1]] in ['|', '7', 'F'] and map[n2[0]][n2[1]] in ['|', 'L', 'J']
        elif n1[0] == n2[0] + 1:
            # n1 is south of n2
            return map[n1[0]][n1[1]] in ['|', 'J', 'L'] and map[n2[0]][n2[1]] in ['|', '7', 'F']
    return False


def find_next_nodes(next_nodes, map, visited, crawl):
    # Find all accessible neighbors of next_nodes
    new_next_nodes = []
    new_visited = visited
    new_crawl = crawl

    for node in next_nodes:
        neighbor_candidates = [(node[0]-1, node[1]), (node[0]+1, node[1]), (node[0], node[1]-1), (node[0], node[1]+1)]
        ic(neighbor_candidates)
        for nc in neighbor_candidates:
            if accessible(nc, node, map):
                if not visited[nc]:
                    new_next_nodes.append(nc)
                    new_visited[nc] = True
                    new_crawl[nc] = new_crawl[node] + 1
    return [new_next_nodes, new_visited, new_crawl]


# Part 1
def part1(fname):
    map = read_input(fname)
    visited = np.full((len(map), len(map[0])), False)
    crawl = np.zeros((len(map), len(map[0])), dtype=int)

    start = []

    # Find start nodes
    for kr, row in enumerate(map):
        for kc, c in enumerate(row):
            if map[kr][kc] == 'S':
                start = (kr, kc)
    ic(start)
    next_nodes = [start]
    visited[start] = True

    # Find accessible neighbors
    while len(next_nodes) > 0:
        [next_nodes, visited, crawl] = find_next_nodes(next_nodes, map, visited, crawl)
        ic(next_nodes)
        ic(crawl)

    # Find longest path
    longest = np.max(crawl)
    ic(longest, visited)

    return longest, visited


# Part 2
def part2(fname):
    res1, visited = part1(fname)
    m = read_input(fname)
    mr, mc = len(m), len(m[0])

    # Find start nodes
    start = []
    for kr, row in enumerate(m):
        for kc, c in enumerate(row):
            if m[kr][kc] == 'S':
                start = (kr, kc)
                m[kr].replace('S', 'F')
    ic(start)

    map = ['.' * (mc+2)]
    for i in range(mr):
        map.append('.' + m[i] + '.')
    map.append('.' * (mc+2))

    new_map = ['O' * (mc+2)]
    for i in range(mr):
        new_map.append('O' + '*' * mc + 'O')
    new_map.append('O' * (mc+2))

    vis = [[False] * (mc+2)]
    for i in range(mr):
        vis_row = [False]
        for j in range(mc):
            vis_row.extend([visited[i][j]])
        vis_row.extend([False])
        vis.append(vis_row)
    ic(len(vis), len(vis[0]))
    # ic(map)
    # ic(new_map)

    mr = len(map)
    mc = len(map[0])

    ready = False
    while not ready:
        ready = True
        for irow in range(1, mr-1):
            for icol in range (1, mc-1):
                c = map[irow][icol]
                if c == '.' and (new_map[irow+1][icol] == 'O' or new_map[irow-1][icol] == 'O' \
                        or new_map[irow][icol+1] == 'O' or new_map[irow][icol-1] == 'O'):
                    new_map[irow] = new_map[irow][:icol] + 'O' + new_map[irow][icol+1:]
                    map[irow] = map[irow][:icol] + 'O' + map[irow][icol+1:]
                    ready = False
    # ic(new_map)

    # Calculate row by row the distance to a O of all '.' elements of map
    nrvbar = 0
    for irow in range(1, mr-1):
        inside = False
        on_A = on_B = on_C = False
        for icol in range (1, mc-1):
            c = map[irow][icol]
            prev_c = map[irow][icol-1]
            if c != '|':
                nrvbar = 0
            if c in ['O', 'I']:
                on_A = on_B = on_C = False
            elif c != '.' and vis[irow][icol]:
                if c == '|':
                    on_A = True
                    nrvbar += 1
                elif c == 'L':
                    on_B = True
                elif c == 'F':
                    on_C = True
            else:   # c == '.'
                if prev_c in ['O', 'I']:
                    new_map[irow] = new_map[irow][:icol] + prev_c + new_map[irow][icol+1:]
                    map[irow] = map[irow][:icol] + prev_c + map[irow][icol+1:]
                elif on_A:
                    for i in range(nrvbar):
                        inside = not inside
                    if inside:
                        new_map[irow] = new_map[irow][:icol] + 'I' + new_map[irow][icol+1:]
                        map[irow] = map[irow][:icol] + 'I' + map[irow][icol+1:]
                    else:
                        new_map[irow] = new_map[irow][:icol] + 'O' + new_map[irow][icol+1:]
                        map[irow] = map[irow][:icol] + 'O' + map[irow][icol+1:]
                elif on_B:
                    if prev_c == '7':
                        inside = not inside
                    if inside:
                        new_map[irow] = new_map[irow][:icol] + 'I' + new_map[irow][icol+1:]
                        map[irow] = map[irow][:icol] + 'I' + map[irow][icol+1:]
                    else:
                        new_map[irow] = new_map[irow][:icol] + 'O' + new_map[irow][icol+1:]
                        map[irow] = map[irow][:icol] + 'O' + map[irow][icol+1:]
                elif on_C:
                    if prev_c == 'J':
                        inside = not inside
                    if inside:
                        new_map[irow] = new_map[irow][:icol] + 'I' + new_map[irow][icol+1:]
                        map[irow] = map[irow][:icol] + 'I' + map[irow][icol+1:]
                    else:
                        new_map[irow] = new_map[irow][:icol] + 'O' + new_map[irow][icol+1:]
                        map[irow] = map[irow][:icol] + 'O' + map[irow][icol+1:]
                on_A = on_B = on_C = False

    ic(new_map)
    # Count nr of I's
    nr_I = 0
    for irow in range(1, mr-1):
        for icol in range (1, mc-1):
            if new_map[irow][icol] == 'I':
                nr_I += 1


    return nr_I


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
        res1, visited = part1(fname)
        nr_v=0
        for i in range(len(visited)):
            for j in range(len(visited[0])):
                if visited[i][j]:
                    nr_v += 1
        print("Part 1: ", res1, nr_v)
    else:
        res2 = part2(fname)
        print("Part 2: ", res2)

    # Stop timer
    toc = time.perf_counter()
    print(f"Time elapsed: {toc - tic:0.4f} seconds")
    return

if __name__ == "__main__":
    main()
