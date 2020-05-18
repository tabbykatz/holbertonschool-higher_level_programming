#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as code:
        print("Exception: {}".format(code), file=sys.stderr)
        return None
