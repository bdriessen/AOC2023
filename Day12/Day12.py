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
    springs = []
    orders = []

    with open(fn) as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]

    for line in lines:
        # Split string in tokens
        tokens = re.split(" ", line)

        springs.append(tokens[0])
        for token in tokens[1:]:
            num = [int(i) for i in re.findall(r'\d+', token)]
            orders.append(num)
#    ic(springs, orders)

    return springs, orders


def print_seq(seq, order, spring):
    sol_spring = ['.' for i in range(len(spring))]
    for i in range(len(seq)):
        start = seq[i]
        for j in range(order[i]):
            sol_spring[start+j] = '#'

    # print sol_spring string at the of the line overwriting the previous line
    print("\033[F"*len(spring), end="")
    # convert sol_spring to string
    sol_spring = ''.join(sol_spring)
    print(sol_spring)
    return


def solve(spring, order, seq):
    global nr_of_solutions
    #ic(seq)
    seqs = []
    if len(seq) == len(order):
        #ic(seq)
        #seqs.append(seq)
        if is_matching(seq, order, spring):
            #solutions.append(seq)
            nr_of_solutions += 1
            ic(nr_of_solutions, seq)
            print(nr_of_solutions, seq)

    else:
        if not seq:
            first_start_next_seq = 0
            last_start_next_seq = len(spring) -1
            min_size_remaining_seq = 0
        else:
            first_start_next_seq = seq[-1] + order[len(seq)-1] + 1  # +1 because of the dot
            # calculate last start next seq that might be useful
            # Then calculate the minimum size of the remaining sequence
            min_size_remaining_seq = 0
            for i in range(len(seq)+1, len(order)):
                min_size_remaining_seq += order[i] + 1 # +1 because of the mandatory ?
            #ic(seq, min_size_remaining_seq)
            # Then calculate the last useful index:
            last_start_next_seq = len(spring) - min_size_remaining_seq - 1
            #print("Last start", last_start_next_seq, seq)

        for i in range(first_start_next_seq, last_start_next_seq+1):
            will_not_fit = False

            for j in range(order[len(seq)]):
                if i+j >= len(spring):
                    will_not_fit = True
                elif spring[i+j] == '.':
                    will_not_fit = True
                after_seq_index = i + order[len(seq)]
                if after_seq_index < len(spring):
                    if spring[after_seq_index] in ['#', '?']:
                        will_not_fit = True

            if will_not_fit:
                continue

            #print(i)
            #ic(i, seq, first_start_next_seq)
            extension_possible = True
            if i + order[len(seq)] > len(spring) - min_size_remaining_seq:
                extension_possible = False

            if extension_possible:
                #print_seq(seq, order, spring)
                # Solve for extended sequence
                if i==first_start_next_seq and verbose:
                    print("investigating", i, seq)
                solve(spring, order, seq + [i])

    #ic(seqs)
    return


def solve2(spring, order, seq):
    global nr_of_solutions
    #ic(seq)
    if len(seq) == len(order):
        #ic(seq)
        if is_matching(seq, order, spring):
            #solutions.append(seq)
            nr_of_solutions += 1
            ic(nr_of_solutions, seq)
            #print(nr_of_solutions, seq)

    else:
        if not seq:
            idx_next_seq = 0
            start_next_seq = 0
        else:
            start_next_seq = seq[-1] + order[len(seq)-1] + 1  # +1 because of the dot
            idx_next_seq = len(seq)

        # Skip dots in front of the next sequence
        if start_next_seq < len(spring):
            while spring[start_next_seq] == '.':
                start_next_seq += 1
                if start_next_seq >= len(spring):
                    return

        min_size_remaining_seq = 0
        for i in range(len(seq) + 1, len(order)):
            min_size_remaining_seq += order[i] + 1  # +1 because of the mandatory ?
        # ic(seq, min_size_remaining_seq)

        # Then calculate the last useful index for placing the next sequence
        last_start_next_seq = len(spring) - min_size_remaining_seq - 1

        for loc in range(start_next_seq, len(spring)):
            will_fit = True
            try_next_loc = True

            if loc > last_start_next_seq:
                will_fit = False
                try_next_loc = False

            # Check if the entire sequence will fit
            for i in range(order[idx_next_seq]):
                if loc+i >= len(spring):
                    will_fit = False
                    try_next_loc = False
                    break
                if spring[loc+i] not in ['#', '?']:
                    will_fit = False
                    try_next_loc = True
                    break

            # Check if after placing the sequence on this location, there is a dot
            idx_after_seq = loc + order[idx_next_seq]
            if idx_after_seq < len(spring):
                if spring[idx_after_seq] not in ['.', '?']:
                    will_fit = False

            # print("investigating", seq + [loc])
            if will_fit and try_next_loc:
                solve2(spring, order, seq + [loc])

            # Only try next location if we can place a dot on this location or if there is already a dot
            if spring[loc] == '#' or not try_next_loc:
                break

    return


def solve3(spring, order):
    # Breadth first search implementation
    # Start with empty sequence
    nodes = []
    node = {"id": spring[0], 'ch': [], 'amount': 0}
    if spring[node['amount']] == '.':
        node['ch'] = ['.']
    elif spring[node['amount']] == '#':
        node['ch'] = ['#']
    else:
        node['ch'] = ['.', '#']
    nodes.append(node)
    queue = [node]
    visited = []

    while queue:
        # Dequeue a node
        node = queue.pop(0)
        # Check if the node is visited
        if node not in visited:
            visited.append(node)
            # Get all neighbours of the node
            children = get_children(node, spring, order)
            # Add children to the queue
            for child in children:
                if still_possible(child, order):
                    queue.append(child)
    return 0


