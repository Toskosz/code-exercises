#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    valles = 0
    altitude_nova = 0
    altitude_velha = 0
    for c in s :
        if(altitude_velha >= 0 and altitude_nova < 0):
            valles += 1
        altitude_velha = altitude_nova
        if c == 'D':
            altitude_nova -= 1
        else:
            altitude_nova += 1
    return valles

if __name__ == '__main__':
    n = 8
    s = ["D", "D", "U", "U", "D", "D", "U", "D", "U", "U", "U", "D"]
    result = countingValleys(n, s)
    print(result)