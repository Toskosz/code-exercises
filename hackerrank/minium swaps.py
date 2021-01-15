# 23415
# 13425 ++
# 12435 ++
# 12345 ++



#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    temp = [0] * (len(arr) + 1)
    for pos, val in enumerate(arr):
        temp[val] = pos
        pos += 1
    count = 0
    for i in range(len(arr)):
        if arr[i] != i+1:
            count += 1
            t = arr[i] # t é o valor que está na posição errada
            arr[i] = i+1 # botamos o valor correto na posição que estamos
            arr[temp[i+1]] = t #no arr no index do elemento certo botamos o elemento errado, ou seja é apenas uma troca botando o valor errado no lugar do valor certo por exemplo 21 12
            temp[t] = temp[i+1] # atualizamos o index do elemento errado para onde ele esta agora que é o index do elemento correto antes da mudança
    return count


if __name__ == '__main__':
    arr = [4, 3, 1, 2]
    res = minimumSwaps(arr)
    print(res)