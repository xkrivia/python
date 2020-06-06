# CHRIS FELLI, 2019

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.


def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    size = len(arr)
    for i in range(size):
        if arr[i] > 0:
            pos += 1
        elif arr[i] < 0:
            neg += 1
        elif arr[i] == 0:
            zero += 1
    print(float(pos/size))
    print(float(neg/size))
    print(float(zero/size))
    return (float(pos/size), float(neg/size), float(zero/size))


print(plusMinus([-4, 3, -9, 0, 4, 1]))
