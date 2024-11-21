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
        module = Module(module_name, module_type, [])
        ic(module.name, module.type)
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
            module.pulses.append("")
            module.states.append("Low")

    # And don't forget the output modules
    for module in modules:
        for outp in module.out:
            if outp not in [x.name for x in modules]:
                module2 = Module(outp, "other", [module.name])
                modules.append(module2)

    for module in modules:
        ic(str(module))
    return modules


class Module:
    module_queue = []
    nlows = 0
    nhighs = 0


    def __init__(self, *args, **kwargs):
        if len(args) == 2:
            self.name = args[0]
            self.type = args[1]
            self.inp = []
            self.out = []
            self.states = []
            self.pulses = [""]
        elif len(args) == 3:
            self.name = args[0]
            self.type = args[1]
            self.inp = args[2]
            self.pulses = [""]
            self.out = []
            self.states = []

    def __str__(self):
        return f"{self.name}, ({self.type}),  {self.inp}, Pu={self.pulses}, Out={self.out}, St={self.states}"

    def update(self, modules):
        # Update flip-flop
        if self.type == "ff":
            # Read the inputs
            toggle = False
            for i, pulse in enumerate(self.pulses):
                if pulse == "Low":
                    toggle = True
            if toggle:
                if self.states[0] == "Low":
                    self.states[0] = "High"
                    # Send a pulse to the destination
                    self.send_pulse(modules, "High")
                else:
                    self.states[0] = "Low"
                    # Send a pulse to the destination
                    self.send_pulse(modules, "Low")
            # Reset the pulses
            for i, pulse in enumerate(self.pulses):
                self.pulses[i] = ""

        elif self.type == "cj":
            # check if we received a pulse
            new_pulse = False
            for i, pulse in enumerate(self.pulses):
                if pulse in ["High", "Low"]:
                    new_pulse = True
                    self.states[i] = self.pulses[i]
                    self.pulses[i] = ""

            if new_pulse:
                all_states_high = True
                for i, state in enumerate(self.states):
                    if state == "Low":
                        all_states_high = False
                if all_states_high:
                    self.send_pulse(modules, "Low")
                else:
                    self.send_pulse(modules, "High")
                
        elif self.type == "bc":
            # send a pulse to all the outputs, but only do this if len(self.states) == 0
            if len(self.states) == 0:
                for dest in self.out:
                    self.send_pulse(modules, "Low")
                    ic("Sending from broadcaster to  ", dest)
                self.states.append("Low")

        return modules

    def update2(self, modules):
        # Updates the state of the module (self). If it has to send a pulse, it will place the pulse in de module_queue

        # Update flip-flop
        if self.type == "ff":
            # Read the inputs
            toggle = False
            for i, pulse in enumerate(self.pulses):
                if pulse == "Low":
                    toggle = True
            if toggle:
                if self.states[0] == "Low":
                    self.states[0] = "High"
                    # Add the pulse to the queue
                    for dest in self.out:
                        Module.module_queue.append([self.name, dest, "High"])
                else:
                    self.states[0] = "Low"
                    # Send a pulse to the destination
                    for dest in self.out:
                        Module.module_queue.append([self.name, dest, "Low"])
            # Reset the pulses
            for i, pulse in enumerate(self.pulses):
                self.pulses[i] = ""

        elif self.type == "cj":
            # check if we received a pulse
            new_pulse = False
            for i, pulse in enumerate(self.pulses):
                if pulse in ["High", "Low"]:
                    new_pulse = True
                    self.states[i] = self.pulses[i]
                    self.pulses[i] = ""

            if new_pulse:
                all_states_high = True
                for i, state in enumerate(self.states):
                    if state == "Low":
                        all_states_high = False
                if all_states_high:
                    for dest in self.out:
                        Module.module_queue.append([self.name, dest, "Low"])
                else:
                    for dest in self.out:
                        Module.module_queue.append([self.name, dest, "High"])

        elif self.type == "bc":
            # send a pulse to all the outputs, but only do this if len(self.states) == 0
            if len(self.states) == 0:
                for dest in self.out:
                    Module.module_queue.append([self.name, dest, "Low"])
                    ic("Sending from broadcaster to  ", dest)
                self.states.append("Low")

        return modules

    def send_pulse(self, modules, polarity):
        # Send a pulse to the destination
        # Find the module with the name dest
        for dest in self.out:
            for module in modules:
                if module.name == dest:
                    # Found the module that is connected to the source
                    # Find which input of the module is connected to the source
                    for i, inp in enumerate(module.inp):
                        if inp == self.name:
                            module.pulses[i] = polarity
                            ic(f"{self.name} -{polarity} ->{dest}")
                            Module.module_queue.append(dest)
                            if polarity == "High":
                                Module.nhighs += 1
                            else:
                                Module.nlows += 1

                    #ic(str(module))
        return


def send_pulse_from_queue(modules):
    for action in Module.module_queue:
        src = action[0]
        dest = action[1]
        polarity = action[2]
        modules = send_pulse2(src, dest, polarity, modules)
    return modules

def send_pulse2(src, dest, polarity, modules):

    # Send a pulse to all connected destination modules
    for module in modules:
        if src in module.inp:
            # Found the module that is connected to the source
            # Find which input of the module is connected to the source
            for i, inp in enumerate(module.inp):
                if inp == src:
                    module.pulses[i] = polarity
                    ic(f"{src} -{polarity} ->{module.name}")
                    if polarity == "High":
                        Module.nhighs += 1
                    else:
                        Module.nlows += 1
    return modules


def solve1(modules):

    # Find the broadcaster
    broadcaster = None
    for module in modules:
        if module.name == "broadcaster":
            broadcaster = module


    newmodules = modules

    number_of_buttons = 5
    for buttonpressed in range(number_of_buttons):
        Module.nlows += 1  # The button is pressed
        broadcaster.states = []
        Module.module_queue.append("broadcaster", "Low")
        broadcaster.send_pulse(modules, "Low")

        # Update the modules

        ic(buttonpressed, Module.module_queue)

        while len(Module.module_queue) > 0:
            # Get the first module from the queue
            module_name = Module.module_queue.pop(0)
            for i in range(len(newmodules)):
                if newmodules[i].name == module_name:
                    newmodules = newmodules[i].update(newmodules)


    # Calculate the score
    score = Module.nhighs * Module.nlows
    ic(Module.nlows, Module.nhighs, score)
    return score

def solve2(modules):

    # Find the broadcaster
    broadcaster = None
    for module in modules:
        if module.name == "broadcaster":
            broadcaster = module


    newmodules = modules

    number_of_buttons = 5
    for buttonpressed in range(number_of_buttons):
        Module.nlows += 1  # The button is pressed
        broadcaster.states = []
        for dest in broadcaster.out:
            Module.module_queue.append(["broadcaster", dest, "Low"])

        # Update the modules

        #ic(buttonpressed, Module.module_queue)

        newmodules = send_pulse_from_queue(newmodules)

        for module in newmodules:
            module.update2(newmodules)


    # Calculate the score
    score = Module.nhighs * Module.nlows
    ic(Module.nlows, Module.nhighs, score)
    return score


def score(part):

    return 0



# Part 1

def part1(fname):
    res = 0
    modules = read_input(fname)
    res = solve2(modules)
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
