#!/usr/bin/python3

import sys


def filter_files(name, function):
    with open(name, "r") as input, open(name + ".out") as ouput:
        for line in input:
            ouput.write(function(line), end="")


def filter_stream(function):
    for line in sys.stdin.readlines():
        print(function(line), end="")
