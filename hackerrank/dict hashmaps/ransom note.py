#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    mag_counter = Counter(magazine)
    note_counter = Counter(note)
    for word in note:
        if word not in magazine or note_counter[word] > mag_counter[word]:
            return print("No")
    return print("Yes")


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
