#!/usr/bin/python3
if __name__ == "__main__":
    import sys

answer = 0

for i in range(1, len(sys.argv)):
    answer += int(sys.argv[i])
print("{:d}".format(answer))
