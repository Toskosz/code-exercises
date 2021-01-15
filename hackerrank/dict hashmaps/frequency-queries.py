#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


# Complete the freqQuery function below.
def freqQuery(queries):
    arr = []
    freq_check = Counter()
    ff_check = Counter()
    for x, y in queries:
        if x == 1:
            ff_check[freq_check[y]] -= 1
            freq_check[y] += 1
            ff_check[freq_check[y]] += 1
        elif x == 2:
            if freq_check[y] > 0:
                ff_check[freq_check[y]] -= 1
                freq_check[y] -= 1
                ff_check[freq_check[y]] += 1
        else:
            if ff_check[y] > 0:
                arr.append(1)
            else:
                arr.append(0)
    return arr

if __name__ == '__main__':

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)
    print(ans)
