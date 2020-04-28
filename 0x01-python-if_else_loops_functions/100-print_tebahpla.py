#!/usr/bin/python3
for alpha in range(25, -1, -1):
    letter = alpha + ord('A')
    if alpha % 2 == 1:
        letter += 32
    print("{:c}".format(letter), end="")
