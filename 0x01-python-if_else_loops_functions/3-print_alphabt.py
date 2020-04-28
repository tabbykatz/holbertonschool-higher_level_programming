#!/usr/bin/python3
for alpha_letters in range(ord('a'), ord('z')+1):
    if alpha_letters in [101, 113]:
        continue
    print("{:c}".format(alpha_letters), end="")
