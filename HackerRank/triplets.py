# CHRIS FELLI, 2019

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    ap=0
    bp=0
    if len(a) != len(b):
        return [0,0]
    for i in range(len(a)):
        if a[i] > b[i]:
            ap = ap + 1
        elif b[i] > a[i]:
            bp = bp + 1
        elif a[i] == b[i]:
            ...
    return [ap, bp]

print(compareTriplets([1,2,3],[4,5,6]))
print(compareTriplets([5,6,7],[3,6,10]))