def solve4(spring, order):
    global nr_of_solutions

    if len(order) == 0:
        # This is a solution
        for i in range(len(spring)):
            if spring[i] == '#':
                return 0
        nr_of_solutions += 1
        return 0

    # check all possible sequences of first element of order in spring, and then check if the rest fits
    seq = order[0]
    still_possible = True

    for i in range(len(spring)):

        # Check if the  seq fits all places in the spring
        will_fit = True
        for j in range(seq):
            if i+j >= len(spring):
                will_fit = False
                return 0
            elif spring[i+j] == '.':
                will_fit = False

        # If the sequence fits, we still must check if the next token is not a # (if the we are not at the end
        # of the spring), or if we arrived at the end of the springs
        if will_fit:
            if i+seq < len(spring):
                if spring[i+seq] in ['.', '?']:
                    solve4(spring[(i+seq+1):], order[1:])
                else:
                    # Not an allocation of the sequence, try next place
                    continue
            else:
                # This is a solution
                solve4(spring[(i+seq+1):], order[1:])
        if spring[i] == '#':
            return 0

    return 0


def get_children(node, spring, order):
    children = []

    if len(node['ch']) == 1:
        if node['ch'][0] == '.':
            # Add child with a dot
            id = node['id'] + '.'
            child = {"id": id, 'ch': [], 'amount': node['amount']+1}
            if node['amount'] < len(spring):
                if spring[node['amount']] == '.':
                    child['ch'] = ['.']
                elif spring[node['amount']] == '#':
                    child['ch'] = ['#']
                else:
                    child['ch'] = ['.', '#']
            children.append(child)
        else:
            # Add child with a #
            id = node['id'] + '#'
            child = {"id": id, 'ch': [], 'amount': node['amount']+1}
            if node['amount'] < len(spring):
                if spring[node['amount']] == '.':
                    child['ch'] = ['.']
                elif spring[node['amount']] == '#':
                    child['ch'] = ['#']
                else:
                    child['ch'] = ['.', '#']
            children.append(child)
    else:
        # Add child with a dot and a child with a #
        id = node['id'] + '.'
        child = {"id": id, 'ch': [], 'amount': node['amount']+1}
        if node['amount'] < len(spring):
            if spring[node['amount']] == '.':
                child['ch'] = ['.']
            elif spring[node['amount']] == '#':
                child['ch'] = ['#']
            else:
                child['ch'] = ['.', '#']
        children.append(child)
        id = node['id'] + '#'
        child = {"id": id, 'ch': [], 'amount': node['amount']+1}
        if node['amount'] < len(spring):
            if spring[node['amount']] == '.':
                child['ch'] = ['.']
            elif spring[node['amount']] == '#':
                child['ch'] = ['#']
            else:
                child['ch'] = ['.', '#']
    return children


def is_matching(seq, order, spring):
    sol_spring = ['.' for i in range(len(spring))]
    for i in range(len(seq)):
        start = seq[i]
        for j in range(order[i]):
            sol_spring[start+j] = '#'

    is_ok = True
    for i in range(len(spring)):
        if sol_spring[i] == '.' and spring[i] == '.':
            continue
        elif sol_spring[i] == '.' and spring[i] == '?':
            continue
        elif sol_spring[i] == '#' and spring[i] == '#':
            continue
        elif sol_spring[i] == '#' and spring[i] == '?':
            continue
        else:
            is_ok = False
            break
    return is_ok


# Part 1
def part1(fname):
    global nr_of_solutions
    springs, orders = read_input(fname)
    total_nr_of_solutions = 0
    for i in range(len(springs)):

        nr_of_solutions = 0
        solve2(springs[i], orders[i], [])
        total_nr_of_solutions += nr_of_solutions
        ic(i, nr_of_solutions)
    return total_nr_of_solutions


def part1_a(fname):
    global nr_of_solutions
    springs, orders = read_input(fname)
    nr_of_solutions = 0
    ic(springs)
    ic(orders)
    # Find all possible allocation of first sequence in springs
    seq = orders[0]
    for i in range(len(springs)):
        solve4(springs[i], orders[i])
        ic(i, nr_of_solutions)
    return nr_of_solutions


# Part 2
def part2(fname):
    global nr_of_solutions
    springs, orders = read_input(fname)
    # ic(orders)
    springs2 = []
    orders2 = []
    for spring in springs:
        new_spring = spring+'?'+spring+'?'+spring+'?'+spring+'?'+spring
        springs2.append(new_spring)
    for order in orders:
        new_order = order+order+order+order+order
        orders2.append(new_order)
    # ic(orders2)

    total_nr_of_solutions = 0
    for i in range(len(springs)):
        print("Solving spring", i)
        nr_of_solutions = 0
        solve2(springs2[i], orders2[i], [])
        total_nr_of_solutions += nr_of_solutions
        print(i, nr_of_solutions)
    return total_nr_of_solutions


real = True
verbose = True
part = 1

solutions = []
nr_of_solutions = 0


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
        res1 = part1_a(fname)
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
