#!/usr/bin/python3
import sys

answer = 0

if len(sys.argv) == 1:
    print("{:d}".format(len(sys.argv) - 1))
if len(sys.argv) >= 2:
    for i in range(1, len(sys.argv)):
        answer += int(sys.argv[i])
    print("{:d}".format(answer))
