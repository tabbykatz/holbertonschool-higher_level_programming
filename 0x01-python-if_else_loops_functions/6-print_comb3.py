#!/usr/bin/python3
for num in range(10):
    for num2 in range(num, 10):
        if num < num2:
            print("{:d}{:d}".format(num, num2),
                  end="\n" if num is 8 and num2 is 9 else ", ")
