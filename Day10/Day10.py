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
import networkx as nx


# Read input file
def read_input(fn):
    with open(fn) as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    ic(lines)
    return lines


def connect_neighbors(node, G):
    node_list = G.nodes(data=True)
    loc = node[0]

    N = N = (loc[0]-1, loc[1])
    S = (loc[0]+1, loc[1])
    W = (loc[0], loc[1]-1)
    E = (loc[0], loc[1]+1)

    if node[1]['val'] == 'S':
        if S in node_list:
            G.add_edge(loc, S)
        if N in node_list:
            G.add_edge(loc, N)
        if W in node_list:
            G.add_edge(loc, W)
        if E in node_list:
            G.add_edge(loc, E)

    elif node[1]['val'] == '|':
        if N in node_list:
            if G.nodes[N]['val'] in ['|', '7', 'F']:
                G.add_edge(loc, N)
        # Check if bottom exists
        if S in node_list:
            if G.nodes[S]['val'] in ['|', 'J', 'L']:
                G.add_edge(loc, S)
    elif node[1]['val'] == '-':
        # Check if W exists
        if W in node_list:
            if G.nodes[W]['val'] in ['L', '-', 'F']:
                G.add_edge(loc, W)
        # Check if E exists
        if E in node_list:
            if G.nodes[E]['val'] in ['J', '-', '7']:
                G.add_edge(loc, E)
    elif node[1]['val'] == 'L':
        # Check if N exists
        if N in node_list:
            if G.nodes[N]['val'] in ['|', '7', 'F']:
                G.add_edge(loc, N)
        # Check if E exists
        if E in node_list:
            if G.nodes[E]['val'] in ['J', '-', '7']:
                G.add_edge(loc, E)
    elif node[1]['val'] == '7':
        # Check if S exists
        if S in node_list:
            if G.nodes[S]['val'] in ['|', 'J', 'L']:
                G.add_edge(loc, S)
        # Check if W exists
        if W in node_list:
            if G.nodes[W]['val'] in ['L', '-', 'F']:
                G.add_edge(loc, W)
    elif node[1]['val'] == 'F':
        # Check if S exists
        if S in node_list:
            if G.nodes[S]['val'] in ['|', 'J', 'L']:
                G.add_edge(loc, S)
        # Check if E exists
        if E in node_list:
            if G.nodes[E]['val'] in ['J', '-', '7']:
                G.add_edge(loc, E)
    elif node[1]['val'] == 'J':
        # Check if N exists
        if N in node_list:
            if G.nodes[N]['val'] in ['|', '7', 'F']:
                G.add_edge(loc, N)
        # Check if W exists
        if W in node_list:
            if G.nodes[W]['val'] in ['L', '-', 'F']:
                G.add_edge(loc, W)

    return G


# Part 1
def part1(fname):
    map = read_input(fname)
    start = []
    G = nx.Graph()
    # Add nodes
    for kr, row in enumerate(map):
        for kc, c in enumerate(row):
            if c != '.':
                G.add_node((kr, kc), val=c, loc=(kr, kc))
            if map[kr][kc] == 'S':
                start = (kr, kc)
    #node_list = G.nodes(data=True)
    #ic((2,0) in node_list)
    #ic(G.nodes[(2,0)]['val'])
    #x = G.nodes[(2,0)]['loc']
    #ic(x[0])
    #ic(G.nodes[(2,0)])
    #ic(node_list)
    #ic(G.nodes(data=True))

    # Add edges
    for node in G.nodes(data=True):
        #ic(node[1])
        G = connect_neighbors(node, G)
    ic(G.nodes())
    # Find largest distance in graph
    dist = nx.all_pairs_shortest_path_length(G)
    ic(G.nodes())
    longest = 0
    for node in G.nodes():
        ic(node, G.nodes[(2,0)])
        if nx.has_path(G, start, node):
            d = nx.shortest_path_length(G, start, node)
            if d > longest:
                longest = d
                ic(node, longest)
            ic(d)

    return longest


# Part 2
def part2(fname):
    return 0




def main():
    real = True
    verbose = False
    part = 1

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
