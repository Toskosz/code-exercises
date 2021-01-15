#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    pos = 0
    passos = 1
    while(pos+2 < len(c)):
        if c[pos+2] == 0:

            pos += 2
            passos += 1
            if pos == (len(c) - 1):
                return passos - 1
            # elif pos + 2 >= len(c):
            #     return passos + 1
        else:
            pos += 1
            passos += 1
            if pos == (len(c) - 1):
                return passos - 1
    return passos

if __name__ == '__main__':
    c = [0, 0]
    result = jumpingOnClouds(c)
    print(result)