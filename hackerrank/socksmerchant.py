#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    x = 0
    banco = []
    for s in ar:
        if s in banco:
            continue
        else:
            x += int(ar.count(s) / 2)
            banco.append(s)
    return x


if __name__ == '__main__':
    n = 9

    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

    result = sockMerchant(n, ar)
    print(result)
