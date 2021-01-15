#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    qntd = int(n/len(s)) * s.count("a")
    resto = n % len(s)
    qntd += s[0:resto].count("a")
    return qntd
if __name__ == '__main__':
    s = "aba"
    n = 10
    result = repeatedString(s, n)
    print(result)