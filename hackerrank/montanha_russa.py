#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the minimumBribes function below.
def minimumBribes(q):
    bribes = 0
    for i in range(0, len(q)):
        if q[i] - (i+1) > 2:
            print("Too chaotic")
            return
        for j in range(max(q[i]-2, 0), i):
            if q[j] > q[i]:
                bribes += 1
    print(bribes)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)