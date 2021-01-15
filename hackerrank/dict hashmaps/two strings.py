#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    y = set(list(s1))
    x = set(list(s2))
    for char in x:
        if char in y:
            return "Yes"
    return "No"

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)