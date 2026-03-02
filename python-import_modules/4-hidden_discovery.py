#!/usr/bin/python3
from hidden_4 import *

if __name__ == "__main__":
    names = dir()
    for name in sorted(names):
        if not name.startswith("__"):
            print(name)
