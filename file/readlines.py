#!/usr/bin/python3

import sys

lines = sys.stdin.readlines()
lines.sort()
for line in lines:
    # print line,
    print(line, end="")
