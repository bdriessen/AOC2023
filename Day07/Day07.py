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

# Read input file
def read_input(fn):
    with open(fn) as f:
        lines = f.readlines()
    lines = [x.strip() for x in lines]
    # split each line into 2 strings seperated by a space
    lines = [x.split(" ") for x in lines]

    deck = []
    for line in lines:
        card = {'hand':line[0], 'bid': int(line[1])}
        deck.append(card)

    ic(deck)
    return deck

def card2hex(card):
    val = ''
    hand = card['hand']
    ic(hand)
    for i in range(5):
        if hand[i].isdigit():
            dig = hand[i]
        else:
            if hand[i] == 'T':
                dig = 'A'
            elif hand[i] == 'J':
                dig = '1'
            elif hand[i] == 'Q':
                dig = 'C'
            elif hand[i] == 'K':
                dig = 'D'
            elif hand[i] == 'A':
                dig = 'E'

        val = val+dig
    return val

def histogram(card):
    # return histogram of hand
    # histogram is a list with 5 elements
    # each element is the number of occurences of a digit in the hand
    hist = []
    for i in range(5):
        hist.append(card['hand'].count(card['hand'][i]))
    return hist

def is_5card(card):
    # return True if hand is a 5-card
    # return False otherwise
    hist = histogram(card)
    if 5 in hist:
        return True
    else:
        return False

def is_4card(card):
    # return True if hand is a 4-card
    # return False otherwise
    hist = histogram(card)
    if 4 in hist:
        return True
    else:
        return False

def is_fullhouse(card):
    # return True if hand is a full house
    # return False otherwise
    hist = histogram(card)
    if 3 in hist and 2 in hist:
        return True
    else:
        return False

def is_3card(card):
    # return True if hand is a 3-card
    # return False otherwise
    hist = histogram(card)
    if 3 in hist and 2 not in hist:
        return True
    else:
        return False

def is_2pair(card):
    # return True if hand is a 2-pair
    # return False otherwise
    hist = histogram(card)
    if hist.count(2) == 4:
        return True
    else:
        return False

def is_1pair(card):
    # return True if hand is a 1-pair
    # return False otherwise
    hist = histogram(card)
    if hist.count(2) == 2 and hist.count(1) == 3:
        return True
    else:
        return False


def is_highcard(card):
    # return True if hand is a high card
    # return False otherwise
    hist = histogram(card)
    if hist.count(1) == 5:
        return True
    else:
        return False


def value1(card):

    if is_5card(card):
        return 7
    elif is_4card(card):
        return 6
    elif is_fullhouse(card):
        return 5
    elif is_3card(card):
        return 4
    elif is_2pair(card):
        return 3
    elif is_1pair(card):
        return 2
    elif is_highcard(card):
        return 1
    else:
        return 0


def value2(card):
    ic(card['hex'], int(card['hex'], 16))
    return int(card['hex'], 16)


# Part 1
def part1(fname):
    deck = read_input(fname)

    for card in deck:
        card['hex'] = str(value1(card))+card2hex(card)
    deck.sort(key=value2, reverse=True)
    ic(deck)

    sum = 0
    for idx, card in enumerate(deck):
        sum += card['bid']*(len(deck)-idx)
    return sum


def get_max_hand(card):
    best_card = card
    best_score = value1(card)
    for joker in ['2','3','4','5','6','7','8','9','T','J','Q','K','A']:
        new_card = card.copy()
        new_card['hand'] = new_card['hand'].replace('J', joker)
        new_score = value1(new_card)
        if new_score > best_score:
            best_card = new_card
            best_score = new_score
    return best_card


# Part 2
def part2(fname):
    ic.disable()
    deck = read_input(fname)
    best_deck = []
    for card in deck:
        best_card = get_max_hand(card)
        best_card['hex'] = str(value1(best_card))+card2hex(card)
        best_deck.append(best_card)

    best_deck.sort(key=value2, reverse=True)
    ic(best_deck)

    sum = 0
    for idx, card in enumerate(best_deck):
        sum += card['bid']*(len(best_deck)-idx)
    return sum


def main():
    real = True
    part = 2


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
