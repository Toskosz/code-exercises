#!/bin/python3

# columns = len(an_array[0])
# rows = len(an_array)

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    results = []
    for i in range(0, len(arr)-2):
        for j in range(0, len(arr[0])):
            sum = sum(arr[i][j:j+3])
            sum += arr[i+1][j+1]
            sum += sum(arr[i+2][j:j+3])
            results.append(sum)
    return max(results)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
